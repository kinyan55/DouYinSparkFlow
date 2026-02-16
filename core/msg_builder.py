"""
core/msg_builder.py
解析消息模板构建具体发送的消息内容
"""

from utils.config import get_config
from utils.hitokoto import request_hitokoto
from datetime import date

def build_message() -> str:
    today = date.today()
    if get_config().get("happyNewYear", {}).get("enabled", False) and date(2026, 2, 16) <= today <= date(2026, 3, 3):
        from utils.chinese_new_year_2026_mare import get_random_festival_quote, get_lunar_date
        message = get_config().get("happyNewYear", {}).get("messageTemplate", "[API]")
        if "[data]" in message:
            message = message.replace("[data]", today.strftime("%Y年%m月%d日"))
        if "[data_lunar]" in message:
            lunar_date = get_lunar_date(today)
            message = message.replace("[data_lunar]", lunar_date if lunar_date else "未知农历日期")
        if "[API]" in message:
            api_content = get_random_festival_quote()
            message = message.replace("[API]", api_content)
    else:
        message = get_config().get("messageTemplate", "续火花")
        if "[API]" in message:
            api_content = request_hitokoto()
            message = message.replace("[API]", api_content)
    return message.strip()