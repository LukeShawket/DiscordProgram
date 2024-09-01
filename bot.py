# bot.py
import os

import discord

import os
from dotenv import load_dotenv

load_dotenv()

_token = os.getenv("TOKEN")

_guild = "tomo pi Takota"

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == _guild, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

client.run(_token)