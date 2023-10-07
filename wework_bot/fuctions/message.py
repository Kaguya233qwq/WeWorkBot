# -*- coding: utf-8 -*-
import ntwork


class MsgInfo:
    """消息详情属性类"""

    def __init__(self, wework_instance: ntwork.WeWork, message):
        self.response_message = message
        self.data = message["data"]
        self.wework_instance = wework_instance

    '''获取消息内各个属性值的方法'''

    def get_sender_userid(self) -> str:
        """获取消息发送人的id"""
        return self.data["sender"]

    def get_sender_name(self) -> str:
        """获取消息发送人的账号名称"""
        return self.data["sender_name"]

    def get_my_id(self) -> str:
        """获取自己（bot）的id"""
        return self.wework_instance.get_login_info()["user_id"]

    def get_conversation_id(self) -> str:
        """获取会话id"""
        return self.data["conversation_id"]

    def get_msg_content(self) -> str:
        """获取消息内容"""
        msg_content = self.data["content"]
        return msg_content

    def get_msg_timestamp(self) -> str:
        """获取消息发送的时间戳"""
        return self.data["send_time"]

    def get_at_list(self) -> list:
        """获取消息内发送人@的成员列表"""
        return self.data["at_list"]

    '''消息来源'''

    def from_group(self) -> bool:
        """判断消息是否为群组消息，是返回True，不是返回False"""
        return True if "R:" in self.get_conversation_id() else False

    def from_private(self) -> bool:
        """判断消息是否为私聊消息，是返回True，不是返回False"""
        return True if "S:" in self.get_conversation_id() else False

    def at_me(self) -> bool:
        """判断消息内容中是否包含@自己，是返回True，不是返回False"""
        if self.get_at_list():
            for member in self.get_at_list():
                return True if self.get_my_id() in member["user_id"] else False   
        else:
            return False

    def not_me(self) -> bool:
        """判断发送消息的人是否不为自己，是返回True，不是返回False"""
        return True if self.get_sender_userid() != self.get_my_id() else False


class MsgRules(MsgInfo):
    """
    消息响应规则类
    GROUP ：只接收群组消息
    PRIVATE ：只接收私聊消息
    BOTH ：接收群组和私聊消息
    """

    def only_group(self) -> bool:
        """判断是否仅接收全部群组消息，是返回True，不是返回False"""
        return True if self.not_me() and not self.from_private() and self.from_group() else False

    def only_private(self) -> bool:
        """判断是否仅接收全部私聊消息，是返回True，不是返回False"""
        return True if self.not_me() and not self.from_group() and self.from_private() else False

    def both(self) -> bool:
        """判断是否接收全部群组消息与私聊消息，是返回True，不是返回False"""
        return True if self.not_me() else False

    def to_me(self) -> bool:
        """
        是否@bot
        """
        return True if self.only_group() and self.at_me() else False

    def from_userid(self, cmd: str) -> bool:
        """判断消息是否来源于指定发送人id，是返回True，不是返回False"""
        return True if cmd == self.get_sender_userid() else False

    def from_name(self, cmd: str) -> bool:
        """判断消息是否来源于指定发送人账号用户名，是返回True，不是返回False"""
        return True if cmd == self.get_sender_name() else False


class Cmd(MsgInfo):
    """自定义命令判定容器类"""

    def cmd_starts(self, cmd: str) -> bool:
        """判断消息内容是否以指定字符串开头，是返回True，不是返回False"""
        return True if self.get_msg_content().startswith(cmd) else False
    
    def cmd_ends(self, cmd: str) -> bool:
        """判断消息是否以指定字符串结尾，是返回True，不是返回False"""
        return True if self.get_msg_content().endswith(cmd) else False

    def cmd_contains(self, cmd: str) -> bool:
        """判断消息是否包含指定字符串，是返回True，不是返回False"""
        return True if cmd in self.get_msg_content() else False
