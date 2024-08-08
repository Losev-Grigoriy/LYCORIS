import os
import disnake
from disnake.ext import commands
from config import TOKEN

intents = disnake.Intents.all()
intents.members = True
intents.voice_states = True
intents.guilds = True
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
    


bot.load_extension("cogs.profil")
bot.load_extension("cogs.eventtribun")
bot.load_extension("cogs.balance")
bot.load_extension("cogs.marry")
bot.load_extension("cogs.lovrum")
bot.load_extension("cogs.lprofil")





@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

bot.run(TOKEN)