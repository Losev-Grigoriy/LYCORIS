import disnake
from disnake.ext import commands


class Verif_staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="staff", description="Выдача staff роли")
    async def staff(self, ctx, member: disnake.Member):
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

        class Staf(disnake.ui.Select):
            def __init__(self):
                super().__init__(
                    placeholder="Выберите роль",
                    options=[
                        disnake.SelectOption(label="Moderator", value="moderator", description="выдать роль"),
                        disnake.SelectOption(label="Designer", value="designer", description="выдать роль"),
                        disnake.SelectOption(label="Eventsmod", value="eventsmod", description="выдать роль"),
                        disnake.SelectOption(label="Creativet", value="creativet", description="выдать роль"),
                        disnake.SelectOption(label="Content maker", value="content_maker", description="выдать роль"),
                        disnake.SelectOption(label="Support", value="support", description="выдать роль"),
                        disnake.SelectOption(label="Tribunemod", value="tribunemod", description="выдать роль"),
                        disnake.SelectOption(label="PR manager", value="prmanager", description="выдать роль"),
                        disnake.SelectOption(label="Streamer", value="streamer", description="выдать роль"),
                        disnake.SelectOption(label="Helper", value="helper", description="выдать роль"),
                        
                        
                    ],
                )

            async def callback(self, inter: disnake.MessageInteraction):
                selected_value = inter.data["values"][0]
                role_ids = {
                    "moderator":1089523604565274746,
                    "designer":1115956471730012190,
                    "eventsmod":1089524364648644728,
                    "creativet":1260619724342038630,
                    "content_maker":1139600451617169550,
                    "support":1089524284151570452,
                    "tribunemod":1260619897650544652,
                    "prmanager":1089524436551610499,
                    "streamer":1139623051290488953,
                    "helper":1260618568060633108



                }
                role_id = role_ids.get(selected_value)
                if role_id:
                    role = disnake.utils.get(member.guild.roles, id=role_id)
                    
                    required_role_ids = {
                        "moderator":1127908886406500362,
                        "designer":1127909510061756456,
                        "eventsmod":1177952301076447313,
                        "creativet":1260619875664003144,
                        "content_maker":1190642392127254598,
                        "support":1126425350289760266,
                        "tribunemod":1260735719689818234,
                        "prmanager":1260735951039365221,
                        "streamer":1193209400211538032,
                        "helper":1260619113768943637
                    }
                    required_role_id = required_role_ids.get(selected_value)
                    if required_role_id and required_role_id in [role.id for role in ctx.author.roles]:
                        if role not in member.roles:
                            await member.add_roles(role)
                            
                            embed = disnake.Embed(
                                title="Staff",
                                description=f"вы выдали {member.mention} роль {selected_value}"
                            )
                            embed.set_thumbnail(url=avatar_url)
                            await inter.response.send_message(embed=embed)
                        else:
                            embed = disnake.Embed(
                                title="Staff",
                                description=f"{member.mention} уже имеет роль {selected_value}"
                            )
                            embed.set_thumbnail(url=avatar_url)
                            await inter.response.send_message(embed=embed, ephemeral=True)
                    else:
                        embed = disnake.Embed(
                            title="Staff",
                            description="у вас нет доступа к этой команде"
                        )
                        await inter.response.send_message(embed=embed, ephemeral=True)
                else:
                    embed = disnake.Embed(
                        title="Staff",
                        description="произошла ошибка при обработке запроса"
                    )
                    await inter.response.send_message(embed=embed, ephemeral=True)

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

    @commands.slash_command(name="removestaff", description="Снятие staff роли")
    async def removestaff(self, ctx, member: disnake.Member):
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

        class Stafff(disnake.ui.Select):
            def __init__(self):
                super().__init__(
                    placeholder="Выберите роль",
                    options=[
                        disnake.SelectOption(label="Moderator", value="moderator", description="снять роль"),
                        disnake.SelectOption(label="Designer", value="designer", description="снять роль"),
                        disnake.SelectOption(label="Eventsmod", value="eventsmod", description="снять роль"),
                        disnake.SelectOption(label="Creativet", value="creativet", description="снять роль"),
                        disnake.SelectOption(label="Content maker", value="content_maker", description="снять роль"),
                        disnake.SelectOption(label="Support", value="support", description="снять роль"),
                        disnake.SelectOption(label="Tribunemod", value="tribunemod", description="снять роль"),
                        disnake.SelectOption(label="PR manager", value="prmanager", description="снять роль"),
                        disnake.SelectOption(label="Streamer", value="streamer", description="снять роль"),
                        disnake.SelectOption(label="Helper", value="helper", description="снять роль"),
                        
                    ],
                )

            async def callback(self, inter: disnake.MessageInteraction):
                selected_value = inter.data["values"][0]
                role_ids = {
                    "moderator":1089523604565274746,
                    "designer":1115956471730012190,
                    "eventsmod":1089524364648644728,
                    "creativet":1260619724342038630,
                    "content_maker":1139600451617169550,
                    "support":1089524284151570452,
                    "tribunemod":1260619897650544652,
                    "prmanager":1089524436551610499,
                    "streamer":1139623051290488953,
                    "helper":1260618568060633108
                }
                role_id = role_ids.get(selected_value)
                if role_id:
                    role = disnake.utils.get(member.guild.roles, id=role_id)
                    
                    required_role_ids = {
                        "moderator":1127908886406500362,
                        "designer":1127909510061756456,
                        "eventsmod":1177952301076447313,
                        "creativet":1260619875664003144,
                        "content_maker":1190642392127254598,
                        "support":1126425350289760266,
                        "tribunemod":1260735719689818234,
                        "prmanager":1260735951039365221,
                        "streamer":1193209400211538032,
                        "helper":1260619113768943637
                    }
                    required_role_id = required_role_ids.get(selected_value)
                    if required_role_id and required_role_id in [role.id for role in ctx.author.roles]:
                        if role in member.roles:
                            await member.remove_roles(role)
                            
                            embed = disnake.Embed(
                                title="Staff",
                                description=f"вы сняли у {member.mention} роль {selected_value}"
                            )
                            embed.set_thumbnail(url=avatar_url)
                            await inter.response.send_message(embed=embed)
                        else:
                            embed = disnake.Embed(
                                title="Staff",
                                description=f"{member.mention} не имеет роли {selected_value}"
                            )
                            embed.set_thumbnail(url=avatar_url)
                            await inter.response.send_message(embed=embed, ephemeral=True)
                    else:
                        embed = disnake.Embed(
                            title="Staff",
                            description="у вас нет доступа к этой команде"
                        )
                        await inter.response.send_message(embed=embed, ephemeral=True)
                else:
                    embed = disnake.Embed(
                        title="Staff",
                        description="произошла ошибка при обработке запроса"
                    )
                    await inter.response.send_message(embed=embed, ephemeral=True)

        class StafffView(disnake.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(Stafff())

        embed = disnake.Embed(
            title="Staff",
            description=f"Пользователь: {member.mention}\n"
            f"ID: {member.id}\n",
        )
        embed.set_thumbnail(url=avatar_url)

        await ctx.send(embed=embed, view=StafffView(), ephemeral=True)

def setup(bot):
    bot.add_cog(Verif_staff(bot))