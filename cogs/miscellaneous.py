import discord
import time
from discord.ext import commands

class miscellaneous(commands.Cog):

    def __init__(self, cat):
        self.cat = cat

    @commands.command()
    async def pong(self, ctx):
        m = await ctx.send("...ponging 🏓")
        time.sleep(1)
        await m.edit(content = f"ping 🏓\nlatency is {round(self.cat.latency*1000)}")

    @commands.command(aliases = ["broadcast", "bc"])
    async def say(self, ctx, *args):
        if len(args) != 0:
            await ctx.message.delete()
            await ctx.send(" ".join(args))
        else:
            await ctx.message.delete()
            await ctx.send("meow :3")

def setup(cat):
    cat.add_cog(miscellaneous(cat))