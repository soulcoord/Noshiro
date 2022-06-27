import json
import discord
import datetime
from random import randint
from discord.ext import commands


class GlobalChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def 設置跨群聊天(self, ctx, channel):
        guildss=[]
        guild_id = ctx.message.guild.id
        guilds_id=ctx.guild.text_channels
        for guilds in guilds_id:
          guildss.append(guilds.id)

        channel_id = int(channel.strip('<>#'))

        with open('global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)

            # Existing global chat
            if new_global_chat in global_chat_data:
                globalname=self.bot.get_channel(global_chat_data[new_global_chat])
                await ctx.send(f':no_entry: 本伺服器已加入過跨群聊天! 此伺服器跨群頻道為`{str(globalname)}`')
            elif channel_id not in guildss:
              await ctx.send(f'此頻道ID不屬於此伺服器')

            # Add new global chat
            else:
                global_chat_data[new_global_chat] = channel_id
                globalname=self.bot.get_channel(channel_id)
                with open('global_chat.json', 'w') as new_global_chat:
                    json.dump(global_chat_data, new_global_chat, indent=4)

                await ctx.send(f':white_check_mark: 本伺服器`{str(globalname)}`已成功加入跨群聊天!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def 移除跨群聊天(self, ctx):
        guild_id = ctx.message.guild.id

        with open('global_chat.json', 'r') as file:
            global_chat_data = json.load(file)

        global_chat_data.pop(str(guild_id))

        # Update global chat
        with open('global_chat.json', 'w') as update_global_chat_file:
            json.dump(global_chat_data, update_global_chat_file, indent=4)

        await ctx.send(':white_check_mark: **頻道已從跨群聊天中刪除!**')

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith('$'):
                with open('global_chat.json', 'r') as file:
                    global_chat_data = json.load(file)

                channel_id = list(global_chat_data.values())

                # Message sender
                if message.channel.id in channel_id:
  
                  # Unsupported message content
                  if not message.content:
                      return
  
                  # Message receiver
                  for ids in channel_id:
                    if message.channel.id != ids:
                        message_embed = discord.Embed(colour=randint(0, 0xffffff))

                        message_embed.timestamp = datetime.datetime.utcnow()
                        message_embed.set_author(icon_url=message.author.avatar_url, name=f'{message.author}')
                        if 'https://' not in message.content:
                          message_embed.description = f'**{message.content}**'
                        elif 'https://' in message.content:
                          message_embed.set_image(url=message.content)
                        message_embed.set_footer(icon_url=message.guild.icon_url, text=message.guild.name)

                        await self.bot.get_channel(ids).send(embed=message_embed)


def setup(bot):
    bot.add_cog(GlobalChat(bot))