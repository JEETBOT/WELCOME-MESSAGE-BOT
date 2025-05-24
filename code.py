import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Apne Bot ka Token yahan daalein (BotFather se milega)
BOT_TOKEN = "7828409161:AAHz_dbVSe6PldckzlZ-GG6hPlCakR4yeV8"

# Aapke Group ka naam jo message mein dikhana hai
GROUP_NAME_DISPLAY = "JEET" # Ise apni group ke naam se badal lein

# Aapke Social Media Links
INSTAGRAM_LINK = "https://www.instagram.com/meihunjeet?igsh=MTF5azlsenkwbnU5OQ"
YOUTUBE_LINK = "https://youtube.com/@jitjourney"
WHATSAPP_LINK = "https://whatsapp.com/channel/0029Va4OGHNJuyAECPWkE60i" # ya aapka WhatsApp group link

# Logging setup (optional, but good for debugging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Jab naya member group join kare toh yeh function call hoga."""
    if update.message and update.message.new_chat_members:
        for member in update.message.new_chat_members:
            # Member ka username ya first name (agar username na ho)
            if member.username:
                member_display_name = f"@{member.username}"
            else:
                member_display_name = member.first_name

            welcome_message = f"Hi {member_display_name}, WELCOME TO CHANNEL {GROUP_NAME_DISPLAY}!"

            # Inline Buttons banana
            keyboard = [
                [InlineKeyboardButton("✅ Instagram✅", url=INSTAGRAM_LINK)],
                [InlineKeyboardButton("✅YouTube✅", url=YOUTUBE_LINK)],
                [InlineKeyboardButton("💬 ✅WhatsApp✅", url=WHATSAPP_LINK)],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Welcome message send karna
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=welcome_message,
                reply_markup=reply_markup
            )
            logger.info(f"Sent welcome message to {member_display_name} in chat {update.effective_chat.id}")

def main() -> None:
    """Bot ko start karta hai."""
    # Application banane ke liye
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handler for new members
    # filters.StatusUpdate.NEW_CHAT_MEMBERS se naye members detect hote hain
    new_member_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member)
    application.add_handler(new_member_handler)

    logger.info("Bot started...")
    # Bot ko run karna shuru karega
    application.run_polling()

if __name__ == '__main__':
    main()