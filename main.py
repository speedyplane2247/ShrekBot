#ShrekBot for Discord 0.2
#By @AlexApps#9295

import discord
from discord.ext import commands
import random
import os
from PIL import Image
import colorsys

bot = commands.Bot(command_prefix='sh!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print('ShrekBot 0.2')
	print('')
	print('Logged in as:')
	print(bot.user.name)
	print('')
	print('Client User ID:')
	print(bot.user.id)
	print('')
	await bot.change_presence(game=discord.Game(name='Shrek the Third', type=3))

@bot.command()
async def help():
	await bot.say('__**ShrekBot 0.2 Commands:**__\n\n```css\nsh!help      : Shows help for commands\nsh!kill      : Kill minecraft avatars\nsh!choose    : Picks randomly between multiple choices\nsh!something : Random Stuff\nsh!zouss     : Zouss City\nsh!echo      : Echoes whatever you say\nsh!ping      : Useful for testing Internet speed\nsh!kick      : For getting rid of annoyances\nsh!hex       : Picks a random hex color```\n```\nIf you want to suggest more commands, visit the creator at:\nhttps://discord.gg/2anYtuD```')

@bot.command()
async def kill(*, mentioned = 'You'):
	await bot.say((mentioned) + ' fell out of the world')

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

@bot.command()
async def ping():
	await bot.say('Pong!')

@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
	try:
		if ctx.message.author.server_permissions.kick_members:
			await bot.kick(userName)
			await bot.say('That fool just got kicked from my swamp!')
			await bot.upload('WhatAreYouDoingInMySwamp.gif')
		else:
			await bot.say('Sorry, you do not have permissions to do that!')
	except:
			await bot.say('Sorry, but an unexpected error occured. Make sure I have the permissions to kick.')
			
@bot.command()
async def hex():
	r = lambda: random.randint(0,255)
	hexcode = '%02X%02X%02X' % (r(),r(),r())
	rgbcode = str(tuple(int(hexcode[i:i+2], 16) for i in (0, 2 ,4)))
#	splitrgbcode = rgbcode.split(',')
#	hsvcode = colorsys.rgb_to_hsv(splitrgbcode)
	await bot.say('`Hex: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
	im = Image.new("RGB", (64,64), '#' + hexcode)
	im.save("color.png")
	await bot.upload('color.png')

bot.run(os.environ['TOKEN_DISCORD'])
