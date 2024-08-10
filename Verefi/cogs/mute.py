import disnake
from disnake.ext import commands
from disnake import ButtonStyle
import asyncio

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="mute", description="выдать мут человеку")
    async def mute(self, ctx, member: disnake.Member, minut: int):

        class CustomButton(disnake.ui.View):
            def __init__(self):
                super().__init__(timeout=60)

            @disnake.ui.button(label="Текстовый", style=ButtonStyle.grey)
            async def send_message_button1(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
                txtmute = disnake.utils.get(member.guild.roles, id=1192549712386076802)

                await member.add_roles(txtmute)
                embed = disnake.Embed(
                    title="мут",
                    description=f"мут {member.mention} успешно выдан на {minut} минут"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)

                son = minut * 60
                await asyncio.sleep(son)
                await member.remove_roles(txtmute)

            @disnake.ui.button(label="Голосовой", style=ButtonStyle.grey)
            async def send_message_button2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
                voismute = disnake.utils.get(member.guild.roles, id=1104166539751587870)

                await member.add_roles(voismute)
                embed = disnake.Embed(
                    title="мут",
                    description=f"мут {member.mention} успешно выдан на {minut} минут"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)

                son = minut * 60
                await asyncio.sleep(son)
                await member.remove_roles(voismute)

        view = CustomButton()
        embed = disnake.Embed(
            title="мут",
            description=f"какой вид мута вы хотите выдать {member.mention}"
        )
        await ctx.send(embed=embed, view=view, ephemeral=True)

def setup(bot):
    bot.add_cog(Mute(bot))