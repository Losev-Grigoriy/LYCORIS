import disnake
from disnake.ext import commands
from typing import Optional
class Verif_admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="admin", description="Выдача staff роли")
    async def admin(self, ctx, member: disnake.Member):
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

        class Staf(disnake.ui.StringSelect):
            def __init__(self):
                super().__init__(
                    placeholder="Выберите роль",
                    min_values=1,
                    max_values=2,
                    options=[
                        disnake.SelectOption(label="Curator", value="curator", description="выдать роль"),
                        disnake.SelectOption(label="Master", value="master", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Moderator", value="отвечает ⠂Moderator", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Designer", value="отвечает ⠂Designer", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Eventsmod", value="отвечает ⠂Eventsmod", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Creative", value="отвечает ⠂Creative", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Content Maker", value="отвечает ⠂Content Maker", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Support", value="отвечает ⠂Support", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Tribunemod", value="отвечает ⠂Tribunemod", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂PR manager", value="отвечает ⠂PR manage", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Streamer", value="отвечает ⠂Streamer", description="выдать роль"),
                        disnake.SelectOption(label="отвечает ⠂Helper", value="отвечает ⠂Helper", description="выдать роль"),
                    ],
                )

            async def callback(self, inter: disnake.MessageInteraction):
                selected_values = inter.data["values"]
                role_ids = {
                    "curator": 1089524144841949205,  
                    "master": 1260622087911899147,
                    "отвечает ⠂Moderator":1127908886406500362,
                    "отвечает ⠂Designer":1193206909751275720,
                    "отвечает ⠂Eventsmod":1177952301076447313,
                    "отвечает ⠂Creative":1260619875664003144,
                    "отвечает ⠂Content Maker":1190642392127254598,
                    "отвечает ⠂Support":1126425350289760266,
                    "отвечает ⠂Tribunemod":1260735719689818234,
                    "отвечает ⠂PR manage":1260735951039365221,
                    "отвечает ⠂Streamer":1193209400211538032,
                    "отвечает ⠂Helper":1260619113768943637
                }

                roles = [disnake.utils.get(member.guild.roles, id=role_ids.get(value)) for value in selected_values]

                

                if "curator" in selected_values:
                    admin_role_id = 1181481411451035710
                    admin_role = disnake.utils.get(member.guild.roles, id=admin_role_id)
                    if admin_role not in ctx.author.roles:
                        embed = disnake.Embed(
                            title="Staff",
                            description="У вас нет доступа к этой команде"
                        )
                        await inter.response.send_message(embed=embed, ephemeral=True)
                        return

                await member.add_roles(*roles)
                roles_mentions = ", ".join([role.mention for role in roles])
                embed = disnake.Embed(
                    title="Staff",
                    description=f"Вы выдали {member.mention} роли: {roles_mentions}"
                )
                embed.set_thumbnail(url=avatar_url)
                await inter.response.send_message(embed=embed)

                

        class StafView(disnake.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(Staf())



        embed = disnake.Embed(
            title="Staff",
            description=f"Пользователь: {member.mention}\n"
            f"ID: {member.id}\n",
        )
        embed.set_thumbnail(url=avatar_url)

        await ctx.send(embed=embed, view=StafView(), ephemeral=True)

    @commands.slash_command(name="removeadmin", description="Снятие staff роли")
    async def removeadmin(self, ctx, member: disnake.Member):
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

        class Staf(disnake.ui.StringSelect):
            def __init__(self):
                super().__init__(
                    placeholder="Выберите роль",
                    min_values=1,
                    max_values=2,
                    options=[
                        disnake.SelectOption(label="Curator", value="curator", description="снять роль"),
                        disnake.SelectOption(label="Master", value="master", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Moderator", value="отвечает ⠂Moderator", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Designer", value="отвечает ⠂Designer", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Eventsmod", value="отвечает ⠂Eventsmod", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Creative", value="отвечает ⠂Creative", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Content Maker", value="отвечает ⠂Content Maker", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Support", value="отвечает ⠂Support", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Tribunemod", value="отвечает ⠂Tribunemod", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂PR manager", value="отвечает ⠂PR manage", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Streamer", value="отвечает ⠂Streamer", description="снять роль"),
                        disnake.SelectOption(label="отвечает ⠂Helper", value="отвечает ⠂Helper", description="снять роль"),
                    ],
                )

            async def callback(self, inter: disnake.MessageInteraction):
                selected_values = inter.data["values"]
                role_ids = {
                    "curator": 1089524144841949205,  
                    "master": 1260622087911899147,
                    "отвечает ⠂Moderator":1127908886406500362,
                    "отвечает ⠂Designer":1193206909751275720,
                    "отвечает ⠂Eventsmod":1177952301076447313,
                    "отвечает ⠂Creative":1260619875664003144,
                    "отвечает ⠂Content Maker":1190642392127254598,
                    "отвечает ⠂Support":1126425350289760266,
                    "отвечает ⠂Tribunemod":1260735719689818234,
                    "отвечает ⠂PR manage":1260735951039365221,
                    "отвечает ⠂Streamer":1193209400211538032,
                    "отвечает ⠂Helper":1260619113768943637
                }

                roles = [disnake.utils.get(member.guild.roles, id=role_ids.get(value)) for value in selected_values]

            

                if "curator" in selected_values:
                    admin_role_id = 1181481411451035710
                    admin_role = disnake.utils.get(member.guild.roles, id=admin_role_id)
                    if admin_role not in ctx.author.roles:
                        embed = disnake.Embed(
                            title="Staff",
                            description="У вас нет доступа к этой команде"
                        )
                        await inter.response.send_message(embed=embed, ephemeral=True)
                        return

                await member.remove_roles(*roles)
                roles_mentions = ", ".join([role.mention for role in roles])
                embed = disnake.Embed(
                    title="Staff",
                    description=f"Вы забрали у {member.mention} роли: {roles_mentions}"
                )
                embed.set_thumbnail(url=avatar_url)
                await inter.response.send_message(embed=embed)

        class StafView(disnake.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(Staf())



        embed = disnake.Embed(
            title="Staff",
            description=f"Пользователь: {member.mention}\n"
            f"ID: {member.id}\n",
        )
        embed.set_thumbnail(url=avatar_url)

        await ctx.send(embed=embed, view=StafView(), ephemeral=True)

def setup(bot):
    bot.add_cog(Verif_admin(bot))