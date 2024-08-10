import disnake
from disnake.ext import commands
from disnake import TextInputStyle

CHANNEL_ID = 1271171550065856552

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="заблокировать")
    async def ban(self,ctx, member: disnake.Member ):
        channel = self.bot.get_channel(CHANNEL_ID)
       

        class Moderatorll(disnake.ui.Modal):
            def __init__(self, *args, **kwargs):
                components = [
                    disnake.ui.TextInput(
                        label="Причина бана", 
                        placeholder="многоразовое нарушение правил",
                        custom_id="name",
                        style=TextInputStyle.short
                    ),
                    
                    
                    
                ]
                super().__init__(title="Причина бана", components=components)

            async def callback(self, interaction: disnake.ModalInteraction):
                name = interaction.text_values["name"]
                
                
                
                    
                    
                    
                embed= disnake.Embed(
                        
                    title=f"ban пользователя | {member.mention}"

                )
                embed.add_field(name=">>> Исполнитель", value=f"```{ctx.author}```",inline=False),    
                embed.add_field(name=">>> Причина бана", value=f"```{name}```",inline=False),

                ban = disnake.utils.get(member.guild.roles, id=1192610555945558086)

                await channel.send(embed=embed)

                await member.add_roles(ban)
               
                

                embed= disnake.Embed(
                        
                    title=f"ban пользователя | {member.mention}",
                    description=f"вы успешно выдали бан {member.mention}"
                )
                    
               
                await ctx.send(embed=embed)

        modal= Moderatorll()
        await ctx.response.send_modal(modal)

def setup(bot):
    bot.add_cog(Ban(bot))        


        


            