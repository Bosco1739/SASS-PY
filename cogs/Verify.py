import discord
from discord.ext import commands
import motor
from motor.motor_asyncio import AsyncIOMotorClient
import time

cluster = AsyncIOMotorClient('mongodb+srv://sasshkuweb:sass2324@cluster0.pkcpidn.mongodb.net/?retryWrites=true&w=majority')
db = cluster["Memberlist"]
cursor = db["member_uid"]

class Verify(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Verify.py is ready!")

  @commands.command()
  async def verify(self, ctx):
    user_input = ctx.message.content.split(" ")[1]
    try:
      member_uid = int(user_input)
      check = await cursor.find_one({"member_uid": user_input})
      if check is None:
        await ctx.message.reply("This user is not in the database.")
        return
      else:
        role = ctx.guild.get_role(1203009142747299860)
        await ctx.author.add_roles(role)
        return

    except ValueError:
      await ctx.message.reply("Please input your UID correctly")
      time.sleep(2)
      await ctx.channel.purge(limit=2)

    
async def setup(client):
  await client.add_cog(Verify(client))
