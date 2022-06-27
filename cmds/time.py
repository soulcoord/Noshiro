import discord
from discord.ext import commands
import datetime,asyncio
from core.classes import Cog_Extension

class time(Cog_Extension):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.coe=0
    async def interval():
      await self.bot.wait_until_ready()
      self.channel=self.bot.get_channel(887530340384669728)

      while not self.bot.is_closed():

        now_times=datetime.datetime.now().strftime('%H%M')
        if now_times == ('0803')and self.coe == 0:
          await self.channel.send('loli')
          self.coe=1
          await asyncio.sleep(1)

        else:
          await asyncio.sleep(1)
    self.bg_task=self.bot.loop.create_task(interval())









def setup(bot):
  bot.add_cog(time(bot))