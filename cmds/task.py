from asyncio.tasks import sleep
from core.classes import Cog_Extension
import discord
import json,asyncio,datetime
from discord.ext import commands
import random
from discord_components import (
    DiscordComponents,
    Button,
    ButtonStyle,
    Select,
    SelectOption,
    Interaction
)

with open("azur_lane.json",'r',encoding='utf8')as azur_p:
  ca=json.load(azur_p)

class task(Cog_Extension):

  @commands.command()
  async def geturl(self,ctx, emoji: discord.Emoji):
      await ctx.send(emoji.url)

def setup(bot):
    bot.add_cog(task(bot))