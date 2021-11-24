from core.classes import Cog_Extension
import discord
import json
from discord.ext import commands
a=0


with open("set.json",'r',encoding='utf8')as jfile:
  jdata=json.load(jfile)
class event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self,msg):

        if msg.content == '莉莉'and msg.author!=self.bot.user:
            await msg.channel.send('<:bump:890447738859311124>')

        if msg.content=='史黛拉':
          await msg.add_reaction('<:__:892414119112753152>')
        
        if msg.content.startswith('說'):
            #分割訊息成兩份
          tmp = msg.content.split(" ",2)
          #如果分割後串列長度只有1
          if len(tmp) == 1:
            await msg.channel.send("你要我說什麼啦？")
          else:
            await msg.channel.send(tmp[1])

        if msg.content.startswith('更改狀態'):
              #切兩刀訊息
          tmp = msg.content.split(" ",2)
          #如果分割後串列長度只有1
          if len(tmp) == 1:
              await msg.channel.send("你要改成什麼啦？")
          else:
              games=discord.Game(tmp[1])
              await self.bot.change_presence(activity=games)

        if msg.author.id==366574612449853460:
          await msg.add_reaction('<:__:892414119112753152>')
        if msg.content == '能代姊姊說愛我' and msg.author!=self.bot.user:
          if msg.author.nick is not None :
            await msg.channel.send(f'{msg.author.nick}我也愛你')
          else:
            await msg.channel.send(f'{msg.author.name}我也愛你')

        
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
      if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("參數錯誤")
      if isinstance(error,commands.errors.CommandNotFound):
        await ctx.send("沒這指令啦！")
    


    
    



def setup(bot):
    bot.add_cog(event(bot))