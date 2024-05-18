from pyrogram import Client, filters
from pytgcalls import GroupCallFactory

app = Client('pytgcalls')
group_call = GroupCallFactory(app).get_file_group_call('input.raw')

@group_call.on_network_status_changed
async def on_network_changed(_, is_connected):
    if is_connected:
        await _.send_message(_.chat.id, 'Successfully joined!')
    else:
        await _.send_message(_.chat.id, 'Disconnected from voice chat..')

@app.on_message(filters.command('join') & filters.me)
async def join_handler(_, message):
    await group_call.start(message.chat.id)

@app.on_message(filters.command("start") & filters.me)
async def start_music(_, message):
    if _.chat.id in group_call.instances.active_chats:
        queues.put(_.chat.id, 'out.raw')
    else:
        await group_call_instances.set_stream(_.chat.id, 'out.raw')

@app.on_message(filters.command("end") & filters.me)
async def end_music(_, message):
    await group_call_instances.stop(_.chat.id)

app.run()
