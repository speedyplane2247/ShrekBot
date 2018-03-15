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
	await bot.say('__**ShrekBot 0.1 Commands:**__\n\n```css\n/help      : Shows help for commands\n/kill      : Kill minecraft avatars\n/clear     : Wipes the chat clean\n/at        : Adventure Time\n/choose    : Picks randomly between multiple choices\n/something : Random Stuff\n/zouss     : Zouss City\n/say       : Echoes whatever you say```\n```\nIf you want to suggest more commands, visit the creator at:\nhttps://discord.gg/2anYtuD```')

@bot.command()
async def kill(mentioned = 'You'):
	await bot.say((mentioned) + ' fell out of the world')

@bot.command()
async def at():
	await bot.say('I want the next adventure time bomb to come out soon. :regional_indicator_a::regional_indicator_t:  :ok_hand:')

@bot.command()
async def clear():
	await bot.say('ﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\nﾠ\n')

@bot.command()
async def choose(*choices : str):
	await bot.say((random.choice(choices)) + ', I choose you!')

@bot.command()
async def something():
	somethings = ['I like tea', 'UNDNDERRTALELL', 'Mmmhmmm. Vsauce, Michael Here.']
	await bot.say(random.choice(somethings))
	
@bot.command()
async def zouss():
	await bot.say('ζουςς is love, ζουςς is life.')
	
@bot.command()
async def ζουςς():
	await bot.say('ζουςς is love, ζουςς is life.')

@bot.command()
async def say(*ecco):
	await bot.say(ecco)

#@bot.command()
#async def give(username, item, quantity)
#	await bot.say('/give is a work in progress.')
#
#@bot.command()
#async def gamemode(gmemde, user)
#	await bot.say('/gamemode is a work in progress.')
#		
bot.run(os.environ['TOKEN_DISCORD'])
