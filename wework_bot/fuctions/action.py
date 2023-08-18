from typing import Any

import ntwork

from wework_bot.fuctions.message import MsgInfo, Cmd
from wework_bot.rule import Rule, select_rule

wework = ntwork.WeWork()
wework.open(smart=True)


class Action:

    @classmethod
    def reply_msg(
            cls,
            wework_instance: ntwork.WeWork,
            message,
            rule: Rule,
            cmd: str,
            reply: any
    ):
        """根据命令返回一条消息"""
        # 消息类实例化
        conversation = MsgInfo(
            wework_instance,
            message
        ).get_conversation_id()  # 实例化消息属性类并获取会话id

        cmd_param = Cmd(
            wework_instance,
            message
        ).cmd_starts(cmd)  # 实例化自定义命令类
        check = select_rule(
            wework_instance,
            message,
            rule=rule
        )
        if check and cmd_param:
            wework.send_text(
                conversation,
                str(reply)
            )  # 符合条件则向指定会话发送指定消息

    @classmethod
    def get_inner_contacts(cls):
        """
        获取联系人列表
        """
        return wework.get_inner_contacts()

    @classmethod
    def download_files_wx(
            cls,
            url: str,
            auth_key: str,
            size: int,
            save_path: Any
    ):
        """
        以wx方式下载文件
        """
        return wework.wx_cdn_download(
            url=url,
            auth_key=auth_key,
            size=size,
            save_path=save_path
        )

    @classmethod
    def download_files_c2c(
            cls,
            file_id: str,
            aes_key: str,
            file_size: int,
            file_type: int,
            save_path: str

    ):
        """
        以c2c方式下载文件
        """
        return wework.c2c_cdn_download(
            file_id=file_id,
            aes_key=aes_key,
            file_size=file_size,
            file_type=file_type,
            save_path=save_path
        )

    @classmethod
    def get_external_contacts(cls):
        """
        发送图片消息
        """
        wework.get_external_contacts()
