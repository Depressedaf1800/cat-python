import discord
import os
import time

cat = discord.Client()

@cat.event
async def on_ready():
    print('cat is meowing :3')

@cat.event
async def on_message(message):
    if message.author == cat.user:
        return

    if message.content.startswith('!ping'):
        m = await message.channel.send('pinging...')
        time.sleep(1)
        await m.edit(content = f'latency is {round(cat.latency*1000)}')


cat.run(os.environ['TOKEN'])