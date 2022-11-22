import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

print("hello world") 

TOKEN = open("token.txt", "r").readline()

players = {}

bot = commands.Bot(command_prefix= '.')

async def on_ready():
  print("Logged in as {0.user}".format(bot))

@bot.command(pass_context=True)
async def join(ctx):
  channel = ctx.message.author.voice.channel
  voice = await channel.connect()

@bot.command(pass_context=True)
async def leave(ctx):
  server = ctx.message.server
  voice_client = client.voice_client_in(server)
  await voice_client.disconnect()

@bot.command(brief="Plays a single video, from a youtube URL") #or bot.command()
async def play(ctx, url):
    voice = get(bot.voice_clients, guild=ctx.guild)
    YDL_OPTIONS = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.%(ext)s',
    }

    with YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.download(url)

    if not voice.is_playing():
        voice.play(FFmpegPCMAudio("song.mp3"))
        voice.is_playing()
        await ctx.send(f"Now playing {url}")
    else:
        await ctx.send("Already playing song")
        return

# @client.command(pass_context=True)
# async def play(ctx, url):
  
#   channel = ctx.message.author.voice.channel
#   if not channel:
#     await ctx.send("You are not connected to a voice channel")
#     return
#   voice = get(client.voice_clients, guild=ctx.guild)
#   if voice and voice.is_connected():
#     await voice.move_to(channel)
#   else:
#     voice = await channel.connect()
  
#   player = await voice.create_ytdl_player(url)
#   players[1] = player
#   player.start()

  # server = ctx.message.server
  # voice_client = client.voice_client_in(server)
  # player = await voice_client.create_ytdl_player(url)
  # players[server.id] = player
  # player.start()




bot.run(TOKEN)