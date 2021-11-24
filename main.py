#導入Discord.py
import discord
import json
import os
import keep_alive
from discord import Embed
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice,create_option




intents = discord.Intents.all()



with open("set.json", 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
#client是我們與Discord連結的橋樑
bot = commands.Bot(command_prefix='$', intents=intents)

slash = SlashCommand(bot, sync_commands=True)

bot.remove_command('help')



#調用event函式庫
#調用event函式庫



@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)
    game = discord.Game('誰又冰我')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)



@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'導入{extension}成功')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'導出{extension}成功')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重製{extension}成功')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')








if __name__ == "__main__":

    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])  #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
