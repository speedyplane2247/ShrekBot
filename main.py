#ShrekBot for Discord 0.1
#By @AlexApps#9295

import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')

@bot.event
async def on_ready():
	print('ShrekBot 0.1')
	print('')
	print('Logged in as:')
	print(bot.user.name)
	print('')
	print('Client User ID:')
	print(bot.user.id)
	print('')
	await bot.change_presence(game=discord.Game(name='Shrek on BluRay'))

@bot.command()
async def help():
	await bot.say('__**ShrekBot 0.1 Commands:**__\n\n```css\n/help      : Shows help for commands\n/kill      : Kill minecraft avatars\n/clear     : Wipes the chat clean\n/choose    : Picks randomly between multiple choices\n/something : Random Stuff\n/zouss     : Zouss City\n/echo      : Echoes whatever you say```\n```\nIf you want to suggest more commands, visit the creator at:\nhttps://discord.gg/2anYtuD```')

@bot.command()
async def kill(*, mentioned = 'You'):
	await bot.say((mentioned) + ' fell out of the world')

@bot.command()
async def clear():
	await bot.say('ﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\n')

@bot.command()
async def choose(*choices : str):
	await bot.say((random.choice(choices)) + ', I choose you!')

@bot.command()
async def something():
	somethings = ['Somebody once told me the world was gonna roll me.\nI ain\'t the sharpest tool in the shed.', 'WHAT ARE YOU DOING IN MY SWAMP?!', 'Shrek is love, Shrek is life.']
	await bot.say(random.choice(somethings))
	
@bot.command()
async def zouss():
	await bot.say('ζ ο υ ς ς    Ͼ ι τ ψ !')
	
@bot.command()
async def ζουςς():
	await bot.say('ζ ο υ ς ς    Ͼ ι τ ψ !')

@bot.command()
async def echo(*, message: str):
    await bot.say(message)

bot.run(os.environ['TOKEN_DISCORD'])
