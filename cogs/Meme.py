import discord
from discord.ext import commands
import json
import random

class Meme(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("MemeCommand.py is ready!")

  @commands.command()
  async def meme(self, ctx):
    memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

    memeData = json.load(memeAPI)

    memeURL = memeData['url']
    memeName = memeData['title']
    memePoster = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postlink']

    embed = discord.Embed(title=memeName, color=discord.Color.blue())
    embed.set_image(url=memePoster)
    embed.set_footer(text=f"Meme by {memePoster} | Subreddit: {memeSub} | Post: {memeLink}")
    await ctx.send(embed=embed)


async def setup(client):
  await client.add_cog(Meme(client))
