from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace this with your real token

# Define a command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot.")

# Main function to run the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
