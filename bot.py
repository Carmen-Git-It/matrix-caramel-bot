import niobot
from niobot import ImageAttachment

import get_frogs
import config

client = niobot.NioBot(
    homeserver=config.HOMESERVER,
    user_id=config.USER_ID,
    command_prefix='!',
    case_insensitive=True,
    owner_id=config.OWNER_ID,
    ignore_self=True
)

@client.on_event("ready")
async def on_ready(sync_result: niobot.SyncResponse):
    print("Logged in!")

# Command
@client.command(name="frog")
async def frog(ctx: niobot.Context):
    print("command")
    attachment = await ImageAttachment.from_file(get_frogs.get_frog())
    await ctx.respond(file=attachment)

client.run(password=config.PASSWORD)