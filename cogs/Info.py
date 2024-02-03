from logging import info
import discord
from discord.ext import commands
from datetime import datetime

class Info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Info.py is ready")

  @commands.command()
  async def info(self, ctx):
    info_embed = discord.Embed(title="Information about Our Society", color=discord.Color.blue())

    info_embed.set_author(name="Statistics and Actuarial Science Society SS HKU", icon_url=self.client.user.display_avatar)
    info_embed.set_thumbnail(url=self.client.user.display_avatar)
    info_embed.add_field(name="Facebook", value="[[Click Here]](https://www.facebook.com/sasshku/)", inline=False)
    info_embed.add_field(name="Instagram", value="[[Click Here]](https://www.instagram.com/sass.ss.hkusu/)", inline=False)
    info_embed.add_field(name="Society Website", value="[[Click Here]](https://www.sass.studsoc.hku.hk/)", inline=False)
    info_embed.add_field(name="Society Email", value="sass@hku.hk")
    info_embed.set_footer(text=f"Requested by <@{ctx.author}>.", icon_url=ctx.author.display_avatar)
    info_embed.timestamp = datetime.utcnow()
    
    await ctx.send(embed=info_embed)


async def setup(client):
  await client.add_cog(Info(client))
    