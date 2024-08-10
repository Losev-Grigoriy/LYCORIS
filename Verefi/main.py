import os
import disnake
from disnake.ext import commands
from config import TOKEN

intents = disnake.Intents.all()
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    

bot.load_extension("cogs.veref")
bot.load_extension("cogs.staffveref")
bot.load_extension("cogs.adminveref")
bot.load_extension("cogs.staff")
bot.load_extension("cogs.mute")
bot.load_extension("cogs.ban")
bot.load_extension("cogs.kik")
bot.load_extension("cogs.warn")


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')


bot.run(TOKEN)