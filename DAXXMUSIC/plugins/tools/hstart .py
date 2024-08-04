from pyrogram import Client, filters

@Client.on_message(filters.command(["hstart", "hhelp"]))
async def start_comm(c, m):
    await m.reply_text("Mᴜsɪᴄ ʙᴏᴛ ɪs ᴡᴏʀᴋɪɴɢ ᴅᴜᴅᴇ")
