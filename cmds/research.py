from core.classes import Cog_Extension
import discord
import json
from discord.ext import commands
import asyncio
import datetime
import random
from discord_components import (
    DiscordComponents,
    Button,
    ButtonStyle,
    Select,
    SelectOption,
    Interaction,
)


with open("research.json",'r',encoding='utf8')as azur_r:
  cr=json.load(azur_r)


class research(Cog_Extension):

 
  @commands.command(name='科研')
  async def 科研(self,ctx):
    print(datetime.datetime.now())

    res=await ctx.send(
    "選擇第幾期科研",
    components = [
    Select(

    placeholder = "科研選擇",
    options =[ 
                    SelectOption(label = "一期", value = "A",description="選擇一期科研"),
                    SelectOption(label = "二期", value = "B",description="選擇二期科研"),
                    SelectOption(label = "三期", value = "C",description="選擇三期科研"),
                    SelectOption(label = "四期", value = "D",description="選擇四期科研")
                ]
            )
    ]

     
    )
    aa=Select(
     placeholder = "科研選擇",
    options =[ 
                    SelectOption(label = "一期", value = "A",description="選擇一期科研"),
                    SelectOption(label = "二期", value = "B",description="選擇二期科研"),
                    SelectOption(label = "三期", value = "C",description="選擇三期科研"),
                    SelectOption(label = "四期", value = "D",description="選擇四期科研")
                ]
            )


    



    

    try:
      while True:
        interaction=await self.bot.wait_for('select_option',timeout=180.0)
  
        
        if interaction.values[0]=='A':
          embed=discord.Embed(title="科研系統(一期)", color=0x000000,timestamp=datetime.datetime.now())
          embed.add_field(name="海王星", value="https://wiki.biligame.com/blhx/%E6%B5%B7%E7%8E%8B%E6%98%9F", inline=False)
          embed.add_field(name="君主", value="https://wiki.biligame.com/blhx/%E5%90%9B%E4%B8%BB", inline=False)
          embed.add_field(name="伊吹", value="https://wiki.biligame.com/blhx/%E4%BC%8A%E5%90%B9", inline=False)
          embed.add_field(name="出雲", value="https://wiki.biligame.com/blhx/%E5%87%BA%E4%BA%91", inline=False)
          embed.add_field(name="羅恩", value="https://wiki.biligame.com/blhx/%E7%BD%97%E6%81%A9", inline=False)
          embed.add_field(name="路易九世", value="https://wiki.biligame.com/blhx/%E8%B7%AF%E6%98%93%E4%B9%9D%E4%B8%96", inline=False)
          embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          embed.set_image(url=random.choice(cr['科研一期']))
          
          await interaction.edit_origin(embed=embed,components=[aa])
        
        
        
        elif interaction.values[0]=='B':
          embed=discord.Embed(title="科研系統(二期)", color=0x000000,timestamp=datetime.datetime.now())
          embed.add_field(name="西亞圖", value="https://wiki.biligame.com/blhx/%E8%A5%BF%E9%9B%85%E5%9B%BE", inline=False)
          embed.add_field(name="佐治亞", value="https://wiki.biligame.com/blhx/%E4%BD%90%E6%B2%BB%E4%BA%9A", inline=False)
          embed.add_field(name="北風", value="https://wiki.biligame.com/blhx/%E5%8C%97%E9%A3%8E", inline=False)
          embed.add_field(name="吾妻", value="https://wiki.biligame.com/blhx/%E5%90%BE%E5%A6%BB", inline=False)
          embed.add_field(name="腓特烈大帝", value="https://wiki.biligame.com/blhx/%E8%85%93%E7%89%B9%E7%83%88%E5%A4%A7%E5%B8%9D", inline=False)
          embed.add_field(name="加斯科涅", value="https://wiki.biligame.com/blhx/%E5%8A%A0%E6%96%AF%E7%A7%91%E6%B6%85", inline=False)
          embed.set_image(url=random.choice(cr['科研二期']))
          embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          await interaction.edit_origin(embed=embed,components=[aa])
        
    
    
        elif interaction.values[0]=='C':
          embed=discord.Embed(title="科研系統(三期)", color=0x000000,timestamp=datetime.datetime.now())
          embed.add_field(name="柴郡", value="https://wiki.biligame.com/blhx/%E6%9F%B4%E9%83%A1", inline=False)
          embed.add_field(name="德雷克", value="https://wiki.biligame.com/blhx/%E5%BE%B7%E9%9B%B7%E5%85%8B", inline=False)
          embed.add_field(name="美因茲", value="https://wiki.biligame.com/blhx/%E7%BE%8E%E5%9B%A0%E8%8C%A8", inline=False)
          embed.add_field(name="奧丁", value="https://wiki.biligame.com/blhx/%E5%A5%A5%E4%B8%81", inline=False)
          embed.add_field(name="香檳", value="https://wiki.biligame.com/blhx/%E9%A6%99%E6%A7%9F", inline=False)
          embed.set_image(url=random.choice(cr['科研三期']))
          embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          await interaction.edit_origin(embed=embed,components=[aa])
     
        
    
        elif interaction.values[0]=='D':
          embed=discord.Embed(title="科研系統(四期)", color=0x000000,timestamp=datetime.datetime.now())
          embed.add_field(name="安克雷奇", value="https://wiki.biligame.com/blhx/%E5%AE%89%E5%85%8B%E9%9B%B7%E5%A5%87", inline=False)
          embed.add_field(name="白龍", value="https://wiki.biligame.com/blhx/%E7%99%BD%E9%BE%99", inline=False)
          embed.add_field(name="埃吉爾", value="https://wiki.biligame.com/blhx/%E5%9F%83%E5%90%89%E5%B0%94", inline=False)
          embed.add_field(name="奧古斯特", value="https://wiki.biligame.com/blhx/%E5%A5%A5%E5%8F%A4%E6%96%AF%E7%89%B9%C2%B7%E5%86%AF%C2%B7%E5%B8%95%E5%A1%9E%E7%93%A6%E5%B0%94", inline=False)
          embed.add_field(name="馬克·波羅", value="https://wiki.biligame.com/blhx/%E9%A9%AC%E5%8F%AF%C2%B7%E6%B3%A2%E7%BD%97", inline=False)
          embed.set_image(url=random.choice(cr['科研四期']))
          embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          await interaction.edit_origin(embed=embed,components=[aa])
    except asyncio.TimeoutError:
      await res.delete()
      





def setup(bot):
    bot.add_cog(research(bot))