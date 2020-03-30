import discord
import youtube_dl
import os
import random

from discord.ext import commands
from discord.utils import get

class smoke(commands.Cog):

    def __init__(self, cat):
        self.cat = cat

    if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus.so')

    @commands.command()
    async def smoke(self, ctx):
        global voice
        urllist = ('https://youtu.be/clU8c2fpk2sg','https://www.youtube.com/watch?v=HQKneQaM-KI',
        'https://www.youtube.com/watch?v=QE4v30t-kY4','https://youtu.be/X3MYWwS-Zrg')
        url = random.choice(urllist)
        channel = ctx.author.voice.channel
        voice = get(self.cat.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"joined {channel}")

        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            await ctx.send("music is currently playing")
            return
        m = await ctx.send("...searching 🔍")

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',   
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading audio")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e:print(f"{name} finished playing"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

        nname = name.rsplit("-", 2)
        await m.delete()
        await ctx.send(f"playing **{nname[0]}**")

def setup(cat):
    cat.add_cog(smoke(cat))