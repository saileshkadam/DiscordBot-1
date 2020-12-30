import discord
import praw
import configparser

parser = configparser.ConfigParser()
lastTenPosts = [0];

config_path = '/home/ubuntu/tokens/keeg_config.ini'
parser.read(config_path)
discord_token = parser.get('discord', 'token')
reddit = praw.Reddit(client_id=parser.get('praw', 'client_id'),
                     client_secret=parser.get('praw', 'client_secret'),
                     password=parser.get('praw', 'password'),
                     user_agent=parser.get('praw', 'user_agent'),
                     username=parser.get('praw', 'username'))
client = discord.Client()  # starts the discord client.

def checkValidMeme(meme):
    if('jpg' in meme or 'png' in meme or 'gif' in meme and meme not in lastTenPosts):
        return True
    else:
        return False

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
    if 'tax ' in m_content:
        await message.add_reaction('<:friedweegs:774055169569587260>')
    if m_content.startswith('!kmeme'):
        subreddit = reddit.subreddit("libertarianmeme")
        memeToSend = subreddit.random().url

        while not checkValidMeme(memeToSend):
            memeToSend = subreddit.random().url

        lastTenPosts.append(memeToSend)
        await message.channel.send(memeToSend)
    else:
        print()


client.run(discord_token)
