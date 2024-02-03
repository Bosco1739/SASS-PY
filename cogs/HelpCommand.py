import discord
from discord.ext import commands
from datetime import datetime

class HelpCommand(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("HelpCommand.py is ready!")

  @commands.command()
  async def help(self, ctx):
    help_embed = discord.Embed(title="Help Desk for SASS.BOT", description="All commands for the bot.", color=discord.Color.blue())

    help_embed.set_author(name="SASS.BOT", icon_url=self.client.user.display_avatar)
    help_embed.add_field(name="Help", value="Shows this message.", inline=True)
    help_embed.add_field(name="Info", value="Information about our society.", inline=True)
    help_embed.add_field(name="Ping", value="Shows the bot latency.", inline=True)
    help_embed.set_footer(text=f"Requested by <@{ctx.author}>.", icon_url=ctx.author.display_avatar)
    help_embed.timestamp = datetime.utcnow()

    await ctx.send(embed=help_embed)


async def setup(client):
  await client.add_cog(HelpCommand(client))
    