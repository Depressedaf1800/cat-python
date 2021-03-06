import discord
import youtube_dl
import os

from discord.ext import commands
from discord.utils import get

class voice(commands.Cog):

    def __init__(self, cat):
        self.cat = cat

    '''if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus.so')'''

    @commands.command(name = "join", aliases = ["j"], help = "joins a voice channel")
    async def join(self, ctx):
        global voice
        channel = ctx.author.voice.channel
        voice = get(self.cat.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await voice.disconnect()

        await ctx.send("meow 🎶 :3")

    @commands.command(name = "leave", aliases = ["disconnect", "l", "dc"], help = "leaves voice channel")
    async def leave(self, ctx):
        voice = get(self.cat.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"cat disconnected")
        else:
            await ctx.send("meow :3")

    @commands.command(name = "play", help = "play a youtube url as mp3")
    async def play(self, ctx, url: str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            await ctx.send("music is currently playing")
            return
        m = await ctx.send("...searching 🔍")

        channel = ctx.author.voice.channel
        voice = get(self.cat.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

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

    @commands.command(name = "pause", help = "pause music")
    async def pause(self, ctx):
        voice = get(self.cat.voice_clients, guild = ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            await ctx.send("paused")
        else:
            await ctx.send("no music running")
    
    @commands.command(name = "resume", help = "resume music")
    async def resume(self, ctx):
        voice = get(self.cat.voice_clients, guild = ctx.guild)
        
        if voice and voice.is_paused():
            voice.resume()
            await ctx.send("music resumed")
        else:
            print("no music paused")
            await ctx.send("no music paused")

    @commands.command(name = "stop", help = "stops playing")
    async def stop(self, ctx):
        voice = get(self.cat.voice_clients, guild = ctx.guild)

        if voice and (voice.is_playing() or voice.is_paused()):
            voice.stop()
            await ctx.send("music stopped")
        else:
            await ctx.send("no music running")

def setup(cat):
    cat.add_cog(voice(cat))