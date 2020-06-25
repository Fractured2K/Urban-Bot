import discord
import os
from discord.ext import commands

# Prefix commmands
client = commands.Bot(command_prefix='.')
# Remove default help command
client.remove_command('help')

# Load bot commands
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    # Update bot status
    await client.change_presence(activity=discord.Game('.help'))
    print(f"Logged in as {client.user}")


client.run(os.getenv("TOKEN"))
