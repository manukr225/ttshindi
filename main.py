import telebot

# 🔑 Your bot token
BOT_TOKEN = '7817191341:AAE8YEgvDv2r3Iz_HvdTIyJMAiI_llKB7sc'

# 📢 List of channels to post into
CHANNELS = ['@couple365', '@vmpaidcoursess']

bot = telebot.TeleBot(BOT_TOKEN)

# 🧠 Memory to avoid duplicate uploads
uploaded_files = {}

# Only use this caption
FIXED_CAPTION = "📝by Mr.X"

@bot.message_handler(content_types=['document', 'video', 'photo', 'audio', 'voice'])
def upload_file(message):
    bot.send_message(message.chat.id, "⏳ Processed your file...")

    try:
        file_id = ""

        # Detect file type
        if message.document:
            file_id = message.document.file_id
        elif message.video:
            file_id = message.video.file_id
        elif message.photo:
            file_id = message.photo[-1].file_id
        elif message.audio:
            file_id = message.audio.file_id
        elif message.voice:
            file_id = message.voice.file_id

        # Already uploaded?
        if file_id in uploaded_files:
            msg_id = uploaded_files[file_id]
            channel = uploaded_files[file_id + "_channel"]
            post_link = f"https://t.me/{channel[1:]}/{msg_id}"
            bot.send_message(message.chat.id, f"⚠️ Already uploaded.\n🔗 [Click to View]({post_link})", parse_mode='Markdown')
            return

        # Send to all channels
        for ch in CHANNELS:
            sent_msg = None
            if message.document:
                sent_msg = bot.send_document(ch, file_id, caption=FIXED_CAPTION)
            elif message.video:
                sent_msg = bot.send_video(ch, file_id, caption=FIXED_CAPTION)
            elif message.photo:
                sent_msg = bot.send_photo(ch, file_id, caption=FIXED_CAPTION)
            elif message.audio:
                sent_msg = bot.send_audio(ch, file_id, caption=FIXED_CAPTION)
            elif message.voice:
                sent_msg = bot.send_voice(ch, file_id, caption=FIXED_CAPTION)

            if sent_msg:
                uploaded_files[file_id] = sent_msg.message_id
                uploaded_files[file_id + "_channel"] = ch
                post_link = f"https://t.me/{ch[1:]}/{sent_msg.message_id}"
                bot.send_message(message.chat.id, f"✅ Posted to {ch}:\n🔗 [Click to View]({post_link})", parse_mode='Markdown')

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error:\n{e}", parse_mode='Markdown')

bot.polling()
