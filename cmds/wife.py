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
  

class wife(Cog_Extension):
  @commands.command()
  async def 我老婆(self,ctx):
    if ctx.author.id==(638726129846452225):
      embed=discord.Embed(title=('赤城'), url=lane['赤城'],timestamp=datetime.datetime.now())
      embed.add_field(name="海事局連結", value=lane['赤城'], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/oauth2/authorize?client_id=886827609005129799&scope=bot&permissions=8", inline=False)
      embed.set_image(url=ca['赤城'])
      await ctx.send(embed=embed)

    elif ctx.author.id==(644925303583670299):
      embed=discord.Embed(title=('獨角獸'), url=lane['獨角獸'],timestamp=datetime.datetime.now())
      embed.add_field(name="海事局連結", value=lane['獨角獸'], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/oauth2/authorize?client_id=886827609005129799&scope=bot&permissions=8", inline=False)
      embed.set_image(url=ca['獨角獸'])
      await ctx.send(embed=embed)
    else:
      await ctx.channel.send('你老婆是誰啦')
  @commands.command()
  async def 我媽媽(self,ctx):
    if ctx.author.id==(638726129846452225):
      embed=discord.Embed(title=('腓特烈大帝'), url=lane['腓特烈大帝'],timestamp=datetime.datetime.now())
      embed.add_field(name="海事局連結", value=lane['腓特烈大帝'], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/oauth2/authorize?client_id=886827609005129799&scope=bot&permissions=8", inline=False)
      embed.set_image(url=ca['腓特烈大帝'])
      await ctx.send(embed=embed)
  @commands.command()
  async def 我老婆的妹妹(self,ctx):
    if ctx.author.id==(638726129846452225):
      embed=discord.Embed(title=('加賀'), url=lane['加賀'],timestamp=datetime.datetime.now())
      embed.add_field(name="海事局連結", value=lane['加賀'], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/oauth2/authorize?client_id=886827609005129799&scope=bot&permissions=8", inline=False)
      embed.set_image(url=ca['加賀'])
      await ctx.send(embed=embed)
  @commands.command()
  async def 我老婆的姊姊(self,ctx):
    if ctx.author.id==(638726129846452225):
      embed=discord.Embed(title=('天城'), url=lane['天城'],timestamp=datetime.datetime.now())
      embed.add_field(name="海事局連結", value=lane['天城'], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/oauth2/authorize?client_id=886827609005129799&scope=bot&permissions=8", inline=False)
      embed.set_image(url=ca['天城'])
      await ctx.send(embed=embed)
      







def setup(bot):
  bot.add_cog(wife(bot))    