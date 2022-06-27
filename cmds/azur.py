from core.classes import Cog_Extension
import discord
from discord import File
import json
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice,create_option
import datetime
import random
from easy_pil import Editor, load_image_async, Font
from discord_components import (
    DiscordComponents,
    Button,
    ButtonStyle,
    Select,
    SelectOption,
    Interaction)
import asyncio

with open("azur.json",'r',encoding='utf8')as azurs:
  lane=json.load(azurs)

with open("set.json", 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
  
with open("azur_lane.json",'r',encoding='utf8')as azur_p:
  ca=json.load(azur_p)

with open("level.json",'r',encoding='utf8')as azurs_level:
  ce=json.load(azurs_level)

with open("evaluation.json",'r',encoding='utf8')as azurs_aa:
  ce1=json.load(azurs_aa)

with open("alias.json",'r',encoding='utf8')as alias_aa:
  alias=json.load(alias_aa)

with open("chde.json",'r',encoding='utf8')as chde:
  chde1=json.load(chde)

with open("azur_1.json",'r',encoding='utf8')as azur_lf:
  azur_le=json.load(azur_lf)







class azur(Cog_Extension):
  @commands.command()
  async def girl(self,ctx,boat):
    pronoun=alias[boat]
    tmp1 = jdata[pronoun][1].split("→")
    tmp2 = jdata[pronoun][3].split("→")
    tmp3 = jdata[pronoun][5].split("→")
    tmp5 = jdata[pronoun][9].split("→")
    tmp6 = jdata[pronoun][11].split("→")
    tmp7 = jdata[pronoun][13].split("→")
    tmp8 = jdata[pronoun][15].split("→")
    tmp9 = jdata[pronoun][17].split("→")
    get=azur_le['獲得'][pronoun]
    full=azur_le['滿星'][pronoun]
    lv120=azur_le['Lv.120'][pronoun]


    if (pronoun in ce1) and (pronoun in azur_le['解鎖']):
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      embed.add_field(name='艦種',value=azur_le['艦種'][pronoun], inline=True )
      embed.add_field(name='陣營',value=azur_le['陣營'][pronoun], inline=True )
      
      embed.add_field(name="科研點", value=f"●獲得：{str(azur_le['獲得'][pronoun])}●滿星：{str(azur_le['滿星'][pronoun])}●LV.120：{str(azur_le['Lv.120'][pronoun])}●總和：{str(get+full+lv120)}", inline=False)
      
      embed.add_field(name="科研屬性加成", value=f"●獲得：{str(azur_le['解鎖'][pronoun])}●LV.120：{str(azur_le['120級(屬性加成)'][pronoun])}", inline=False)
      if len(tmp1)==2:
        embed.add_field(name="數值(好感度：愛 等級：125)", value=f"●砲擊：{tmp2[1]}●防空：{tmp3[1]}●雷擊：{tmp5[1]}●航空：{tmp6[1]}●裝填：{tmp7[1]}●機動：{tmp8[1]}●命中：{tmp9[1]}", inline=False)
      if len(tmp1)==1:
        embed.add_field(name="數值(好感度：愛 等級：125)", value=f"●砲擊：{tmp2[0]}●防空：{tmp3[0]}●雷擊：{tmp5[0]}●航空：{tmp6[0]}●裝填：{tmp7[0]}●機動：{tmp8[0]}●命中：{tmp9[0]}", inline=False)
      
      embed.add_field(name="海事局連結", value=f'[{pronoun}]({lane[pronoun]})', inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="[點擊這裡加入](https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands)", inline=False)
      embed.add_field(name="評價", value=ce1[pronoun], inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
      await ctx.message.delete()
    elif (pronoun in ce1) and (pronoun not in azur_le['解鎖']):
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      if len(tmp1)==2:
        embed.add_field(name="數值(好感度：愛 等級：125)", value=f"●砲擊：{tmp2[1]}●防空：{tmp3[1]}●雷擊：{tmp5[1]}●航空：{tmp6[1]}●裝填：{tmp7[1]}●機動：{tmp8[1]}●命中：{tmp9[1]}", inline=False)
      if len(tmp1)==1:
        embed.add_field(name="數值(好感度：愛 等級：125)", value=f"●砲擊：{tmp2[0]}●防空：{tmp3[0]}●雷擊：{tmp5[0]}●航空：{tmp6[0]}●裝填：{tmp7[0]}●機動：{tmp8[0]}●命中：{tmp9[0]}", inline=False)
      
      embed.add_field(name="海事局連結", value=f'[{pronoun}]({lane[pronoun]})', inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="[點擊這裡加入](https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands)", inline=False)
      embed.add_field(name="評價", value=ce1[pronoun], inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
    elif (pronoun not in ce1) and (pronoun not in azur_le['解鎖']):
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      
      embed.add_field(name="海事局連結", value=f'[{pronoun}]({lane[pronoun]})', inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="[點擊這裡加入](https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands)", inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      embed.add_field(name='艦種',value=azur_le['艦種'][pronoun], inline=True )
      embed.add_field(name='陣營',value=azur_le['陣營'][pronoun], inline=True )
      
      embed.add_field(name="科研點", value=f"●獲得：{str(azur_le['獲得'][pronoun])}●滿星：{str(azur_le['滿星'][pronoun])}●LV.120：{str(azur_le['Lv.120'][pronoun])}●總和：{str(get+full+lv120)}", inline=False)
      
      embed.add_field(name="科研屬性加成", value=f"●獲得：{str(azur_le['解鎖'][pronoun])}●LV.120：{str(azur_le['120級(屬性加成)'][pronoun])}", inline=False)
      if len(tmp1)==2:
        embed.add_field(name="數值(好感度：愛 等級：125)", value=f"●砲擊：{tmp2[1]}●防空：{tmp3[1]}●雷擊：{tmp5[1]}●航空：{tmp6[1]}●裝填：{tmp7[1]}●機動：{tmp8[1]}●命中：{tmp9[1]}", inline=False)
      if len(tmp1)==1:
        embed.add_field(name="數值(好感度：愛 等級：125)", value=f"●砲擊：{tmp2[0]}●防空：{tmp3[0]}●雷擊：{tmp5[0]}●航空：{tmp6[0]}●裝填：{tmp7[0]}●機動：{tmp8[0]}●命中：{tmp9[0]}", inline=False)
      
      embed.add_field(name="海事局連結", value=f'[{pronoun}]({lane[pronoun]})', inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="[點擊這裡加入](https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands)", inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
      
      await ctx.message.delete()

        


  

    
  @commands.command()
  async def level(self,ctx,start:int,end:int,remaining):
    if start>end:
      await ctx.send('你打反啦')
    else:
      
      result=int(ce[str(end)])-int(ce[str(start)])-int(remaining)
      if (result%3000)==0:
        need=result//3000
      else:
        need=(result//3000)+1
      await ctx.send(f'你還缺{result}經驗(艦艇研習數據T1 {need}本)才能到達等級{end}')

  @commands.command()
  async def 別名(self,ctx,evaluation):
    await ctx.send(f"{evaluation}：{chde1[evaluation]}")

  
  @commands.command()
  async def 數值(self,ctx,boat):
    if boat == str('女帝天尊'):
      await ctx.send("女帝天尊\n砲擊|=========  無限\n防空|=========  無限\n雷擊|=========  無限\n航空|=========  無限\n裝填|=========  無限\n機動|=                       69\n命中|=========  無限")

  @cog_ext.cog_slash(name="科研屬性加成",
  description="科研屬性加成艦船查詢",
  options=[create_option(name="屬性",
                       description="關於要查詢加成的屬性",
                       required=True,
                       option_type=3,
                       choices=[
                        create_choice(
                          name="耐久",
                          value="耐久"),
                         create_choice(
                          name="炮擊",
                          value="炮擊"),
                         create_choice(
                          name="雷擊",
                          value="雷擊"),
                         create_choice(
                          name="防空",
                          value="防空"),
                         create_choice(
                          name="航空",
                          value="航空"),
                         create_choice(
                          name="裝填",
                          value="裝填"),
                         create_choice(
                          name="機動",
                          value="機動"),
                         create_choice(
                          name="命中",
                          value="命中"),
                         create_choice(
                           name="反潛",
                           value="反潛"
                         )
                       ]),
          
          
            create_option(name="艦種",
                       description="關於要查詢加成的艦種",
                       required=True,
                       option_type=3,
                       choices=[
                        create_choice(
                          name="驅逐",
                          value="驅逐"),
                         create_choice(
                          name="輕巡",
                          value="輕巡"),
                         create_choice(
                          name="重巡",
                          value="重巡"),
                         create_choice(
                          name="超巡",
                          value="超巡"),
                         create_choice(
                          name="戰巡",
                          value="戰巡"),
                         create_choice(
                          name="戰列",
                          value="戰列"),
                         create_choice(
                          name="輕航",
                          value="輕航"),
                         create_choice(
                          name="正航",
                          value="正航"),
                         create_choice(
                           name="重砲",
                           value="重砲"),
                         create_choice(
                           name="維修",
                           value="維修"),
                         create_choice(
                           name="航戰",
                           value="航戰"),
                         create_choice(
                           name="潛艇",
                           value="潛艇"),
                         create_choice(
                           name="潛母",
                           value="潛母"),
                         create_choice(
                           name="運輸",
                           value="運輸")
                       ])
          
          ])



  async def 科研屬性加成(self,ctx,艦種,屬性):
    af={}
    i=0
    alen=0
    acon=1
    embed=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    embed1=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    embed2=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    embed3=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    embed4=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    embed5=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    embed6=discord.Embed(title='科研屬性查詢',timestamp=datetime.datetime.now())
    aembed=[embed,embed1,embed2,embed3,embed4,embed5,embed6]
    for key, value in azur_le['艦種'].items():
      value1=azur_le['120級(屬性加成)'][key]
      value2=azur_le['解鎖'][key]
      if 屬性 in value1 and 屬性 not in value2 and 艦種 in value1:
        af[key]=(f"120等時獲得：{value1}")
      elif 屬性 not in value1 and 屬性 in value2 and 艦種 in value2:
        af[key]=(f"解鎖時時獲得：{value2}")
      elif 屬性 in value1 and 屬性 in value2 and 艦種 in value1 and 艦種 in value2:
        af[key]=(f"解鎖時時獲得：{value2}|120等時獲得：{value1}")
    for key1, value1 in af.items():
      i+=1
      if i >= (25):
        i=0
        alen+=1
        acon+=1
        aembed[alen].add_field(name=key1,value=value1, inline=True)
      else:
        aembed[alen].add_field(name=key1,value=value1, inline=True)
    for ae in range(alen+1):
      aembed[ae].set_image(url="https://images-ext-2.discordapp.net/external/3MYCLFJvgmDzFtPXiDGrhaWViPkod1_97-sLPfwoeKU/https/c-ssl.duitang.com/uploads/item/202003/06/20200306130447_mfesu.thumb.1000_0.gif")

    contents = aembed
    pages = acon
    cur_page = 1
    message1=await ctx.send('未有人使用，此訊息將會在60秒後刪除')
    message = await ctx.send(embed= aembed[cur_page-1])
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=60 ,check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=contents[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=contents[cur_page-1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:      
            await message.delete()
            await message1.delete()
            break

  

def setup(bot):
    bot.add_cog(azur(bot))      






