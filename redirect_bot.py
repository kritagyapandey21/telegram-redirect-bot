import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_BOT_USERNAME = os.getenv("TARGET_BOT_USERNAME")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command and redirect to target bot."""
    user = update.effective_user
    
    # Create inline keyboard with prominent redirect button
    keyboard = [
        [InlineKeyboardButton("✅ Continue →", url=f"https://t.me/{TARGET_BOT_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send redirect message
    await update.message.reply_text(
        "🔄 Redirecting...",
        reply_markup=reply_markup
    )
    
    logger.info(f"User {user.id} ({user.username}) was redirected to {TARGET_BOT_USERNAME}")

async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle any message and redirect to target bot."""
    user = update.effective_user
    
    # Create inline keyboard with prominent redirect button
    keyboard = [
        [InlineKeyboardButton("✅ Continue →", url=f"https://t.me/{TARGET_BOT_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send redirect message
    await update.message.reply_text(
        "🔄 Redirecting...",
        reply_markup=reply_markup
    )
    
    logger.info(f"User {user.id} ({user.username}) sent a message and was redirected")

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_any_message))

    # Start the bot
    logger.info("Bot is starting...")
    
    # Use run_polling with drop_pending_updates to avoid issues on hosting
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )

if __name__ == '__main__':
    main()
