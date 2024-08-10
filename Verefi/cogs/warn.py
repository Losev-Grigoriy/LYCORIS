import disnake
from disnake.ext import commands, tasks
from disnake import TextInputStyle
import sqlite3
from datetime import datetime, timedelta

CHANNEL_ID = 1271171550065856552

class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('warnings.db')
        self.cursor = self.conn.cursor()
        
        
        # Создание таблицы, если она не существует
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS warnings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            reason TEXT,
            date_issued TIMESTAMP
        )
        ''')
        self.conn.commit()

        self.cleanup_warnings.start()

    # Функция для удаления устаревших предупреждений
    def delete_expired_warnings(self):
        expiration_date = datetime.now() - timedelta(days=30)
        self.cursor.execute("DELETE FROM warnings WHERE date_issued < ?", (expiration_date,))
        self.conn.commit()

    # Задача по проверке устаревших предупреждений каждый день
    @tasks.loop(hours=24)
    async def cleanup_warnings(self):
        self.delete_expired_warnings()

    # Команда warn
    @commands.slash_command(name="warn", description="Выдать варн пользователю")
    async def warn(self, ctx, member: disnake.Member,):
        channel = self.bot.get_channel(CHANNEL_ID)
        class Moderatorll(disnake.ui.Modal):
            def __init__(self, *args, **kwargs):
                components = [
                    disnake.ui.TextInput(
                        label="Причина dfhyf", 
                        placeholder="Нарушение правил",
                        custom_id="name",
                        style=TextInputStyle.short
                    ),
                    
                    
                    
                ]
                super().__init__(title="Причина варна", components=components)

            async def callback(self, interaction: disnake.ModalInteraction):
                name = interaction.text_values["name"]


                date_issued = datetime.now()
                self.cursor.execute("INSERT INTO warnings (user_id, reason, date_issued) VALUES (?, ?, ?)", (member.id, name, date_issued))
                self.conn.commit()
                
                
                
                
                    
                    
                    
                embed= disnake.Embed(
                        
                    title=f"Варн пользователя | {member.mention}"

                )
                embed.add_field(name=">>> Исполнитель", value=f"```{ctx.author}```",inline=False),    
                embed.add_field(name=">>> Причина варна", value=f"```{name}```",inline=False),

                ban = disnake.utils.get(member.guild.roles, id=1192610555945558086)

                await channel.send(embed=embed)

                await member.add_roles(ban)
               
                

                embed= disnake.Embed(
                        
                    title=f"Варн пользователя | {member.mention}",
                    description=f"вы успешно выдали варн {member.mention}"
                )
                    
               
                await ctx.send(embed=embed)

        modal= Moderatorll()
        await ctx.send_modal(modal)
        

    # Команда wlist
    @commands.slash_command(name="wlist", description="Посмотреть наказания пользывателя")
    async def wlist(self, ctx, member: disnake.Member):
        self.delete_expired_warnings()  # Удаляем устаревшие предупреждения перед выводом списка
        self.cursor.execute("SELECT reason, date_issued FROM warnings WHERE user_id = ?", (member.id,))
        warnings = self.cursor.fetchall()
        if warnings:
            warnings_list = "\n".join([f"{idx+1}. {reason} (выдано: {date_issued.strftime('%Y-%m-%d %H:%M:%S')})" 
                                        for idx, (reason, date_issued) in enumerate(warnings)])
            
            embed = disnake.Embed(
                title=f"Список наказаний для {member.mention}:",
                description=f"{warnings_list}"
            )

            await ctx.send(embed=embed)

        else:

            embed = disnake.Embed(
                title=f"Список наказаний для {member.mention}:",
                description=f"У {member.mention} нет предупреждений."
            )

            await ctx.send(embed=embed)
            

    # Команда wclear
    @commands.slash_command(name="wclear",description="Очистить наказания пользывателя"  )
    async def wclear(self, ctx, member: disnake.Member):
        channel = self.bot.get_channel(CHANNEL_ID)
        


        class Moderatorl(disnake.ui.Modal):
            def __init__(self, *args, **kwargs):
                components = [
                    disnake.ui.TextInput(
                        label="Причина снятия варна", 
                        placeholder="был выдан по ошибке",
                        custom_id="name",
                        style=TextInputStyle.short
                    ),
                    
                    
                    
                ]
                super().__init__(title="Причина снятия варна", components=components)

            async def callback(self, interaction: disnake.ModalInteraction):
                name = interaction.text_values["name"]

                self.cursor.execute("DELETE FROM warnings WHERE user_id = ?", (member.id,))
                self.conn.commit()
                
                
                
                    
                    
                    
                embed= disnake.Embed(
                        
                    title=f"Снятия варна | {member.mention}"

                )
                embed.add_field(name=">>> Исполнитель", value=f"```{ctx.author}```",inline=False),    
                embed.add_field(name=">>> Причина снятия варна", value=f"```{name}```",inline=False),

                

                await channel.send(embed=embed)

                
               
                

                embed= disnake.Embed(
                        
                    title=f"Снятия варна | {member.mention}",
                    description=f"вы успешно сняли все варны у {member.mention}"
                )
                    
               
                await channel.send(embed=embed)

        modal= Moderatorl()
        await ctx.send_modal(modal)



   

# Функция для добавления Cogs в бота
def setup(bot):
    bot.add_cog(Warns(bot))