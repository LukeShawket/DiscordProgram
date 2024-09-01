# bot.py
import os
import random
import discord
import os
from dotenv import load_dotenv
import datetime

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

load_dotenv()

_token = os.getenv("TOKEN")

_guild = "tomo pi Takota"

client = discord.Client(intents=discord.Intents.all())

# Coonects the bot to the guil.
@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == _guild, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')
 
 # Greatings from bot to the new member of the guild.   
@client.event
async def on_member_join(member):
    await member.create.dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to our server!')

# Test interactions with bot.
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    _first_response = 'reeeeeeeeee!'
    _Dakota_response = 'Shut up!'

    if message.content == 'Hi' or message.content == 'Hello':
        await message.channel.send(_first_response)
    elif client.user.name == 'jan Takota':
        await message.channel.send(_Dakota_response)

# Dice rolling game
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    random_num = random.randint(1, 8)

    if message.content == 'Roll a dice':
        await message.channel.send(random_num)

# Ask time
@client.event
async def on_message(message):
    if message.content == client.user:
        return
    
    _time = datetime.datetime.now()

    if message.content == 'time':
        await message.channel.send(_time)

client.run(_token)