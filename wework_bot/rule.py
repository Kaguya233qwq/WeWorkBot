from wework_bot.fuctions.message import MsgRules


class __BaseRule:
    ...


class Rule(__BaseRule):
    """
    消息响应规则类型选择器
    - GROUP: 仅限群组消息
    - PRIVATE: 仅限私聊消息
    - BOTH: 不限私聊群聊
    - TO_ME: 仅限at机器人的消息
    - SU: 仅超级用户
    """

    GROUP = 'group'
    PRIVATE = 'private'
    BOTH = 'both'
    TO_ME = 'to_me'
    SU = 'su'


def select_rule(
        wework_instance,
        message,
        rule: Rule
):
    rule_ = MsgRules(wework_instance, message)
    if rule == Rule.PRIVATE:
        return rule_.only_private()
    elif rule == Rule.GROUP:
        return rule_.only_group()
    elif rule == Rule.BOTH:
        return rule_.both()
    elif rule == Rule.TO_ME:
        return rule_.to_me()
    elif rule == Rule.SU:
        return rule_.is_su()
    else:
        raise TypeError('仅能为 class:Rule')
