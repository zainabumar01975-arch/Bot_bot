from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = 7929296544

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Start"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "This bot explains how to access rewards and what to do.\n\n"
        "Tap START below to continue.",
        reply_markup=reply_markup
    )

# BUTTON / TEXT HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Start":
        await update.message.reply_text(
            "🤔 Were you referred by someone?\n"
            "You can continue either way."
        )

        await update.message.reply_text(
            "📌 STEP 1:\n"
            "Download the Cardcosmic app and use this invitation code:\n\n"
            "👉 JSEXD8\n\n"
            "Follow the signup instructions in the app."
        )

        await update.message.reply_text(
            "📌 STEP 2:\n"
            "Send a screenshot of your dashboard here after signup."
        )
    else:
        await update.message.reply_text("Tap START to begin.")

# HANDLE SCREENSHOT
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]

    # Send to you
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo.file_id,
        caption=f"New user submission from @{update.message.from_user.username}"
    )

    await update.message.reply_text(
        "✅ Screenshot received!\n\n"
        "Next step:\n"
        "Share this bot with friends to continue."
    )

# BUILD BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

app.run_polling()
