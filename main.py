#導入Discord.py
import discord
import json
import os
import keep_alive
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_components import Button, Select, SelectOption, ComponentsBot

intents = discord.Intents.all()

with open("set.json", 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
#client是我們與Discord連結的橋樑
bot = ComponentsBot("$", intents=intents)

slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help')


@bot.command()
#調用event函式庫
#調用event函式庫

@bot.event
#當機器人完成啟動時
async def on_ready():
    print(bot.user)
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"{len(bot.guilds)} 正在冰我"))


bot.application_info()


@commands.is_owner()
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'導入{extension}成功')


@commands.is_owner()
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'導出{extension}成功')


@commands.is_owner()
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重製{extension}成功')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":

    keep_alive.keep_alive()
    bot.run('ODg2ODI3NjA5MDA1MTI5Nzk5.GkbE1-.lPyGeQ_W-tOmCVyJWbrhDBefkcWsyzrwIOtyGo')
