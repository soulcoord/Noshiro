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
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def 公告(self,ctx):
      embed=discord.Embed(title="```置頂公告```", color=0xffff78)
      embed.add_field(name='> 如何解鎖頻道', value="歡迎各位新朋友加入 開心農場 請先去領取身分組才能解鎖大多數頻道", inline=False)
      embed.add_field(name='> 注意事項', value="本群將會定時清理低活躍度的成員，所謂的低活躍是指 未參加本群聊天或語音通話", inline=False)
      embed.add_field(name='> 群組規則', value="若在本群遇到什麼問題請跟管理員講 ，勿在群組起糾紛，若管理員無法解決那~~可以考慮走法律途徑~~", inline=False)

      await ctx.send(embed=embed)



    





    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clean(self,ctx,num:int):
      await ctx.channel.purge(limit=num+1)

      

   
def setup(bot):
    bot.add_cog(mes(bot))
