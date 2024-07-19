import disnake
from disnake.ext import commands
from typing import Optional

class Verif_f(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="verif", description="Верефикация")
    async def verif(ctx, member: disnake.Member):

        class Nedop(disnake.ui.Modal):
            def __init__(self):
                components=[
                    disnake.ui.TextInput(
                        label="Причина недопуска",
                        placeholder="Ведите причину недопуска",
                        custom_id="Причина недопуска",
                        max_length=50
                    )

                ]
                super().__init__(title="Недопуск", components=components)
            async def callback(self, inter: disnake.ModalInteraction):
                
                avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

                embed = disnake.Embed(
                    title="Недопуск ",
                    description=f"Пользователь:{member.mention}"
                )
                for key, value in inter.text_values.items():
                    embed.add_field(
                        name=key.capitalize(),
                        value=value[:1024],
                        inline=False

                    )
                embed.set_thumbnail(url=avatar_url)
                await inter.response.send_message(embed=embed)
                nedop = disnake.utils.get(member.guild.roles, id=1260729539420618863)
                await member.add_roles(nedop)
                anverefi = disnake.utils.get(member.guild.roles, id=1260727937662193674)
                await member.remove_roles(anverefi)
                



        class Verif(disnake.ui.View):
            def __init__(self):
                super().__init__(timeout=60)
                self.value: Optional[bool] = None

            @disnake.ui.button(label="мужская", style=disnake.ButtonStyle.grey)
            async def man(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
                
                man = disnake.utils.get(member.guild.roles, id=753254181841928212)
                await member.add_roles(man)
                anverefi = disnake.utils.get(member.guild.roles, id=1260727937662193674)
                await member.remove_roles(anverefi)
                avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
                
                embed = disnake.Embed(
                    title="Верефикация",
                    description=f"вы выдали {member.mention} мужскую роль"
                        

                )
                embed.set_thumbnail(url=avatar_url)
                await inter.response.send_message(embed=embed )
                
                self.value = True
                self.stop()

            @disnake.ui.button(label="женская", style=disnake.ButtonStyle.grey)
            async def girl(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
                
                girl = disnake.utils.get(member.guild.roles, id=753253834595369111)
                await member.add_roles(girl)
                anverefi = disnake.utils.get(member.guild.roles, id=1260727937662193674)
                await member.remove_roles(anverefi)
                avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
                
                embed = disnake.Embed(
                    title="Верефикация",
                    description=f"вы выдали {member.mention} женскую роль"
                        

                )
                embed.set_thumbnail(url=avatar_url)
                await inter.response.send_message(embed=embed )

                self.value = False
                self.stop()

            @disnake.ui.button(label="недопуск", style=disnake.ButtonStyle.grey)
            async def nedop(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
                member = inter.user
                modal = Nedop()
                await inter.response.send_modal(modal=modal)
                
                


                self.value = None
                self.stop()
        anverefi = disnake.utils.get(ctx.guild.roles, id=1260727937662193674)
        nedop = disnake.utils.get(ctx.guild.roles, id=1260729539420618863)
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        
        if anverefi in member.roles and nedop not in member.roles:
            embed = disnake.Embed(
                title="Верификация",
                description=f"Пользователь: {member.mention}\n"
                            f"ID: {member.id}\n"
                            f"Creat: {str(member.created_at)[:-21]}"
            )
            embed.set_thumbnail(url=avatar_url)
            await ctx.send(embed=embed, view=Verif(), ephemeral=True)
            await Verif().wait()
        if nedop in member.roles and anverefi not in member.roles:
            embed = disnake.Embed(
                title="Недопуск",
                description=f"У пользователя {member.mention} недопуск"
            )
            embed.set_thumbnail(url=avatar_url)
            await ctx.send(embed=embed, ephemeral=True)
        if anverefi not in member.roles and nedop not in member.roles:
            embed = disnake.Embed(
                title="Верификация",
                description=f"Пользователь {member.mention} уже верифицирован"
            )
            embed.set_thumbnail(url=avatar_url)
            await ctx.send(embed=embed, ephemeral=True)

    @commands.Cog.listener()
    async def on_member_join(member):
        anverefi = disnake.utils.get(member.guild.roles, id=1260727937662193674)
        await member.add_roles(anverefi)




def setup(bot):
    bot.add_cog(Verif_f(bot))