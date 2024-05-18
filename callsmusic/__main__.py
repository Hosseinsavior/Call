from pyrogram import filters
from pyrogram import Client
from pytgcalls import GroupCallFactory

client = Client('pytgcalls')

group_call_factory = GroupCallFactory(client)
group_call = group_call_factory.get_file_group_call('input.raw')

@group_call.on_network_status_changed
async def on_network_changed(group_call, is_connected):
    chat_id = MAX_CHANNEL_ID - group_call.full_chat.id
    if is_connected:
        await client.send_message(chat_id, 'Successfully joined!')
    else:
        await client.send_message(chat_id, 'Disconnected from voice chat..')

@client.on_message(filters.outgoing & filters.command('join'))
async def join_handler(client, message):
    await group_call.start(message.chat.id)

@client.on_message(filters.me & filters.command("start"))
async def start_stream(client, message):
    if message.chat.id in group_call_instances.active_chats:
        queues.put(message.chat.id, 'out.raw')
    else:
        await group_call_instances.set_stream(message.chat.id, 'out.raw')

@client.on_message(filters.me & filters.command("end"))
async def end_stream(client, message):
    await group_call_instances.stop(message.chat.id)

client.run()
