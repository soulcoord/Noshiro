from core.classes import Cog_Extension
import discord
import json
from discord.ext import commands
import datetime
import random

with open("azur.json",'r',encoding='utf8')as azurs:
  lane=json.load(azurs)

with open("azur_lane.json",'r',encoding='utf8')as azur_p:
  ca=json.load(azur_p)

with open("level.json",'r',encoding='utf8')as azurs_level:
  ce=json.load(azurs_level)

with open("evaluation.json",'r',encoding='utf8')as azurs_aa:
  ce1=json.load(azurs_aa)

with open("alias.json",'r',encoding='utf8')as alias_aa:
  alias=json.load(alias_aa)







class azur(Cog_Extension):
  @commands.command()
  async def girl(self,ctx,boat):
      pronoun=alias[boat]
      if (pronoun in ce1):
        embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
        embed.add_field(name="海事局連結", value=lane[pronoun], inline=False)
        embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands", inline=False)
        embed.add_field(name="評價", value=ce1[pronoun], inline=False)
        embed.set_image(url=ca[pronoun])
        embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
        await ctx.send(embed=embed)
        await ctx.message.delete()
      else:
        embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
        embed.add_field(name="海事局連結", value=lane[pronoun], inline=False)
        embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands", inline=False)
        embed.set_image(url=ca[pronoun])
        embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
        await ctx.send(embed=embed)
        await ctx.message.delete()
        


  
  @commands.command()
  async def 建造時間(self,ctx):
    await ctx.send('https://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%97%B6%E9%97%B4')
  @commands.command()
  async def level(self,ctx,start,end,remaining):
    if start>end:
      await ctx.send('你打反啦')
    else:
      result=int(ce[end])-int(ce[start])-int(remaining)
      if (result%3000)==0:
        need=result//3000
      else:
        need=(result//3000)+1
      await ctx.send(f'你還缺{result}經驗(艦艇研習數據T1 {need}本)才能到達等級{end}')


  
  

def setup(bot):
    bot.add_cog(azur(bot))      






