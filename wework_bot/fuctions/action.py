from typing import Any

from wework_bot.bot import bot
from wework_bot.fuctions.message import Message
from wework_bot.rule import Rule, rule_checker


class Action:

    @classmethod
    def reply_text_msg(cls, message: dict, rule: Rule, cmd: str, reply: str):
        """根据命令返回一条消息"""
        msg_instance = Message(message)
        checker = rule_checker(msg_instance, rule)
        if checker and msg_instance.starts_with(cmd):
            bot.send_text(
                msg_instance.conversation_id, reply
            )  # 符合条件则向指定会话发送指定消息

    @classmethod
    def get_inner_contacts(cls):
        """
        获取联系人列表
        """
        return bot.get_inner_contacts()

    @classmethod
    def download_files_wx(cls, url: str, auth_key: str, size: int, save_path: Any):
        """
        以wx方式下载文件
        """
        return bot.wx_cdn_download(
            url=url, auth_key=auth_key, size=size, save_path=save_path
        )

    @classmethod
    def download_files_c2c(
        cls, file_id: str, aes_key: str, file_size: int, file_type: int, save_path: str
    ):
        """
        以c2c方式下载文件
        """
        return bot.c2c_cdn_download(
            file_id=file_id,
            aes_key=aes_key,
            file_size=file_size,
            file_type=file_type,
            save_path=save_path,
        )

    @classmethod
    def get_external_contacts(cls):
        """
        获取外部联系人列表
        """
        bot.get_external_contacts()
