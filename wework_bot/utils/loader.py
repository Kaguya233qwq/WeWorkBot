import os
import sys
import traceback

from importlib import import_module

def load_plugins_from_local():
    """加载所有本地插件
    """
    pkg_list = os.listdir('plugins')
    if "__pycache__" in pkg_list:
        pkg_list.remove('__pycache__')
    if pkg_list != [] or pkg_list != ['']:
        for pkg in pkg_list:
            try:
                pkg = pkg.strip('.py')
                import_module(f'plugins.{pkg}')
                print(f'插件 {pkg} 加载成功')
            except Exception as e:
                print(f'插件 {pkg} 未能成功加载，原因：')
                print(traceback.format_exc())
                sys.exit(-1)
        