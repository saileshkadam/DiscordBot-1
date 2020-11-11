import discord
import praw
import configparser

#config_path = '/home/ubuntu/tokens/discordToken.txt'
#tokenFile = open(discord_path, 'r')
#token = tokenFile.read()
#praw_path = '/home/ubuntu/tokens/praw_config.ini'

parser = configparser.ConfigParser()

config_path = '/home/ubuntu/tokens/keeg_config.ini'
parser.read(config_path)
discord_token = parser.get('discord', 'token')
reddit = praw.Reddit(client_id=parser.get('praw', 'client_id'),
                     client_secret=parser.get('praw', 'client_secret'),
                     password=parser.get('praw', 'password'),
                     user_agent=parser.get('praw', 'user_agent'),
                     username=parser.get('praw', 'username'))
client = discord.Client()  # starts the discord client.

@client.event
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    m_content = message.content.lower()

    if m_content.startswith('!rant'):
        await message.channel.send('Buckle up kiddos, its going to get political')
    if 'voting' in m_content or 'vote' in m_content:
        await message.add_reaction('<:soldiersam:774092343120887808>')
    if 'tyranny' in m_content or 'tyrannical' in m_content or 'tyrant' in m_content:
        await message.add_reaction('<:nostep:773692274449580062>')
    if 'tax' in m_content:
        await message.add_reaction('<:friedweegs:774055169569587260>')
    if m_content.startswith('!kmeme'):
        subreddit = reddit.subreddit("libertarianmeme")
        await message.channel.send(subreddit.random().url)
    else:
        print()


client.run(token)
