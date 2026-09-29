from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8896502448:AAHy3dlBbHIUusxM5sZgtJNSNQ317cVgdyo"
MY_CHAT_ID = 6628347596

async def send_message(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    await context.bot.send_message(chat_id=job.chat_id, text="عمر منيك")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    for job in current_jobs:
        job.schedule_removal()

    # التكرار كل 60 ثانية (دقيقة واحدة)
    context.job_queue.run_repeating(send_message, interval=60, first=5, chat_id=chat_id, name=str(chat_id))
    
    await update.message.reply_text("تم التفعيل! سيرسل البوت الرسالة كل دقيقة.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("البوت يعمل الآن...")
    app.run_polling()
