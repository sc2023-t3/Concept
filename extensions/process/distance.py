import re

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from classes.data import Distance
from classes.states import States
from extensions.process.rates import ask_rates


async def ask_distance(update: Update, _: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🩴 <200m", callback_data="distance(<200)")],
        [InlineKeyboardButton("👟 200 ~ 1000m", callback_data="distance(200-1000)")],
        [InlineKeyboardButton("🥾 >1000m", callback_data="distance(>1000m)")],
        [InlineKeyboardButton("我不知道 / 幫我決定😶", callback_data="distance(random)")]
    ]

    await update.message.reply_text(
        text="你想要跑超馬、半馬還是學校體適能💦？",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def receive_distance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> States:
    """
    Ask user how far they want to go.
    :param update: The update object from telegram.
    :param context: The context object from telegram.
    """
    distance = re.search(r"distance\((.*)\)", update.callback_query.data)

    context.chat_data.get("data").distance = Distance(distance.group(1))

    await ask_rates(update, context)
    return States.ASKING_RATES
