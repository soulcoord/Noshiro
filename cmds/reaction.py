from core.classes import Cog_Extension
import discord
import json
from discord.ext import commands
with open("set.json",'r',encoding='utf8')as jfile:
  jdata=json.load(jfile)




class reaction(Cog_Extension):
  @commands.has_permissions(administrator=True)
  @commands.command()
  async def 表情符號(self,ctx):
      await ctx.send('領取身分組')
      await ctx.add_reaction('<:good:902928424711114763>')
  
  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self,payload):
    if str(payload.emoji)=='<:good:902928424711114763>':
      guild=self.bot.get_guild(payload.guild_id)#取的當前所在伺服器
      role=guild.get_role(902928683835199498)#取得伺服器內指定的身分組
      await payload.member.add_roles(role)#給予表情用戶身分組
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self,payload):
    if str(payload.emoji)=='<:good:902928424711114763>':
      guild=self.bot.get_guild(payload.guild_id)
      user=guild.get_member(payload.user_id)
      role=guild.get_role(902928683835199498)#取得伺服器內指定的身分組
      await user.remove_roles(role)

def setup(bot):
    bot.add_cog(reaction(bot))