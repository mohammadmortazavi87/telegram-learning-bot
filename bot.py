from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get('7288787349:AAG9CF10XVZHJ0V7aKUnOnIwy7mrnmIp1DM')

memory = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام! من یک ربات ساده هستم. باهام حرف بزن!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    memory.append(user_message)
    
    if "سلام" in user_message:
        response = "سلام دوست من!"
    elif "خداحافظ" in user_message:
        response = "فعلا دوست من!"
    else:
        response = "حرف جالبی زدی! ادامه بده..."

    await update.message.reply_text(response)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("ربات روشن است...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
