#ShrekBot for Discord 0.2
#By @AlexApps#9295

import discord
from discord.ext import commands
import random
from random import randint
import os
from PIL import Image
import time
import urllib.parse
import re
import logging

logging.basicConfig( filename="main.log",filemode='w',level=logging.DEBUG,format= '%(asctime)s - %(levelname)s - %(message)s',)

bot = commands.Bot(command_prefix='sh!', case_insensitive=True)

version = '0.2'
bot.remove_command("help")

listening = ['All Star - Smash Mouth','I\'m a believer - Smash Mouth','the blissful sounds of Lord Farquaad','the screeches of Donkey']
playing = ['Shrek Swamp Kart Speedway','Shrek Smash n\' Crash Racing','Shrek Kart','DreamWorks Super Star Kartz','Shrek: Treasure Hunt','Shrek Super Party','Shrek\'s Carnival Craze Party Games','Shrek: Fairy Tale Freakdown','Shrek Game Land Activity Center','Shrek: Hassle at the Castle','Shrek Extra Large','Shrek: Reekin\' Havoc','Shrek 2 Activity Center: Twisted Fairy Tale Fun','Shrek 2: Team Action','Shrek 2: Beg for Mercy','Shrek SuperSlam','Shrek n\' Roll','Shrek: Ogres & Dronkeys','Puss in Boots','Fruit Ninja: Puss in Boots','Shrek\'s Fairytale Kingdom','Shrek Alarm','Shrek: Dragon\'s Tale','Shrek the Third: Arthur\'s School Day Adventure','Shrek the Third: The Search for Arthur']
watching = ['Shrek','Shrek in the Swamp Karaoke Dance Party','Shrek 2','Shrek the Third','Shrek the Halls','Shrek Forever After','Scared Shrekless','Puss in boots']
thingytothingy = {'listening': discord.ActivityType.listening, 'playing': discord.ActivityType.playing, 'watching': discord.ActivityType.watching}
presencelists = ['listening','playing','watching']
presence=random.choice(presencelists)

@bot.event
async def on_ready():
	print('ShrekBot '+version)
	print('Logged in as: '+bot.user.name)
	print('Client User ID: '+str(bot.user.id))
	await bot.change_presence(activity=discord.Activity(type=thingytothingy[presence], name=random.choice(globals()[presence])))

@bot.command(help='Shows help for commands')
async def help(ctx):
	await ctx.send('__**ShrekBot 0.2 Commands:**__\n\n```css\nsh!help      : Shows help for commands\nsh!kill      : Be an assassin\nsh!choose    : Picks randomly between multiple choices\nsh!something : Random Stuff\nsh!zouss     : Zouss City\nsh!echo      : Echoes whatever you say\nsh!ping      : Useful for testing Internet speed\nsh!kick      : For getting rid of annoyances\nsh!hex       : Picks a random hex color\nsh!google    : Searches the web (or images if typed first)\nsh!lmgtfy    : Let me Google that for you\nsh!emojify   : For when plain text just is not enough\nsh!dice      : Leave it to luck\nsh!egg       : For those free range fellas```\n```\nIf you want to suggest more commands, visit the creator at:\nhttps://discord.gg/2anYtuD```')

@bot.command(help='Be an assassin')
async def kill(ctx, *, user = 'You'):
	await ctx.send((user) + ' fell out of the world')

@bot.command(help='Picks randomly between multiple choices')
async def choose(ctx, *choices : str):
	await ctx.send((random.choice(choices)) + ', I choose you!')

@bot.command(help='Random Stuff')
async def something(ctx):
	somethings = ['Somebody once told me the world was gonna roll me.\nI ain\'t the sharpest tool in the shed.', 'WHAT ARE YOU DOING IN MY SWAMP?!', 'Shrek is love, Shrek is life.']
	await ctx.send(random.choice(somethings))

@bot.command(help='Zouss City', aliases=['ζουςς'])
async def zouss(ctx):
	await ctx.send('ζ ο υ ς ς    Ͼ ι τ ψ !')

@bot.command(help='Echoes whatever you say')
async def echo(ctx, *, message):
	await ctx.send(message)

@bot.command(help='For getting rid of annoyances')
async def kick(ctx, username: discord.User):
	try:
		if ctx.message.author.server_permissions.kick_members:
			await bot.kick(username)
			await ctx.send('That fool just got kicked from my swamp!')
			await ctx.send(file=discord.File('WhatAreYouDoingInMySwamp.gif'))
		else:
			await ctx.send('Sorry, you do not have permissions to do that!')
	except:
			await ctx.send('Sorry, but an unexpected error occured. Make sure I have the permissions to kick.')

@bot.command(help='Picks a random hex color')
async def hex(ctx):
	r = lambda: random.randint(0,255)
	hexcode = '%02X%02X%02X' % (r(),r(),r())
	rgbcode = str(tuple(int(hexcode[i:i+2], 16) for i in (0, 2 ,4)))
	await ctx.send('`Hex: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
	im = Image.new("RGB", (64,64), '#' + hexcode)
	im.save("color.png")
	await ctx.send(file=discord.File('color.png'))

@bot.command(help='Useful for testing Internet speed')
async def ping(ctx):
	await ctx.send("🏓 Pong: **{}ms**".format(round(bot.latency * 1000, 2)))

@bot.command(help='Leave it to luck')
async def dice(ctx, number = 6):
	await ctx.send("You rolled a __**{}**__!".format(randint(1, number)))

@bot.command(help='Let me Google that for you')
async def lmgtfy(ctx, *, searchquery: str):
	await ctx.send('<https://lmgtfy.com/?iie=1&q=' + urllib.parse.quote_plus(searchquery) + '>')

@bot.command(help='Searches the web (or images if typed first)') #Make this a group
async def google(ctx, *, searchquery: str):
	searchquerylower = searchquery.lower()
	if searchquerylower.startswith('images '):
		await ctx.send('<https://www.google.com/search?tbm=isch&q=' + urllib.parse.quote_plus(searchquery[7:]) + '>')
	else:
		await ctx.send('<https://www.google.com/search?q=' + urllib.parse.quote_plus(searchquery) + '>')

@bot.command(help='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
	author = ctx.message.author
	emojified = '⬇ Copy and paste this: ⬇\n'
	formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
	if text == '':
		await ctx.send('Remember to say what you want to convert!')
	else:
		for i in formatted:
			if i == ' ':
				emojified += '     '
			else:
				emojified += ':regional_indicator_{}: '.format(i)
		if len(emojified) + 2 >= 2000:
			await ctx.send('Your message in emojis exceeds 2000 characters!')
		if len(emojified) <= 25:
			await ctx.send('Your message could not be converted!')
		else:
			await author.send('`'+emojified+'`')

@bot.command(help='For those free range fellas')
async def egg(ctx):
	await ctx.send('100% Free range!')

@bot.command(help='Secret debug commands')
async def clearlog(ctx):
	if ctx.author.id != 292383975048216576:
		await ctx.send('This is an exclusive bot dev only command!')
	else:
		try:
			open('main.log', 'w').close()
			await ctx.send('All gone!')
		except:
			await ctx.send('An error occured! oof')

@bot.command(help='Secret debug commands')
async def printlog(ctx):
	if ctx.author.id != 292383975048216576:
		await ctx.send('This is an exclusive bot dev only command!')
	else:
		try:
			await ctx.send('```' + open('main.log', 'r').read() + '```')
		except:
			await ctx.send('An error occured! oof')

bot.run(os.environ['TOKEN_DISCORD'])
