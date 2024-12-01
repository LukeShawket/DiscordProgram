import random
import datetime
import discord

client = discord.Client()

_guild = "YourGuildName"  # Define your guild name here
_token = "YourToken"  # Define your bot token here

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == _guild, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to our server!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() in ['hi', 'hello']:
        await message.channel.send('reeeeeeeeee!')
    elif message.content.lower() == 'roll a dice':
        random_num = random.randint(1, 8)
        await message.channel.send(f'You rolled a {random_num}')
    elif message.content.lower() == 'time':
        _time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await message.channel.send(f'Current time: {_time}')
    elif client.user.name == 'jan Takota':
        await message.channel.send('Shut up!')

client.run(_token)
