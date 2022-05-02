from core.classes import Cog_Extension
import discord
import json
import datetime
import asyncio
from discord.ext import commands

class help(Cog_Extension):
  @commands.command()
  async def help(self,ctx):
    embed1=discord.Embed(title="關於碧藍航線的指令",color=0xa3d3ff)
    embed1.add_field(name="> 查詢艦船", value="$girl (艦船名稱)", inline=False)
    embed1.add_field(name="> 查詢科研", value="$科研", inline=False)
    embed1.add_field(name="> 查詢所需經驗", value="$level (目前的等級) (目標等級) (目前經驗)", inline=False)
    embed1.add_field(name="> 數值", value="$數值 (艦船名稱)", inline=False)
    embed1.add_field(name="> 別名(舉例：海王星砲)", value="$別名 海王星砲", inline=False)
    
    await ctx.author.send(embed=embed1)

  @commands.command()
  async def 我有問題(self,ctx,title,*,content):
    b=self.bot.get_user(366574612449853460)
    embed=discord.Embed(timestamp=datetime.datetime.now())
    embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
    embed.add_field(name=title,value=content)
    await b.send(embed=embed)
    






def setup(bot):
    bot.add_cog(help(bot))