#imports
import discord
import os
import time
import dotenv

#extensions
from dotenv import load_dotenv
from discord.ext import commands

#load .env
load_dotenv()

#define bot
cat = commands.Bot(command_prefix = "!", case_insensitive = True)

#when bot is online
@cat.event
async def on_ready():
    print("cat is meowing :3")

    for cog in [file.split(".")[0] for file in os.listdir('cogs') if file.endswith(".py")]:
        try:
            if cog != "__init__":
                cat.load_extension(f"cogs.{cog}")
                print(f"{cog} loaded")
        except Exception as e:
            print(e)
    
@cat.event
async def on_message(message):
    print(f'{message.author.display_name} said {message.content} in {message.channel}')
    if message.author == cat.user:
        return
    if message.content.lower() == "hi":
        await message.channel.send(f"hi {message.author.mention} :3")
    await cat.process_commands(message)

cat.run(os.environ['TOKEN'])