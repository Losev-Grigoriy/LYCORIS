import disnake
from disnake.ext import commands
from disnake import TextInputStyle

CHANNEL_ID = 1271171550065856552

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command( name="kick", description="Кикнуть участника с сервера")
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):

        channel = self.bot.get_channel(CHANNEL_ID)
       

        class Moderatorl(disnake.ui.Modal):
            def __init__(self, *args, **kwargs):
                components = [
                    disnake.ui.TextInput(
                        label="Причина кика", 
                        placeholder="многоразовое нарушение правил",
                        custom_id="name",
                        style=TextInputStyle.short
                    ),
                    
                    
                    
                ]
                super().__init__(title="Причина кика", components=components)

            async def callback(self, interaction: disnake.ModalInteraction):
                name = interaction.text_values["name"]
                
                
                
                    
                    
                    
                embed= disnake.Embed(
                        
                    title=f"кик пользователя | {member.mention}"

                )
                embed.add_field(name=">>> Исполнитель", value=f"```{inter.author}```",inline=False),    
                embed.add_field(name=">>> Причина кика", value=f"```{name}```",inline=False),

                

                await channel.send(embed=embed)

                await member.kick(reason=name)
               
                

                embed= disnake.Embed(
                        
                    title=f"кик пользователя | {member.mention}",
                    description=f"вы успешно кикнули {member.mention}"
                )
                    
               
                await inter.response.send(embed=embed)

        modal= Moderatorl()
        await inter.response.send_modal(modal)

        
        
        

def setup(bot):
    bot.add_cog(Moderation(bot))