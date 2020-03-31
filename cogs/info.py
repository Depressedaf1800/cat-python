import discord
import time
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, cat):
        self.cat = cat

    @commands.command()
    async def ping(self, ctx):
        m = await ctx.send("...pinging 🏓")
        time.sleep(1)
        await m.edit(content = f"pong 🏓\nlatency is {round(self.cat.latency*1000)}")

def setup(cat):
    cat.add_cog(info(cat))
        