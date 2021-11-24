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


class test(Cog_Extension):
    @cog_ext.cog_slash(name="loli",
             description="This is just a test command, nothing more.",
             options=[
               create_option(
                 name="optone",
                 description="This is the first option we have.",
                 option_type=3,
                 required=True,
                 choices=[
                   create_choice(name='fuck',value='ok'),
                   create_choice(name='loli',value='is ok')

                 
                 ])
                 
                 ]
)
    async def _loli(self,ctx, optone: str):
      await ctx.send(content=f"Wow, you actually chose {optone}!")



def setup(bot):
  bot.add_cog(test(bot))      
