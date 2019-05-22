'''
# ShrekBot for Discord 0.2
# By @AlexApps#9295
# Now with 100% more PEP8!
'''

import base64
import json
import os
import random
from random import randint
import re
import signal
import sys
import urllib.parse
import datetime

from PIL import Image
import requests
import discord
from discord.ext import commands

if "TOKEN_DISCORD" in os.environ:
    TOKEN_DISCORD = os.environ['TOKEN_DISCORD']
elif len(sys.argv) >= 2:
    TOKEN_DISCORD = sys.argv[1]
elif os.path.isfile('token_discord.txt'):
    TOKENFILE = open('token_discord.txt', 'r')
    TOKEN_DISCORD = TOKENFILE.read()
    TOKENFILE.close()
else:
    print('Please provide a token')
    sys.exit(1)

BOT = commands.Bot(command_prefix='sh!', case_insensitive=True)

BOT.remove_command("help")

LISTENING = ['All Star - Smash Mouth', 'I\'m a believer - Smash Mouth',
             'the blissful sounds of Lord Farquaad', 'the screeches of Donkey']
PLAYING = ['Shrek Swamp Kart Speedway', 'Shrek Smash n\' Crash Racing',
           'Shrek Kart', 'DreamWorks Super Star Kartz', 'Shrek: Treasure Hunt',
           'Shrek Super Party', 'Shrek\'s Carnival Craze Party Games',
           'Shrek: Fairy Tale Freakdown', 'Shrek Game Land Activity Center',
           'Shrek: Hassle at the Castle', 'Shrek Extra Large',
           'Shrek: Reekin\' Havoc', 'Shrek 2 Activity Center: Twisted Fairy Tale Fun',
           'Shrek 2: Team Action', 'Shrek 2: Beg for Mercy', 'Shrek SuperSlam',
           'Shrek n\' Roll', 'Shrek: Ogres & Dronkeys', 'Puss in Boots',
           'Fruit Ninja: Puss in Boots', 'Shrek\'s Fairytale Kingdom', 'Shrek Alarm',
           'Shrek: Dragon\'s Tale', 'Shrek the Third: Arthur\'s School Day Adventure',
           'Shrek the Third: The Search for Arthur']
WATCHING = ['Shrek', 'Shrek in the Swamp Karaoke Dance Party', 'Shrek 2',
            'Shrek the Third', 'Shrek the Halls', 'Shrek Forever After',
            'Scared Shrekless', 'Puss in boots']
ACTIVITYTYPE = {'LISTENING': discord.ActivityType.listening,
                'PLAYING': discord.ActivityType.playing,
                'WATCHING': discord.ActivityType.watching}
PRESENCELISTS = ['LISTENING', 'PLAYING', 'WATCHING']
PRESENCE = random.choice(PRESENCELISTS)

INFO = open('commands.md', 'r')
INFOTEXT = INFO.read()
INFO.close()

@BOT.event
async def on_ready():
    '''
    Prepares and starts the bot
    '''
    print('ShrekBot 0.2')
    print('Logged in as: '+BOT.user.name)
    print('Client User ID: '+str(BOT.user.id))
    await BOT.change_presence(activity=discord.Activity(
        type=ACTIVITYTYPE[PRESENCE], name=(random.choice(globals()[PRESENCE])+' | sh!info')))

def sigterm_handler():
    '''
    Cleans up at SIGTERM
    '''
    BOT.logout()
    print('Shutting down...')
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

@BOT.command(helpinfo='Shows info about the bot', aliases=['help', 'about'])
async def info(ctx):
    '''
    Provides information about commands and the bot itself.
    '''
    await ctx.send(INFOTEXT)

@BOT.command(helpinfo='Be an assassin')
async def kill(ctx, *, user='You'):
    '''
    Kills the player, minecraft style
    '''
    await ctx.send((user) + ' fell out of the world')

@BOT.command(helpinfo='Picks randomly between multiple choices')
async def choose(ctx, *choices: str):
    '''
    Picks randomly from all choices provided.
    '''
    await ctx.send((random.choice(choices)) + ', I choose you!')

@BOT.command(helpinfo='Random Stuff')
async def something(ctx):
    '''
    Tells a random Shrek quote
    '''
    somethings = [
        'Somebody once told me the world was gonna roll me.',
        'I ain\'t the sharpest tool in the shed.',
        'WHAT ARE YOU DOING IN MY SWAMP?!',
        'Shrek is love, Shrek is life.']
    await ctx.send(random.choice(somethings))

@BOT.command(helpinfo='Zouss City', aliases=['ζουςς'])
async def zouss(ctx):
    '''
    Zouss City = Life City
    '''
    await ctx.send('ζ ο υ ς ς    Ͼ ι τ ψ !')

@BOT.command(helpinfo='Echoes whatever you say')
async def echo(ctx, *, message):
    '''
    Repeats whatever you inputted
    '''
    await ctx.send(message)

@BOT.command(helpinfo='For getting rid of annoyances')
async def kick(ctx, usr: discord.Member, *, rsn=''):
    '''
    Kicks mentioned member
    '''
    try:
        if ctx.author.guild_permissions.kick_members:
            await usr.kick(reason='Kicker: {}, Reason: {}'
                           .format('{}#{}'
                                   .format(ctx.author.name,
                                           ctx.author.discriminator)
                                   , rsn))
            await ctx.send('That fool just got kicked from my swamp!')
            await ctx.send(file=discord.File('WhatAreYouDoingInMySwamp.gif'))
        else:
            await ctx.send('Sorry, you do not have permissions to do that!')
    except discord.errors.Forbidden:
        await ctx.send('Sorry, but I do not have permission to kick.')

@BOT.command(helpinfo='Picks a random hex color', aliases=['hex', 'colour'])
async def color(ctx, inputcolor=''):
    '''
    Randomly picks a color, or displays a hex color
    '''
    if inputcolor == '':
        randgb = lambda: random.randint(0, 255)
        hexcode = '%02X%02X%02X' % (randgb(), randgb(), randgb())
        rgbcode = str(tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4)))
        await ctx.send('`Hex: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
        heximg = Image.new("RGB", (64, 64), '#' + hexcode)
        heximg.save("color.png")
        await ctx.send(file=discord.File('color.png'))
    else:
        if inputcolor.startswith('#'):
            hexcode = inputcolor[1:]
            if len(hexcode) == 8:
                hexcode = hexcode[:-2]
            elif len(hexcode) != 6:
                await ctx.send('Make sure hex code is this format: `#7289DA`')
            rgbcode = str(tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4)))
            await ctx.send('`Hex: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
            heximg = Image.new("RGB", (64, 64), '#' + hexcode)
            heximg.save("color.png")
            await ctx.send(file=discord.File('color.png'))
        else:
            await ctx.send('Make sure hex code is this format: `#7289DA`')

@BOT.command(helpinfo='Useful for testing Internet speed')
async def ping(ctx):
    '''
    Checks latency on Discord
    '''
    await ctx.send("🏓 Pong: **{}ms**".format(round(BOT.latency * 1000, 2)))

@BOT.command(helpinfo='Leave it to luck', aliases=['roll', 'random'])
async def dice(ctx, number=6):
    '''
    Picks a random int between 1 and number
    '''
    await ctx.send("You rolled a __**{}**__!".format(randint(1, number)))

@BOT.command(helpinfo='Let me Google that for you')
async def lmgtfy(ctx, *, searchquery: str):
    '''
    Sarcastic site for helping googling
    '''
    await ctx.send('<https://lmgtfy.com/?iie=1&q={}>'
                   .format(urllib.parse.quote_plus(searchquery)))

@BOT.command(helpinfo='Searches the web (or images if typed first)', aliases=['search'])
async def google(ctx, *, searchquery: str):
    '''
    Should be a group in the future
    Googles searchquery, or images if you specified that
    '''
    searchquerylower = searchquery.lower()
    if searchquerylower.startswith('images '):
        await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'
                       .format(urllib.parse.quote_plus(searchquery[7:])))
    else:
        await ctx.send('<https://www.google.com/search?q={}>'
                       .format(urllib.parse.quote_plus(searchquery)))

@BOT.command(helpinfo='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into emoji
    '''
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

@BOT.command(helpinfo='When your text needs to be c o n c e a l e d')
async def spoilify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into hidden secrets
    '''
    author = ctx.message.author
    spoilified = '⬇ Copy and paste this: ⬇\n'
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in text:
            spoilified += '||{}||'.format(i)
        if len(spoilified) + 2 >= 2000:
            await ctx.send('Your message in spoilers exceeds 2000 characters!')
        if len(spoilified) <= 4:
            await ctx.send('Your message could not be converted!')
        else:
            await author.send('`'+spoilified+'`')

@BOT.command(helpinfo='Secret debug commands', aliases=['restart'])
async def reboot(ctx):
    '''
    This command only works for me, and reboots the bot on heroku.
    '''
    if ctx.author.id != 292383975048216576:
        await ctx.send('This is an exclusive bot developer only command!')
    else:
        await ctx.send('**Restarting...**')
        await BOT.logout()
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/vnd.heroku+json; version=3',
                   'Authorization': 'Bearer {}'
                                    .format(os.environ['HEROKU_API_KEY'])}
        requests.delete('https://api.heroku.com/apps/shrek-bot/dynos/worker',
                        headers=headers)

@BOT.command(helpinfo='Clone your words - like echo')
async def clone(ctx, *, message):
    '''
    Creates a webhook, that says what you say. Like echo.
    '''
    pfp = requests.get(ctx.author.avatar_url_as(format='png', size=256)).content
    hook = await ctx.channel.create_webhook(name=ctx.author.display_name,
                                            avatar=pfp)

    await hook.send(message)
    await hook.delete()

@BOT.command(helpinfo='Shows MC skin')
async def skin(ctx, username='Shrek'):
    '''
    Sends specified MC skin to Discord
    '''
    uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'
                        .format(username)).json()['id']

    url = json.loads(base64.b64decode(requests.get(
        'https://sessionserver.mojang.com/session/minecraft/profile/{}'
        .format(uuid)).json()['properties'][0]['value'])
                     .decode('utf-8'))['textures']['SKIN']['url']

    skinurl = requests.get(url).content
    await ctx.send('**Username: `{}`**'.format(username))
    await ctx.send(file=discord.File(skinurl, filename='{}.png'.format(username)))

@BOT.command(helpinfo='Searches for YouTube videos', aliases=['yt'])
async def youtube(ctx, *, query: str):
    '''
    Uses YouTube Data v3 API to search for videos
    '''
    req = requests.get(
        ('https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1'
         '&order=relevance&q={}&relevanceLanguage=en&safeSearch=moderate&type=video'
         '&videoDimension=2d&fields=items%2Fid%2FvideoId&key=')
        .format(query) + os.environ['YOUTUBE_API_KEY'])
    await ctx.send('**Video URL: https://www.youtube.com/watch?v={}**'
                   .format(req.json()['items'][0]['id']['videoId']))

@BOT.command(helpinfo='Who created the bot')
async def owner(ctx):
    '''
    Yadaya self explanatory
    '''
    await ctx.send('This bot was made by `AlexApps#9295`')

@BOT.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
async def wikipedia(ctx, *, query: str):
    '''
    Uses Wikipedia APIs to summarise search
    '''
    sea = requests.get(
        ('https://en.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Sorry, your search could not be found.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://en.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Sorry, your search could not be found.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://en.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=embed)

@BOT.command(helpinfo='Number of servers ShrekBot is in', aliases=['server', 'num', 'count'])
async def servers(ctx):
    '''
    Number of servers ShrekBot is in
    '''
    await ctx.send('**Number of servers:** ***'+str(len(BOT.guilds))+'***!')

@BOT.command(helpinfo='Info about servers ShrekBot is in', aliases=['sinfo', 'sv', 'si'])
async def serverinfo(ctx):
    '''
    Info about servers ShrekBot is in
    '''
    for x in BOT.guilds:
        await ctx.send('***{}, {} Members***'.format(x.name, x.member_count))


BOT.run(TOKEN_DISCORD)
