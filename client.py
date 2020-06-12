import discord
import os
from discord.ext import commands


client = commands.Bot(command_prefix='.')
client.remove_command('help')

# Load bot commands
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


client.run("NzIwMzYzMTIxMzg2MTkzMDA5.XuE8aQ.Z1pgEQUS9kg4MhP7B5trI9aVWmA")
