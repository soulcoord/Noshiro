from asyncio.tasks import sleep
from core.classes import Cog_Extension
import discord
import json,asyncio,datetime
from discord.ext import commands

class task(Cog_Extension):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.counter=0
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(891665244311666710)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now().strftime('%H%M')
                with open("set.json",'r',encoding='utf8')as jfile:
                    jdata=json.load(jfile)
                if now_time==jdata['time']and self.counter==0:
                    await self.channel.send('女帝不可以色色')
                    await self.channel.send('一天一魚雷，女帝遠離我')
                    await self.channel.send('我討厭女帝就跟我討厭胡蜂、大黃蜂一樣，所以裡我遠一點')
                    await self.channel.send('女帝不要')
                    self.counter=1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task=self.bot.loop.create_task(time_task())
        
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel=self.channel=self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')
    @commands.command()
    async def set_time(self,ctx,time):
        self.counter=0
        with open("set.json",'r',encoding='utf8')as jfile:
            jdata=json.load(jfile)
        jdata['time']=time
        with open("set.json",'w',encoding='utf8')as jfile:
            json.dump(jdata,jfile,indent=4)



def setup(bot):
    bot.add_cog(task(bot))