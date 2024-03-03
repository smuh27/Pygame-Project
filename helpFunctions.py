import requests, json, os, discord, html
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
SERVER = os.getenv('DISCORD_SERVER')
TOKEN = os.getenv('TOKEN')

info = (requests.get("https://opentdb.com/api.php?amount=10&type=boolean")).json()
results = info['results']

def get_QA():
    for index in range(len(results)):
        for key in results[index]:
            if (key == 'question'):
                return html.unescape(results[index]['question'])

print(get_QA())   