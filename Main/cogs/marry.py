import disnake
from disnake.ext import commands
import sqlite3

class Marry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = sqlite3.connect("server.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS loverum(
                    id1 INT,
                    id2 INT,
                    name1 TEXT,
                    name2 TEXT,
                    namelovrum TEXT,
                    cash INT,
                    voice_hours INT,
                    voice_minutes INT,
                    voice_seconds INT
                       
                    )""")
        self.connection.commit()

    @commands.slash_command(name="marry", description="Предложение пожениться")
    async def marry(self, ctx, member: disnake.Member):

        # Проверка, есть ли у автора или упомянутого пользователя уже пара
        id1 = self.cursor.execute("SELECT id1 FROM loverum WHERE id1 = ? OR id2 = ?", (ctx.author.id, ctx.author.id)).fetchone()
        id2 = self.cursor.execute("SELECT id2 FROM loverum WHERE id1 = ? OR id2 = ?", (ctx.author.id, ctx.author.id)).fetchone()
        
        if id1 or id2:
            embed = disnake.Embed(
                title="Женитьба",
                description="У вас уже есть пара"
            )
            await ctx.send(embed=embed, ephemeral=True)
        else:
            id1 = self.cursor.execute("SELECT id1 FROM loverum WHERE id1 = ? OR id2 = ?", (member.id, member.id)).fetchone()
            id2 = self.cursor.execute("SELECT id2 FROM loverum WHERE id1 = ? OR id2 = ?", (member.id, member.id)).fetchone()
            
            if id1 or id2:
                embed = disnake.Embed(
                    title="Женитьба",
                    description=f"У {member.mention} уже есть пара"
                )
                await ctx.send(embed=embed, ephemeral=True)
            else:
                men = ctx.author
                cym = 1000
                bal = self.cursor.execute("SELECT cash FROM users WHERE id = ?", (ctx.author.id,)).fetchone()
                
                if bal is None or (bal and bal[0] < cym):
                    capital = cym - (bal[0] if bal else 0)
                    await ctx.send(f"Вам не хватает {capital} :coin:", ephemeral=True)
                else:
                    self.cursor.execute("UPDATE users SET cash = cash - ? WHERE id = ?", (cym, ctx.author.id))
                    self.connection.commit()

                    class Answer(disnake.ui.View):
                        def __init__(self, cursor):
                            super().__init__()
                            self.cursor = cursor
                            self.value = None

                        @disnake.ui.button(label="Согласиться", style=disnake.ButtonStyle.green)
                        async def yes(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
                            self.cursor.execute("INSERT INTO loverum (id1, id2, name1, name2, cash,voice_hours ,voice_minutes ,voice_seconds) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                                (men.id, member.id, men.name, member.name, 0,0,0,0))
                            self.cursor.connection.commit()

                            loverole = disnake.utils.get(member.guild.roles, id=1195782177800065164)
                            await member.add_roles(loverole)
                            await men.add_roles(loverole)

                            embed = disnake.Embed(
                                title="Согласие",
                                description=f"Вы согласились пожениться с {men.mention}"
                            )
                            await member.send(embed=embed)

                            embed = disnake.Embed(
                                title="Согласие",
                                description=f"{member.mention} согласился(лась) пожениться"
                            )
                            await men.send(embed=embed)

                            self.value = True
                            self.stop()

                        @disnake.ui.button(label="Отказаться", style=disnake.ButtonStyle.red)
                        async def no(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
                            self.cursor.execute("UPDATE users SET cash = cash + ? WHERE id = ?", (cym, men.id))
                            self.cursor.connection.commit()

                            embed = disnake.Embed(
                                title="Отказ",
                                description=f"Вы отказались пожениться с {men.mention}"
                            )
                            await member.send(embed=embed)

                            embed = disnake.Embed(
                                title="Отказ",
                                description=f"{member.mention} отказался(лась) жениться"
                            )
                            await men.send(embed=embed)

                            self.value = False
                            self.stop()

                    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
                    embed = disnake.Embed(
                        title="Предложение пожениться",
                        description=f"Вы предложили пожениться {member.mention}"
                    )
                    embed.set_thumbnail(url=avatar_url)
                    await ctx.send(embed=embed)

                    avatar_url = men.avatar.url if men.avatar else men.default_avatar.url
                    embed = disnake.Embed(
                        title="Предложение пожениться",
                        description=f"{men.mention} предложил вам пожениться"
                    )
                    embed.set_thumbnail(url=avatar_url)
                    await member.send(embed=embed, view=Answer(self.cursor))
                    await Answer(self.cursor).wait()

def setup(bot):
    bot.add_cog(Marry(bot))