import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = "Nzc0MzYzNzM3NzcwNTU3NTAy.X6Wsbg.LZQoMY9izdfAZ5hVVjb4DowePvI"

text_channel_list = []
client = discord.Client()  # starts the discord client.


@client.event
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    if message.content.startswith('!rant'):
        await message.channel.send('Here is a random ramnbling of political nonsense from some website')


client.run(token)