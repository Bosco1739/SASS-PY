import discord
from discord.ext import commands
from discord import app_commands
from discord.interactions import Interaction

class Ping(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Ping.py is ready!")
  
  @app_commands.command(name= "ping", description= "Shows the bot's latency.")
  async def ping(self, ctx:Interaction):
    bot_latency = round(self.client.latency * 1000)
    await ctx.response.send_message(f"Pong! Bot latency: {bot_latency}ms")
    
async def setup(client):
  await client.add_cog(Ping(client))
