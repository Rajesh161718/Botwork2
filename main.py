import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from scraper import extract_links, scrape_product_data
from scheduler import start_scheduler

BOT_TOKEN = "7032227791:AAFLRnENB63xvffatdO9fsSNi77-VsGtkPw"  # Your real bot token here!

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("👋 Send me your affiliate product links or a .txt file.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        logger.warning("Empty or no text message received.")
        return

    links = extract_links(update.message.text)
    if not links:
        await update.message.reply_text("⚠️ No valid links found.")
        return

    for link in links:
        await update.message.reply_text(f"🔗 Received link: {link}")
        product_info = scrape_product_data(link)
        await update.message.reply_text(product_info)

def main():
    print("🚀 Bot is starting...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    start_scheduler()  # start your scheduled jobs if any

    app.run_polling()

if __name__ == "__main__":
    main()
