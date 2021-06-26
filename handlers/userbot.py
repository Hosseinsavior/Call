# Copyright (c) @Bruh_0x (Itz-fork)
# Plugin To Handle Your Streamer Account

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message

from config import BOT_USERNAME, BOT_OWNER
from callsmusic.callsmusic import client as NEXAUB

# To Block a PM'ed User
@NEXAUB.on_message(filters.private & filters.command("block", [".", "/"]) & filters.me & ~filters.edited)
async def ubblock(_, message: Message):
  shit_id = message.chat.id
  gonna_block_u = await message.edit_text("`Blocking User...`")
  try:
    await NEXAUB.block_user(shit_id)
    await gonna_block_u.edit("`Successfully Blocked This User`")
  except Exception as lol:
    await gonna_block_u.edit(f"`Can't Block This Guy! May be this is durov?` \n\n**Error:** `{lol}`")


# To Unblock User That Already Blocked
@NEXAUB.on_message(filters.command("unblock", [".", "/"]) & filters.me & ~filters.edited)
async def ubblock(_, message: Message):
  good_bro = int(message.command[1])
  gonna_unblock_u = await message.edit_text("`Unblocking User...`")
  try:
    await NEXAUB.unblock_user(good_bro)
    await gonna_unblock_u.edit(f"`Successfully Unblocked The User` \n**User ID:** `{good_bro}`")
  except Exception as lol:
    await gonna_unblock_u.edit(f"`Can't Unblock That Guy!, I think he is still dumb!` \n\n**Error:** `{lol}`")


# To Get How Many Chats that you are in (PM's also counted)
@NEXAUB.on_message(filters.private & filters.command("chats", [".", "/"]) & filters.me & ~filters.edited)
async def ubgetchats(_, message: Message):
  getting_chats = await message.edit_text("`Checking Your Chats, Hang On...`")
  async for dialog in NEXAUB.iter_dialogs():
    try:
      total = await NEXAUB.get_dialogs_count()
      await getting_chats.edit(f"**Total Dialogs Counted:** `{total}` \n\n**Not Stable Lol**")
    except Exception as lol:
      await getting_chats.edit(f"`Never Gonna Give You Up!` \n\n**Error:** `{lol}`")


# Leave From a Chat
@NEXAUB.on_message(filters.private & filters.command("kickme", [".", "/"]) & filters.me & ~filters.edited)
async def ubkickme(_, message: Message):
  i_go_away = await message.edit_text("`Leaving This Chat...`")
  try:
    await NEXAUB.leave_chat()
    await i_go_away.edit("`Successfully Leaved This Chat!`")
  except Exception as lol:
    await i_go_away.edit(f"`Can't Leave This Chat!, What a cruel world!` \n\n**Error:** `{lol}`")


# Alive Message
@NEXAUB.on_message(filters.command("alive", [".", "/"]) & filters.me & ~filters.edited)
async def ubalive(_, message: Message):
  await message.edit_text(f"**🌀 Nexa Music Userbot is Alive 🌀** \n\n**🤖 Bot Version:** `V2.9.1` \n\n**🐬 Info**\n ↳**Music Bot:** {BOT_USERNAME} \n ↳**Owner:** [Click Here](tg://user?id={BOT_OWNER})")