from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, Application, CallbackQueryHandler


async def send_results(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    Send the results to the user.
    :param update: The update object from telegram.
    :param _: The context object from telegram.
    """
    query = update.callback_query

    await query.answer()

    keyboard = [
        [InlineKeyboardButton(
            "🗾 Google Map",
            url="https://www.google.com.tw/maps/place/%E5%9C%8B%E7%AB%8B%E9%99%BD%E6%98%8E%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%B8%E7%AC%AC%E4%BA%8C%E9%A4%90%E5%BB%B3/@24.7879049,120.9975688,17.63z/data=!3m1!5s0x3468360e62bbab7b:0x4cf3e94af2597f85!4m6!3m5!1s0x34683611dcf63a29:0xc53353416c0f7c1e!8m2!3d24.789302!4d120.997197!16s%2Fg%2F1pzwsht95?hl=zh-TW&entry=ttu"
        )],
        [InlineKeyboardButton("🔁 再來一次", callback_data="to_length")]
    ]

    await query.edit_message_text(
        text="🍽️ 這是你的結果！\n\n"
             "📍 店名：國立陽明交通大學第二餐廳\n"
             "🏷️ 類型：中式\n"
             "💰 價位：$ (100~200元)\n"
             "🚶 距離：1.2km",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def setup(application: Application):
    application.add_handler(CallbackQueryHandler(send_results, pattern="to_result"))
