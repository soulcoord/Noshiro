from core.classes import Cog_Extension
import discord
import json

from discord_slash import SlashCommand, SlashContext, cog_ext
from discord.ext import commands
from discord_slash.utils.manage_commands import create_choice,create_option


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

slash = SlashCommand(bot, sync_commands=True)

with open("set.json",'r',encoding='utf8')as jfile:
  jdata=json.load(jfile)
class mes(Cog_Extension):




    





    @commands.command()
    async def sayd(self,ctx,*,msg):
      msg = discord.utils.escape_mentions(msg)  
      await ctx.message.delete()
      await ctx.send(msg)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clean(self,ctx,num:int):
      await ctx.channel.purge(limit=num+1)

      

   
def setup(bot):
    bot.add_cog(mes(bot))
