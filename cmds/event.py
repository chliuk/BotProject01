from http import client
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime
from discord.utils import get


with open('/DiscordBot/BotProject01/setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'歡迎 {member} 加入～')
        embed=discord.Embed(title="", url="https://media.52poke.com/wiki/thumb/a/a9/061Poliwhirl.png/600px-061Poliwhirl.png", description="哈囉～歡迎來到傻豆的DC群，這裡是供Pokemon Go玩家討論遊戲的平台，請詳閱討論串了解本平台的各項功能。", color=0x759ef0, timestamp= datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/4/4b/580Ducklett.png/600px-580Ducklett.png")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self,message):
        if message != '[rank':
            async def updata_data(users, user):
                if not f'{user.id}' in users:
                    users[f'{user.id}'] = {}
                    users[f'{user.id}']['experience'] = 0
                    users[f'{user.id}']['level'] = 1

            async def add_experience(users, user, exp):
                users[f'{user.id}']['experience'] += exp

            async def level_up(users, user, channel):
                experience = users[f'{user.id}']['experience']
                lvl_start = users[f'{user.id}']['level']
                lvl_end = int((((experience-5)/22) ** (1/2)) + 1)

                if lvl_start < lvl_end:
                    await channel.send(f'訓練家{user.mention}等級提升至level {lvl_end}')
                    users[f'{user.id}']['level'] = lvl_end
                    if lvl_end == 2:
                        guild = user.guild
                        role = guild.get_role(1009329967601029141)
                        await user.add_roles(role)
                        await channel.send(f'訓練家{user.mention}抓到{role.name}了！')
        
                    if lvl_end == 4:
                        guild = user.guild
                        old_role = guild.get_role(1009329967601029141)
                        new_role = guild.get_role(1009330681580625963)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 6:
                        guild = user.guild
                        old_role = guild.get_role(1009330681580625963)
                        new_role = guild.get_role(1009330771762348074)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 8:
                        guild = user.guild
                        old_role = guild.get_role(1009330771762348074)
                        new_role = guild.get_role(1009330837407416320)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 10:
                        guild = user.guild
                        old_role = guild.get_role(1009330837407416320)
                        new_role = guild.get_role(1009330891333570560)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 12:
                        guild = user.guild
                        old_role = guild.get_role(1009330891333570560)
                        new_role = guild.get_role(1009330971021160530)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 14:
                        guild = user.guild
                        old_role = guild.get_role(1009330971021160530)
                        new_role = guild.get_role(1009331015363330068)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 16:
                        guild = user.guild
                        old_role = guild.get_role(1009331015363330068)
                        new_role = guild.get_role(1009331082103095346)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 18:
                        guild = user.guild
                        old_role = guild.get_role(1009331082103095346)
                        new_role = guild.get_role(1009331122649436230)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 19:
                        guild = user.guild
                        old_role = guild.get_role(1009331122649436230)
                        new_role = guild.get_role(1009331261292154990)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')

                    if lvl_end == 20:
                        guild = user.guild
                        old_role = guild.get_role(1009331261292154990)
                        new_role = guild.get_role(1009331323258814495)
                        await user.remove_roles(old_role)
                        await user.add_roles(new_role)
                        await channel.send(f'訓練家{user.mention}抓到{new_role.name}了！')
        
            if message.author.bot == False:
                with open('D:\DiscordBot\BotProject01\setting.json', 'r') as f:
                    users = json.load(f)

                await updata_data(users, message.author)
                await add_experience(users, message.author, 5)
                await level_up(users, message.author, message.channel)

                with open('D:\DiscordBot\BotProject01\setting.json', 'w') as f:
                    json.dump(users, f)

        else:
            await self.bot.process_commands(message)

        

async def setup(bot):
    await bot.add_cog(Event(bot))