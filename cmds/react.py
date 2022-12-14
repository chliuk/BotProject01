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

#åé«æ°        
    @commands.command()
    async def dialga_raid(self, ctx, number):
        raidemoji = ["ðï¸", "â"]
        embed=discord.Embed(title=ctx.message.author.name+'çåæ°æ¿ï¼æ'+str(number)+"å ´ï¼", color=0xdc0909)
        embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/8/8a/483Dialga.png/600px-483Dialga.png")
        embed.add_field(name="é ­ç®è³è¨", value="ð¸å¸çç§å¡\nð¸å±¬æ§ï¼é¼ï¼é¾\nð¸äºæåé«æ°\nð¸æ¥µéå©äººãå»ºè­°åå°äºäººéæ", inline=False)
        embed.add_field(name="åå æåæ¶åé«æ°", value="éä¸»æäººï¼\nðæè¦+1\nä¸»æäººï¼\nâåæ¶ä¸»æ\nðå³å»éå", inline=False)
        message = await ctx.send(embed=embed)
    
        for emoji in raidemoji:
          await message.add_reaction(emoji)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, id=998750831002255430)
        room = await ctx.guild.create_text_channel(name=ctx.message.author.name+'çåæ°æ¿', overwrites=overwrites, category=category)
        room_id=room.id
        role = await ctx.guild.create_role(name = str(room_id))
        await room.set_permissions(role, read_messages=True)

        room_embed=discord.Embed(title=ctx.message.author.name+'çåæ°æ¿ï¼æ'+str(number)+"å ´ï¼", color=0x885dfd)
        room_embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/8/8a/483Dialga.png/600px-483Dialga.png")
        room_embed.add_field(name="é ­ç®è³è¨",value="ð¸å¸çç§å¡\nð¸å±¬æ§ï¼é¼ï¼é¾\nð¸20/25ç­æå¤§CP2307/2884\nð¸å¯ç¨æ ¼é¬¥ãå°é¢ç³»å¯¶å¯å¤¢ææ°\nð¸æ¨è¦ææï¼è·¯å¡å©æ­ãä¿®å»ºèå°ãé¾é ­å°é¼ ãåºæå¤ãæªåãåå°é²", inline=False)
        room_embed.add_field(name="çµæåé«æ°",value="ç¾¤çµå§ä»»ä¸äººè¼¸å¥""[deletechannel""å³å¯ééæ­¤ç¾¤çµ")
        await room.send(embed=room_embed)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["ðï¸", "â"]

        count = 5

        try:
            while count>0:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == "ðï¸":
                    count-=1
                    guild = self.bot.get_guild(ctx.guild.id)
                    rolee = guild.get_role(role.id)
                    users = await reaction.users().flatten()
                    for use in users:
                        await use.add_roles(rolee)

                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}ä¸»ææå")

                elif str(reaction.emoji) == "â":
                    count-=5
                    await room.delete()
                    await role.delete()
                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}åæ¶äºåé«æ°")

            if count == 0:
                guild = self.bot.get_guild(ctx.guild.id)
                rolee = guild.get_role(role.id)
                users = await reaction.users().flatten()
                for use in users:
                    await use.add_roles(rolee)

                await message.delete()
                await ctx.message.delete()
                await ctx.send(f"{user}ä¸»ææå")
               
        except:
            pass

#ç¶é©å
    @commands.command()
    async def EXP(self, ctx, number):
        raidemoji = ["ðï¸", "â"]
        embed=discord.Embed(title=ctx.message.author.name+'ç'+str(number)+'äººç¶é©å', color=0x4dff00)
        embed.set_thumbnail(url="https://media.52poke.com/wiki/b/bb/870Falinks.png")
        embed.add_field(name="åå æåæ¶ç¶é©å", value="éä¸»æäººï¼\nðæè¦+1\nä¸»æäººï¼\nâåæ¶ä¸»æ\nðå³å»éå", inline=False)
        message = await ctx.send(embed=embed)
    
        for emoji in raidemoji:
          await message.add_reaction(emoji)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, id=998750831002255430)
        room = await ctx.guild.create_text_channel(name=ctx.message.author.name+'ç'+str(number)+'äººç¶é©å', overwrites=overwrites, category=category)
        room_id=room.id
        role = await ctx.guild.create_role(name = str(room_id))
        await room.set_permissions(role, read_messages=True)

        room_embed=discord.Embed(title=ctx.message.author.name+'ç'+str(number)+'äººç¶é©å', color=0x4dff00)
        room_embed.set_thumbnail(url="https://media.52poke.com/wiki/b/bb/870Falinks.png")
        room_embed.add_field(name="çµæç¶é©å",value="ç¾¤çµå§ä»»ä¸äººè¼¸å¥""[deletechannel""å³å¯ééæ­¤ç¾¤çµ")
        await room.send(embed=room_embed)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["ðï¸", "â"]

        count = 30

        try:
            while count>0:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == "ðï¸":
                    count-=1
                    guild = self.bot.get_guild(ctx.guild.id)
                    rolee = guild.get_role(role.id)
                    users = await reaction.users().flatten()
                    for use in users:
                        await use.add_roles(rolee)

                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}ä¸»ææå")

                elif str(reaction.emoji) == "â":
                    count-=30
                    await room.delete()
                    await role.delete()
                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}åæ¶äºç¶é©å")

            if count == 0:
                guild = self.bot.get_guild(ctx.guild.id)
                rolee = guild.get_role(role.id)
                users = await reaction.users().flatten()
                for use in users:
                    await use.add_roles(rolee)

                await message.delete()
                await ctx.message.delete()
                await ctx.send(f"{user}ä¸»ææå")
               
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
        await ctx.send(f'è¨ç·´å®¶{userr.mention}çç¶é©å¼ï¼')
        await ctx.send(file=card)
        print('4567')
        

async def setup(bot):
    await bot.add_cog(React(bot))