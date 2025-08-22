import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# set up the bot with the necessary intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print('Ready to go@')

client.run(TOKEN)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! I am your friendly bot!')

    if message.content.startswith('!bye'):
        await message.channel.send('Goodbye! See you next time!')