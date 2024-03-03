import requests, json, os, discord
from discord.ext import commands
from dotenv import load_dotenv
from helpFunctions import get_question
load_dotenv()

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True 

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
SERVER = os.getenv('DISCORD_SERVER')
TOKEN = os.getenv('TOKEN')


@client.event 
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=SERVER)
    await tree.sync(guild=discord.Object(id=guild.id))
    print("Ready!")
    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )



client.run(TOKEN)