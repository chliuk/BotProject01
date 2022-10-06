import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord.utils import get
from typing import Optional
from easy_pil import Editor, load_image_async, Font

with open('/DiscordBot/BotProject01/setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def picture(self, ctx):
       pic = discord.File(jdata['pic'])
       await ctx.send(file = pic)

#團體戰        
    @commands.command()
    async def dialga_raid(self, ctx, number):
        raidemoji = ["🖐️", "❌"]
        embed=discord.Embed(title=ctx.message.author.name+'的團戰房（打'+str(number)+"場）", color=0xdc0909)
        embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/8/8a/483Dialga.png/600px-483Dialga.png")
        embed.add_field(name="頭目資訊", value="🔸帝牙盧卡\n🔸屬性：鋼＋龍\n🔸五星團體戰\n🔸極限兩人、建議四到五人開打", inline=False)
        embed.add_field(name="參加或取消團體戰", value="非主持人：\n🖐我要+1\n主持人：\n❌取消主持\n🖐即刻開團", inline=False)
        message = await ctx.send(embed=embed)
    
        for emoji in raidemoji:
          await message.add_reaction(emoji)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, id=998750831002255430)
        room = await ctx.guild.create_text_channel(name=ctx.message.author.name+'的團戰房', overwrites=overwrites, category=category)
        room_id=room.id
        role = await ctx.guild.create_role(name = str(room_id))
        await room.set_permissions(role, read_messages=True)

        room_embed=discord.Embed(title=ctx.message.author.name+'的團戰房（打'+str(number)+"場）", color=0x885dfd)
        room_embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/8/8a/483Dialga.png/600px-483Dialga.png")
        room_embed.add_field(name="頭目資訊",value="🔸帝牙盧卡\n🔸屬性：鋼＋龍\n🔸20/25等最大CP2307/2884\n🔸可用格鬥、地面系寶可夢應戰\n🔸推薦打手：路卡利歐、修建老將、龍頭地鼠、固拉多、怪力、土地雲", inline=False)
        room_embed.add_field(name="結束團體戰",value="群組內任一人輸入""[deletechannel""即可關閉此群組")
        await room.send(embed=room_embed)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["🖐️", "❌"]

        count = 5

        try:
            while count>0:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == "🖐️":
                    count-=1
                    guild = self.bot.get_guild(ctx.guild.id)
                    rolee = guild.get_role(role.id)
                    users = await reaction.users().flatten()
                    for use in users:
                        await use.add_roles(rolee)

                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}主持成功")

                elif str(reaction.emoji) == "❌":
                    count-=5
                    await room.delete()
                    await role.delete()
                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}取消了團體戰")

            if count == 0:
                guild = self.bot.get_guild(ctx.guild.id)
                rolee = guild.get_role(role.id)
                users = await reaction.users().flatten()
                for use in users:
                    await use.add_roles(rolee)

                await message.delete()
                await ctx.message.delete()
                await ctx.send(f"{user}主持成功")
               
        except:
            pass

#經驗團
    @commands.command()
    async def EXP(self, ctx, number):
        raidemoji = ["🖐️", "❌"]
        embed=discord.Embed(title=ctx.message.author.name+'的'+str(number)+'人經驗團', color=0x4dff00)
        embed.set_thumbnail(url="https://media.52poke.com/wiki/b/bb/870Falinks.png")
        embed.add_field(name="參加或取消經驗團", value="非主持人：\n🖐我要+1\n主持人：\n❌取消主持\n🖐即刻開團", inline=False)
        message = await ctx.send(embed=embed)
    
        for emoji in raidemoji:
          await message.add_reaction(emoji)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, id=998750831002255430)
        room = await ctx.guild.create_text_channel(name=ctx.message.author.name+'的'+str(number)+'人經驗團', overwrites=overwrites, category=category)
        room_id=room.id
        role = await ctx.guild.create_role(name = str(room_id))
        await room.set_permissions(role, read_messages=True)

        room_embed=discord.Embed(title=ctx.message.author.name+'的'+str(number)+'人經驗團', color=0x4dff00)
        room_embed.set_thumbnail(url="https://media.52poke.com/wiki/b/bb/870Falinks.png")
        room_embed.add_field(name="結束經驗團",value="群組內任一人輸入""[deletechannel""即可關閉此群組")
        await room.send(embed=room_embed)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["🖐️", "❌"]

        count = 30

        try:
            while count>0:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == "🖐️":
                    count-=1
                    guild = self.bot.get_guild(ctx.guild.id)
                    rolee = guild.get_role(role.id)
                    users = await reaction.users().flatten()
                    for use in users:
                        await use.add_roles(rolee)

                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}主持成功")

                elif str(reaction.emoji) == "❌":
                    count-=30
                    await room.delete()
                    await role.delete()
                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}取消了經驗團")

            if count == 0:
                guild = self.bot.get_guild(ctx.guild.id)
                rolee = guild.get_role(role.id)
                users = await reaction.users().flatten()
                for use in users:
                    await use.add_roles(rolee)

                await message.delete()
                await ctx.message.delete()
                await ctx.send(f"{user}主持成功")
               
        except:
            pass

    @commands.command()
    async def deletechannel(self, ctx):
        await ctx.channel.delete()
        role = ctx.channel.id
        for del_role in ctx.guild.roles:
            if del_role.name == f'{role}':
               await del_role.delete()

    @commands.command()
    async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
        userr = user or ctx.author

        print('123')

        with open("/DiscordBot/BotProject01/setting.json", "r") as f:
          data = json.load(f)

        print('45')

        xp = data[str(userr.id)]["experience"]
        lvl = data[str(userr.id)]["level"]
        print('67')
        next_level_xp = 22 * ((lvl) ** 2) + 5
        xp_need = next_level_xp
        xp_have = data[str(userr.id)]["experience"]

        percentage = int(((xp_have * 100)/ xp_need))

        if percentage < 1:
          percentage = 0
        print('89')
        ## Rank card
        background = Editor(data['zIMAGE02'])
        profile = await load_image_async(str(userr.display_avatar.url))
        print('45')
        profile = Editor(profile).resize((200, 200)).circle_image()
        print('46')
        poppins = Font.poppins(size=40)
        poppins_small = Font.poppins(size=45)
        print('10')
        #you can skip this part, I'm adding this because the text is difficult to read in my selected image
        ima = Editor(data['zBLACK'])
        background.blend(image=ima, alpha=.5, on_top=False)

        background.paste(profile.image, (20, 50))

        background.rectangle((250, 175), width=590, height=40, fill="#fff", radius=20)
        background.bar(
            (245, 175),
            max_width=590,
            height=40,
            percentage=percentage,
            fill="#ff9933",
            radius=20,
        )
       # background.text((200, 40), f'{userr.name}', font=poppins, color="#ff9933")
        print('11')
        #background.rectangle((200, 100), width=350, height=2, fill="#ff9933")
        background.text(
            (250, 75),
            f"Level : {lvl}   "
            + f" XP : {xp} / {22 * ((lvl) ** 2) + 5}",
            font=poppins_small,
            color="#ff9933",
        )

        card = discord.File(fp=background.image_bytes, filename=data['zCARD'])
        await ctx.send(f'訓練家{userr.mention}的經驗值：')
        await ctx.send(file=card)
        print('4567')
        

async def setup(bot):
    await bot.add_cog(React(bot))