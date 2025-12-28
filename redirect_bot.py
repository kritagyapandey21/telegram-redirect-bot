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
    """Handle the /start command with informative content before redirect."""
    user = update.effective_user
    
    # Create inline keyboard with redirect button
    keyboard = [
        [InlineKeyboardButton("Start Your AI Session", url=f"https://t.me/{TARGET_BOT_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send informative welcome message
    welcome_message = (
        "Welcome to Tanix AI\n\n"
        "Tanix AI is your 24/7 intelligent assistant powered by advanced artificial intelligence.\n\n"
        "Our Features:\n"
        "- Natural language conversations\n"
        "- Instant responses to your questions\n"
        "- Available around the clock\n"
        "- Personalized assistance\n"
        "- Multi-topic expertise\n\n"
        "Ready to experience intelligent conversations?\n"
        "Click the button below to start your session."
    )
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup
    )
    
    logger.info(f"User {user.id} ({user.username}) was shown info and redirect to {TARGET_BOT_USERNAME}")

async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle any message with helpful redirect to active bot."""
    user = update.effective_user
    
    # Create inline keyboard with redirect button
    keyboard = [
        [InlineKeyboardButton("Start Your AI Session", url=f"https://t.me/{TARGET_BOT_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send helpful message
    response_message = (
        "Thank you for your message.\n\n"
        "To start using Tanix AI and get responses to your questions, "
        "please click the button below to begin your session with our main AI assistant."
    )
    
    await update.message.reply_text(
        response_message,
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
    
