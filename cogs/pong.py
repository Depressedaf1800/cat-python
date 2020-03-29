import discord
import time
from discord.ext import commands

class pong(commands.Cog):

    def __init__(self, cat):
        self.cat = cat

    @commands.command()
    async def pong(self, ctx):
        m = await ctx.send("...ponging 🏓")
        time.sleep(1)
        await m.edit(content = f"ping 🏓\nlatency is {round(self.cat.latency*1000)}")

def setup(cat):
    cat.add_cog(pong(cat))