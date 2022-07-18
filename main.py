import discord
from discord.ext import commands
import os

TOKEN = 'OTk4NjA0MDUzMzkzMTk5MTc1.Gc0QZG.CJCC5jLCErAaVn9mn8RZmpVgj4QvEwrKNYBZC0'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix="?")

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))



bot.run(os.getenv("TOKEN"))

