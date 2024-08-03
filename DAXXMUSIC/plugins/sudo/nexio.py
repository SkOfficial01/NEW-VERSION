import requests
import random
from DAXXMUSIC import app, userbot
from DAXXMUSIC.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from DAXXMUSIC.utils.daxx_ban import admin_filter






Yumikoo_text = [
"hey please don't disturb me.",
"who are you",    
"aap kon ho",
"aap mere owner to nhi lgte ",
"hey tum mera name kyu le rhe ho meko sone do",
"ha bolo kya kaam hai ",
"dekho abhi mai busy hu ",
"hey i am busy",
"aapko smj nhi aata kya ",
"leave me alone",
"dude what happend",    
]

strict_txt = [
"i can't restrict against my besties",
"are you serious i am not restrict to my friends",
"fuck you bsdk k mai apne dosto ko kyu kru",
"hey stupid admin ", 
"ha ye phele krlo maar lo ek dusre ki gwaand",  
"i can't hi is my closest friend",
"i love him please don't restict this user try to usertand "
]


 
ban = ["ban","boom"]
unban = ["unban",]
mute = ["mute","silent","shut"]
unmute = ["unmute","speak","free"]
kick = ["kick", "out","nikaal","nikal"]
promote = ["promote","adminship"]
fullpromote = ["fullpromote","fulladmin"]
demote = ["demote","lelo"]
group = ["group"]
channel = ["channel"]



# ========================================= #


@app.on_message(filters.command(["anki","umit"], prefixes=["S", "S"]) & admin_filter)
async def restriction_app(app :app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Yumikoo_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")
    
    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("Oᴋʏ, sᴜᴍɪᴛ Jɪ ᴍᴇʀᴇ ᴏᴡɴᴇʀ ᴋᴇ ᴋᴇʜɴᴇ ᴘʀ ᴍᴇ ɪs ᴍᴜʀᴋʜ sᴀᴋsʜ ᴋᴏ ʙᴀɴ ᴋʀ ʀʜɪ ʜᴜ💀")
                    
        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"Oᴋʏ, sᴜᴍɪᴛ Jɪ ᴍᴇʀᴇ ᴏᴡɴᴇʀ ᴋᴇ ᴋᴇʜɴᴇ ᴘʀ ᴍᴇ ɪs ᴍᴜʀᴀᴋʜ sᴀᴋsʜ ᴋᴏ ᴅᴜʙᴀʀᴀ ɢʀᴏᴜᴘ ᴍᴇ ᴀɴᴇ ᴋᴇ ʟɪʏᴇ ᴜɴʙᴀɴ ᴋʀ ʀʜɪ ʜᴜ💀") 
                
        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("🤡Is Jᴏᴋᴇʀ ᴋᴏ ᴏᴡɴᴇʀ ᴋᴇ ᴋᴇʜɴᴇ ᴘʀ ʙʜɢᴀ ᴅɪʏᴀ Mᴇɴᴇ💀") 
                    
        for muted in data:
            print(f"present {muted}") 
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"😏Bs ᴋʀ ᴋɪᴛɴᴀ ᴋ ʙᴏʟᴛᴇ ʜᴏ ᴄʜᴜᴘ ʜᴏ Jᴀᴏ🤫") 
                    
        for unmuted in data:
            print(f"present {unmuted}")            
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"🤨ᴅᴜʙᴀʀᴀ ᴍᴏᴋᴀ ᴅᴇ ʀʜɪ ʜᴜ ʙᴏʟɴᴇ ᴋᴀ ɢʟᴛ ʙᴏʟᴀ ᴛᴏ ғɪʀsᴇ ᴜɴᴍᴜᴛᴇ ʜᴏ Jᴀᴏɢᴇ ᴛᴜᴍ🤨")   


        for promoted in data:
            print(f"present {promoted}")            
            if promoted in promote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
                await message.reply("🙈Aʏᴇᴇ ʜᴀʏᴇᴇ sɪʀ ᴋᴇ ᴋᴇʜɴᴇ ᴘʀ ᴍᴇ ᴛᴜᴍʜᴇ ᴘʀᴏᴍᴏᴛᴇ ᴋʀ ᴅᴇ ʀʜɪ ʜᴜ😁")

        for demoted in data:
            print(f"present {demoted}")            
            if demoted in demote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                       )
                     )
                await message.reply("😏Jᴀ ᴀʙsᴇ ᴛᴜ ᴀᴅᴍɪɴ ɴᴀʜɪ")


#async def your_function():
    for fullpromoted in data:
        print(f"present {fullpromoted}")            
        if fullpromoted in fullpromote:
            await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
               )
             )
            await message.reply("🙈Hʏᴇᴇ ᴍᴇ sᴀᴅᴋᴇ Jᴀᴠᴀ sɪʀ Jɪ ᴋɪs ᴋʜᴀᴀs sᴀᴋsʜ ᴋᴏ ғᴜʟʟ ᴘᴏʀᴍᴏᴛᴇ ᴋʀɴᴇ ᴋᴏ ʙᴏʟ ʀʜᴇ🙈😁ʟᴏ ᴋʀ ᴅɪʏᴀ ғᴜʟʟ ᴘʀᴏᴍᴏᴛᴇ sɪʀ ᴋᴇ ᴋᴇʜɴᴇ ᴘʀ🙈")
