from core.classes import Cog_Extension
import discord
import json
from discord import File
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord.ext import commands
from discord_slash.utils.manage_commands import create_choice,create_option
import asyncio
import random
import datetime




intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

slash = SlashCommand(bot, sync_commands=True)

with open("set.json",'r',encoding='utf8')as jfile:
  jdata=json.load(jfile)

with open("azur.json",'r',encoding='utf8')as azur1:
  azur=json.load(azur1)
with open("research.json",'r',encoding='utf8')as azur_r:
  cr=json.load(azur_r)
with open("azur_lane.json",'r',encoding='utf8')as azur_p:
  ca=json.load(azur_p)


class test(Cog_Extension):
  @commands.is_owner()
  @commands.command()
  async def test(self,ctx):
    embed1=discord.Embed(title="兌換",color=0xa3d3ff)
    embed1.add_field(name='a', value="a", inline=False)

    
    embed2=discord.Embed(title="測試翻頁", color=0xd09af4)
    embed2.add_field(name="這是測試頁", value="測試", inline=False)
    
      
    contents = [embed1, embed2]
    pages = 2
    cur_page = 1
    message = await ctx.send(embed=contents[cur_page-1])
    await ctx.message.delete()
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=5 ,check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

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
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the ;;first page
        except asyncio.TimeoutError:      
            await message.delete()
            break


  @cog_ext.cog_slash(name="help",
  description="關於機器人指令")



  async def _help(self,ctx):
    embed1=discord.Embed(title="能代姊姊的指令說明**()裡是參數說明**",color=0xa3d3ff)
    embed1.add_field(name="> 查詢艦船", value="$girl (艦船名稱)", inline=False)
    embed1.add_field(name="> 查詢科研", value="$科研", inline=False)
    embed1.add_field(name="> 查詢所需經驗", value="$level (目前的等級) (目標等級) (目前經驗)", inline=False)
    embed1.add_field(name="> 別名(舉例：海王星砲)", value="$別名 海王星砲", inline=False)
    embed1.add_field(name="> 跨群聊天", value="$設置跨群聊天 (要設置的頻道ID) \n $移除跨群聊天", inline=False)
    embed1.add_field(name="> 大世界", value="$大世界", inline=False)
    
    await ctx.send(embed=embed1)



def setup(bot):
  bot.add_cog(test(bot))      
