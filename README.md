# 基于ntwork的二次开发项目

> [!CAUTION]\
> **请不要在tencent官方群聊和任何影响力较大的简中互联网平台（包括但不限于: 哔哩哔哩，微博，知乎，抖音等）发布和讨论*任何*与本项目存在相关性的信息**

## 自动回复如此简便，快速构建你的业务逻辑

下面是一个示例插件的内容

```python
import ntwork

from wework_bot.fuctions.action import reply_msg, wework
from wework_bot.rule import Rule
from wework_bot import run


@wework.msg_register(ntwork.MT_RECV_TEXT_MSG)
def msg_handler(wework_instance: ntwork.WeWork, message):
    #  回复一条消息
    reply_msg(
        wework_instance,
        message,
        rule=Rule.PRIVATE, # 仅私聊触发
        cmd='你好',
        reply='你好呀'
    )

```
## 项目结构

- 主程序入口：workbot.py

- 主要依赖：ntwork

- 插件目录：plugins

- 主包：wework_bot

## 如何开发插件？

在plugins文件夹下新建python包或新建单py文件即可在其中编写自己的插件

plugins文件夹下的插件都将在ntwork启动时自动导入

导入成功或失败均会输出日志。导入失败的原因是因为开发者编写插件时产生了语法错误，开发者可根据日志修复

## 后续我要做的&我目前无法实现的

接下来会完善整个插件开发的体验，逐步优化基本函数与方法，重写与优化控制台日志等

我目前做不到的：我无法对现有的ntwork的底层hook核心函数进行新增/修改/删除等操作（主要还是因为c语言苦手），我能做的是做一个在原有基础的东西之上进行一个封装，优化大家的开发体验

故issue中请不要再提此类问题，否则我将进行忽视

## 关于环境需要注意的事

1.ntwork只能运行在python3.10及其以下版本(具体使用哪个版本取决于ntwork下编译的二进制文件对应的python版本)，并不兼容python3.11及以上的python版本

2.原作者已将pipy上的包删除，所以用pip无法再安装ntwork

解决方法：在我的ntwork的fork分支项目的releases中有一个ntwork的备份包pkg，需要者自行下载导入