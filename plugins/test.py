import ntwork

from wework_bot.bot import bot
from wework_bot.fuctions.action import Action
from wework_bot.rule import Rule


@bot.msg_register(ntwork.MT_RECV_TEXT_MSG)
def msg_handler(_, message: dict):
    #  菜单命令
    menu = (
        " [玫瑰]欢迎使用[玫瑰]\n"
        " [玫瑰]今日问候[玫瑰]\n"
        " [玫瑰]客户服务[玫瑰]\n"
        " [玫瑰]数据查询[玫瑰]\n"
        " [玫瑰]发送日报[玫瑰]\n"
        " [玫瑰]其他功能[玫瑰]"
    )
    Action.reply_text_msg(message, rule=Rule.PRIVATE, cmd="/菜单", reply=menu)
