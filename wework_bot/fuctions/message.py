# -*- coding: utf-8 -*-
from wework_bot.bot import bot

from .config import Config


class Message:
    """基础消息类"""

    def __init__(self, message: dict):

        self.sender_id: str = message["data"]["sender"]
        """发送人id"""

        self.sender_name: str = message["data"]["sender_name"]
        """发送人账号名称"""

        self.self_id: str = bot.get_login_info()["user_id"]
        """机器人id"""

        self.conversation_id: str = message["data"]["conversation_id"]
        """消息会话id"""

        self.contents: str = message["data"]["content"]
        """消息内容"""

        self.send_time = message["data"]["send_time"]
        """发送时间"""

        self.at_list: list = message["data"]["at_list"]
        """@成员列表"""

    def sender_not_me(self) -> bool:
        """判断发送消息的人是否不为自己(所有的他人消息)，是返回True，不是返回False"""
        return self.sender_id != self.self_id

    def from_group(self) -> bool:
        """判断消息是否为群组消息，是返回True，不是返回False"""
        return "R:" in self.conversation_id and self.sender_not_me()

    def from_private(self) -> bool:
        """判断消息是否为私聊消息，是返回True，不是返回False"""
        return "S:" in self.conversation_id and self.sender_not_me()

    def at_me(self) -> bool:
        """判断消息内容中是否包含@自己，是返回True，不是返回False"""
        for member in self.at_list:
            if self.self_id in member["user_id"]:
                return True
        return False

    def starts_with(self, content: str) -> bool:
        """判断消息内容是否以指定内容开头，是返回True，不是返回False"""
        return self.contents.startswith(content)

    def ends_with(self, content: str) -> bool:
        """判断消息是否以指定内容结尾，是返回True，不是返回False"""
        return self.contents.endswith(content)

    def contains(self, content: str) -> bool:
        """判断消息是否包含指定内容，是返回True，不是返回False"""
        return content in self.contents

    def from_user_id(self, user_id: str) -> bool:
        """判断消息是否来源于指定发送人id，是返回True，不是返回False"""
        return user_id == self.sender_id

    def from_user_name(self, user_name: str) -> bool:
        """判断消息是否来源于指定发送人账号用户名，是返回True，不是返回False"""
        return user_name == self.sender_name

    def is_su(self) -> bool:
        """判断消息是否来源于超级用户"""
        return self.sender_id in Config.SUPER_USERS