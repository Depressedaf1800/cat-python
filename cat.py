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
cat = commands.Bot(command_prefix = "!")

#when bot is online
@cat.event
async def on_ready():
    print('cat is meowing :3')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cat.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename[:-3]} loaded')

@cat.event
async def on_message(message):
    print(f'{message.author.display_name} said {message.content} in {message.channel}')
    if message.author == cat.user:
        return

cat.run(os.environ['TOKEN'])