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
    Interaction,
)

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


    if (pronoun in ce1) and (pronoun in azur_le['解鎖']):
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      embed.add_field(name='艦種',value=azur_le['艦種'][pronoun], inline=True )
      embed.add_field(name='陣營',value=azur_le['陣營'][pronoun], inline=True )
      
      embed.add_field(name="科研點", value=f"●獲得：{str(azur_le['獲得'][pronoun])}●滿星：{str(azur_le['滿星'][pronoun])}●LV.120：{str(azur_le['Lv.120'][pronoun])}●總和：{str(azur_le['合計'][pronoun])}", inline=False)
      
      embed.add_field(name="科研屬性加成", value=f"●獲得：{str(azur_le['解鎖'][pronoun])}●LV.120：{str(azur_le['120級(屬性加成)'][pronoun])}", inline=False)
      
      embed.add_field(name="海事局連結", value=lane[pronoun], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands", inline=False)
      embed.add_field(name="評價", value=ce1[pronoun], inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
      await ctx.message.delete()
    elif (pronoun in ce1) and (pronoun not in azur_le['解鎖']):
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      
      embed.add_field(name="海事局連結", value=lane[pronoun], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands", inline=False)
      embed.add_field(name="評價", value=ce1[pronoun], inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
    elif (pronoun not in ce1) and (pronoun not in azur_le['解鎖']):
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      
      embed.add_field(name="海事局連結", value=lane[pronoun], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands", inline=False)
      embed.set_image(url=ca[pronoun])
      embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title=(pronoun), url=lane[pronoun],timestamp=datetime.datetime.now())
      embed.add_field(name='艦種',value=azur_le['艦種'][pronoun], inline=True )
      embed.add_field(name='陣營',value=azur_le['陣營'][pronoun], inline=True )
      
      embed.add_field(name="科研點", value=f"●獲得：{str(azur_le['獲得'][pronoun])}●滿星：{str(azur_le['滿星'][pronoun])}●LV.120：{str(azur_le['Lv.120'][pronoun])}●總和：{str(azur_le['合計'][pronoun])}", inline=False)
      
      embed.add_field(name="科研屬性加成", value=f"●獲得：{str(azur_le['解鎖'][pronoun])}●LV.120：{str(azur_le['120級(屬性加成)'][pronoun])}", inline=False)
      
      embed.add_field(name="海事局連結", value=lane[pronoun], inline=False)
      embed.add_field(name="邀請機器人加入你的群組", value="https://discord.com/api/oauth2/authorize?client_id=886827609005129799&permissions=8&scope=bot%20applications.commands", inline=False)
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
    polic=alias[boat]
    tmp1 = jdata[polic][1].split("→")
    tmp2 = jdata[polic][3].split("→")
    tmp3 = jdata[polic][5].split("→")
    tmp5 = jdata[polic][9].split("→")
    tmp6 = jdata[polic][11].split("→")
    tmp7 = jdata[polic][13].split("→")
    tmp8 = jdata[polic][15].split("→")
    tmp9 = jdata[polic][17].split("→")

    if len(tmp1)==2: 
      bar_color= "#ff9933"
      profile = await load_image_async(str(ca[boat]))
      profile = Editor(profile).resize((231, 273))
      poppins = Font.poppins(size=24)  
      text_color='#000000'
      bar_color = "#ff9933"
      background = Editor("image0.jpg")
      background.paste(profile.image, (0, 0))
      background.bar(
          (177, 305),
          max_width=731,
          height=47,
          percentage=(int(tmp2[1])/4.37),
          fill=bar_color,
      )
      background.bar(
          (177, 523),
          max_width=731,
          height=47,
          percentage=(int(tmp3[1])/5.68),
          fill=bar_color,
      )
      background.bar(
          (177, 723),
          max_width=731,
          height=47,
          percentage=(int(tmp5[1])/6.09),
          fill=bar_color,
      )
      background.bar(
          (177, 937),
          max_width=731,
          height=47,
          percentage=(int(tmp6[1])/4.62),
          fill=bar_color,
      )
      background.bar(
          (177, 1143),
          max_width=731,
          height=47,
          percentage=(int(tmp7[1])/2.34),
          fill=bar_color,
      )
      background.bar(
          (177, 1357),
          max_width=731,
          height=47,
          percentage=(int(tmp8[1])/3.15),
          fill=bar_color,
      )
      background.bar(
          (177, 1573),
          max_width=731,
          height=47,
          percentage=(int(tmp9[1])/2.35),
          fill=bar_color,
      )    
      background.text((1435, 305), str(tmp2[1]), font=poppins, color=text_color)
      background.text((1435, 523), str(tmp3[1]), font=poppins, color=text_color)
      background.text((1435, 723), str(tmp5[1]), font=poppins, color=text_color)
      background.text((1435, 937), str(tmp6[1]), font=poppins, color=text_color)
      background.text((1435, 1143), str(tmp7[1]), font=poppins, color=text_color)
      background.text((1435, 1357), str(tmp8[1]), font=poppins, color=text_color)
      background.text((1435, 1573), str(tmp9[1]), font=poppins, color=text_color)
      card = File(fp=background.image_bytes, filename="image.png")
      await ctx.send(file=card)
    if len(tmp1)==1:
      bar_color= "#ff9933"
      profile = await load_image_async(str(ca[boat]))
      profile = Editor(profile).resize((231, 273))
      poppins = Font.poppins(size=24)  
      text_color='#000000'
      bar_color = "#ff9933"
      background = Editor("image0.jpg")
      background.paste(profile.image, (0, 0))
      background.bar(
          (177, 305),
          max_width=731,
          height=47,
          percentage=(int(tmp2[0])/4.37),
          fill=bar_color,
      )
      background.bar(
          (177, 523),
          max_width=731,
          height=47,
          percentage=(int(tmp3[0])/5.68),
          fill=bar_color,
      )
      background.bar(
          (177, 723),
          max_width=731,
          height=47,
          percentage=(int(tmp5[0])/6.09),
          fill=bar_color,
      )
      background.bar(
          (177, 937),
          max_width=731,
          height=47,
          percentage=(int(tmp6[0])/4.62),
          fill=bar_color,
      )
      background.bar(
          (177, 1143),
          max_width=731,
          height=47,
          percentage=(int(tmp7[0])/2.34),
          fill=bar_color,
      )
      background.bar(
          (177, 1357),
          max_width=731,
          height=47,
          percentage=(int(tmp8[0])/3.15),
          fill=bar_color,
      )
      background.bar(
          (177, 1573),
          max_width=731,
          height=47,
          percentage=(int(tmp9[0])/2.35),
          fill=bar_color,
      )    
      background.text((1435, 305), str(tmp2[0]), font=poppins, color=text_color)
      background.text((1435, 523), str(tmp3[0]), font=poppins, color=text_color)
      background.text((1435, 723), str(tmp5[0]), font=poppins, color=text_color)
      background.text((1435, 937), str(tmp6[0]), font=poppins, color=text_color)
      background.text((1435, 1143), str(tmp7[0]), font=poppins, color=text_color)
      background.text((1435, 1357), str(tmp8[0]), font=poppins, color=text_color)
      background.text((1435, 1573), str(tmp9[0]), font=poppins, color=text_color)
      card = File(fp=background.image_bytes, filename="image.png")
      await ctx.send(file=card)

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



  async def _科研屬性加成(self,ctx,艦種,屬性):
    embed3=discord.Embed(title='科研屬性查詢', url='https://wiki.biligame.com/blhx/%E8%88%B0%E9%98%9F%E7%A7%91%E6%8A%80',timestamp=datetime.datetime.now())
    for key, value in azur_le['艦種'].items():
      value1=azur_le['120級(屬性加成)'][key]
      value2=azur_le['解鎖'][key]
      if 屬性 in value1 and 屬性 not in value2 and 艦種 in value1:

        embed3.add_field(name=key, value=f"120等時獲得：{value1}", inline=False)
      elif 屬性 not in value1 and 屬性 in value2 and 艦種 in value2:

        embed3.add_field(name=key, value=f"解鎖時時獲得：{value2}", inline=False)
      elif 屬性 in value1 and 屬性 in value2 and 艦種 in value1 and 艦種 in value2:

        embed3.add_field(name=key, value=f"解鎖時時獲得：{value2}|120等時獲得：{value1}", inline=False)
      elif 屬性 not in value1 and 屬性 not in value2 and 艦種 not in value1 and 艦種 not in value2:
        embed3.set_image(url='https://c-ssl.duitang.com/uploads/item/202003/06/20200306130447_mfesu.thumb.1000_0.gif')
    embed3.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")

    await ctx.send(embed=embed3)

  

def setup(bot):
    bot.add_cog(azur(bot))      






