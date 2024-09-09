import inspect


def func_inject_dependencies(func):
    """
    装饰器，用于自动注入方法的依赖项。
    """
    def wrapper(*args, **kwargs):
        def get_instance(cls):
            """
            动态创建并返回依赖项的实例。
            """
            if not hasattr(get_instance, "_registry"):
                get_instance._registry = {}
            
            if cls not in get_instance._registry:
                instance = cls()
                get_instance._registry[cls] = instance
            
            return get_instance._registry[cls]
        # 获取方法的所有依赖项
        signature = inspect.signature(func)
        dependencies = {}
        for param_name, param in signature.parameters.items():
            if param_name in ['self', 'cls'] + list(args) + list(kwargs.keys()):
                continue
            # 动态创建并注入依赖项
            dependency_cls = param.annotation
            if dependency_cls is param.empty:
                raise ValueError(f"Missing type annotation for parameter '{param_name}' in {func.__qualname__}")
            dependencies[param_name] = get_instance(dependency_cls)
        
        # 调用原始方法
        return func(*args, **{**kwargs, **dependencies})
    
    return wrapper

def class_inject_dependencies(cls):
    """
    装饰器，用于为目标类自动注入依赖项。
    """
    class DecoratedClass(cls):
        def __init__(self, *args, **kwargs):
            # 获取类的所有依赖项
            init_signature = inspect.signature(cls.__init__)
            dependencies = {}
            for param_name, param in init_signature.parameters.items():
                if param_name == 'self' or param_name in kwargs:
                    continue
                # 动态创建并注入依赖项
                dependency_cls = param.annotation
                if dependency_cls is param.empty:
                    raise ValueError(f"Missing type annotation for parameter '{param_name}' in {cls.__name__}")
                dependencies[param_name] = DecoratedClass.get_instance(dependency_cls)
            
            # 调用原始的 __init__ 方法来创建类的实例
            super(DecoratedClass, self).__init__(*args, **{**kwargs, **dependencies})
        
        def get_instance(cls):
            """
            动态创建并返回依赖项的实例。
            """
            if not hasattr(DecoratedClass.get_instance, "_registry"):
                DecoratedClass.get_instance._registry = {}
            
            if cls not in DecoratedClass.get_instance._registry:
                instance = cls()
                DecoratedClass.get_instance._registry[cls] = instance
            
            return DecoratedClass.get_instance._registry[cls]
    print("依赖注入成功")
    return DecoratedClass