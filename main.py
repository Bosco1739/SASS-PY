import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle

from keep_alive import keep_alive
from datetime import datetime


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')

bot_status = cycle(["Type '!help' for help", "https://www.sass.studsoc.hku.hk/index.php"])





@tasks.loop(seconds=5)
async def change_status():
  await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
  print("Success: Bot is ready!")
  change_status.start()


@client.event
async def on_member_join(member):
  member_channel = member.guild.get_channel(1188116147686625310)
  bot_channel = member.guild.get_channel(1188121722235400215)
  member_count = member.guild.member_count
  bot_count = sum(1 for member in member.guild.members if member.bot)
  await bot_channel.edit(name = f"Bots: {bot_count}")
  await member_channel.edit(name = f"Members: {member_count}")


@client.event
async def on_member_remove(member):
  member_channel = member.guild.get_channel(1188116147686625310)
  bot_channel = member.guild.get_channel(1188121722235400215)
  member_count = member.guild.member_count
  bot_count = sum(1 for member in member.guild.members if member.bot)
  await bot_channel.edit(name = f"Bots: {bot_count}")
  await member_channel.edit(name = f"Members: {member_count}")


async def load():
  for filename in os.listdir('cogs'):
    if filename.endswith(".py"):
      await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
  async with client:
    await load()
    await client.start(str(os.getenv("TOKEN")))


keep_alive()
asyncio.run(main())
