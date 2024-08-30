import pathlib
import json

from typing import List,Any

from .exception import *

config_register: dict = {
    'SUPER_USERS': ['']
}
"""注册配置项名称"""

class Config:
    """配置项类
    """
    
    SUPER_USERS: List[str]
    """超级用户列表
    """
    
def create_config():
    """创建初始化配置文件
    """
    if not pathlib.Path('config.cfg').is_file():
        with open('config.cfg','w') as f:
            f.write(json.dumps(config_register))
        print('初始化配置项成功')
    
def load_config():
    """加载配置项
    """
    create_config()
    with open('config.cfg','r') as f:
        data: dict = json.loads(f.read())
    
    # 更新对应配置类的值
    Config.SUPER_USERS = data.get('SUPER_USERS')
    print('Config loaded successful')
    
def update_config(config: str,value: Any):
    """更新配置项
    """
    if config_register.get(config):
        with open('config.cfg','r') as f:
            data: dict = json.loads(f.read())
        data[config] = value
        with open('config.cfg','w') as f:
            f.write(json.dumps(data))
        load_config()
        print(f'配置 {config} 的值已更新为：{value}')
    else:
        raise ConfigNotExistError('配置项不存在')