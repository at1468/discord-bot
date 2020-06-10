import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

random.seed()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='wholesome')
async def wholesome(ctx):
    wholesomeLevel = random.randint(0, 100)

    if wholesomeLevel < 100:
        await ctx.send(ctx.author.mention + ' is wholesome ' + str(wholesomeLevel))
    else:
        await ctx.send(file=discord.File('media/wholesome100.jpg'))



bot.run(TOKEN)
