from wework_bot.fuctions.message import Message


class __BaseRule: ...


class Rule(__BaseRule):
    """
    消息响应规则类型选择器
    - GROUP: 仅限群组消息
    - PRIVATE: 仅限私聊消息
    - BOTH: 不限私聊群聊
    - TO_ME: 仅限at机器人的消息
    - SU: 仅超级用户
    """

    GROUP = "group"
    PRIVATE = "private"
    BOTH = "both"
    TO_ME = "to_me"
    SU = "su"


def rule_checker(message: Message, rule: Rule):
    if rule == Rule.PRIVATE:
        return message.from_private()
    elif rule == Rule.GROUP:
        return message.from_group()
    elif rule == Rule.BOTH:
        return message.sender_not_me()
    elif rule == Rule.TO_ME:
        return message.from_private() or message.at_me()
    elif rule == Rule.SU:
        return message.is_su()
    else:
        raise TypeError("仅能为 class:Rule")
