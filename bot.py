import os
# University Student Appeal Bot
# Python Telegram Bot: collects student appeals and forwards to admin

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! \n"\
        "Bu bot TDIU Samarqand filiali talabalarining murojaatlarini qabul qiladi.\n"\
        "Murojaatingizni oddiy xabar sifatida yozib yuboring."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    appeal_text = (
        "📩 YANGI MUROJAAT\n\n"
        f"👤 Talaba: {user.full_name}\n"
        f"🆔 Username: @{user.username}\n"
        f"📝 Murojaat:\n{text}"
    )

    # send to admin
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=appeal_text)

    # confirm to user
    await update.message.reply_text(
        "✅ Murojaatingiz qabul qilindi.\n"\
        "Adminlar tomonidan ko‘rib chiqiladi."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()
