import os
import random
import discord.ext as commands
from dotenv import load_dotenv



load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

client.run(token)

@client.command(aliases=['quote', 'q', 'wind'])
async def _quote(ctx):
    kazu_quotes = [
        "Come driving rain or winds that churn, I shall return, by blade alone, armed, if barefoot, to my home... I am Kaedehara Kazuha, a wanderer who roams the land. Since we are both travelers, let us journey together for a time.",
        "The wind has ceased... The world is silent, so now is the best time to rest well. See you tomorrow."
    ]
    await ctx.send(str(random.choice(kazu_quotes)))
