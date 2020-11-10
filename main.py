import discord

path = '/home/ubuntu/tokens/discordToken.txt'
tokenFile = open(path,'r')
token = tokenFile.read()

client = discord.Client()  # starts the discord client.


@client.event
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    if message.content.startswith('!rant'):
        await message.channel.send('Buckle up kiddos, its going to get political')

    if ('voting' in message.content) or ('taxes' in message.content):
        await message.channel.send(':soldiersam:')


client.run(token)