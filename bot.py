import niobot
from niobot import ImageAttachment

import get_frogs
import config

client = niobot.NioBot(
    homeserver=config.HOMESERVER,
    user_id=config.USER_ID,
    command_prefix="!",
    case_insensitive=True,
    owner_id=config.OWNER_ID,
    ignore_self=True,
)


@client.on_event("ready")
async def on_ready(sync_result: niobot.SyncResponse):
    print("Logged in!")


@client.command(name="frog")
async def frog(ctx: niobot.Context):
    filename = await get_frogs.get_frog()
    attachment = await ImageAttachment.from_file(filename)
    await ctx.respond(file=attachment)


if __name__ == "__main__":
    client.run(password=config.PASSWORD)
