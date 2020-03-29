import discord
import time
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, cat):
        self.client = cat

    @commands.command()
    async def ping(self, ctx):
        m = await ctx.send('pinging...🏓')
        time.sleep(1)
        await m.edit(content = f'latency is {round(self.client.latency*1000)}')

def setup(cat):
    cat.add_cog(ping(cat)) 