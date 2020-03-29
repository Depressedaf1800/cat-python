import discord
from discord.ext import commands

class say(commands.Cog):

    def __init__(self, cat):
        self.cat = cat

    @commands.command(aliases = ["broadcast", "bc"])
    async def say(self, ctx, *args):
        if len(args) != 0:
            await ctx.message.delete()
            await ctx.send(" ".join(args))
        else:
            await ctx.message.delete()
            await ctx.send("meow :3")
            

def setup(cat):
    cat.add_cog(say(cat))