import disnake
from disnake.ext import commands
import sqlite3

class Event_t(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logging = False
        self.modal_responses = {}
        self.command_author = None

    @commands.slash_command(name="event", description="евент на трибуде")
    async def event_t(self, inter: disnake.ApplicationCommandInteraction):
        self.command_author = inter.author

        class Event_m(disnake.ui.Modal):
            def __init__(self, parent_cog):
                self.parent_cog = parent_cog
                components = [
                    disnake.ui.TextInput(
                        label="Ответ на вопрос",
                        placeholder="Введите ответ на вопрос",
                        custom_id="Ответ на вопрос",
                        max_length=25
                    )
                ]
                super().__init__(title="Эвент", components=components)

            async def callback(self, inter: disnake.ModalInteraction):
                embed = disnake.Embed()
                for key, value in inter.text_values.items():
                    embed.add_field(
                        name=key.capitalize(),
                        value=value[:1024],
                        inline=False
                    )
                    self.parent_cog.modal_responses = value
                await inter.response.send_message()

        modal = Event_m(self)
        await inter.response.send_modal(modal=modal)

        self.logging = True

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.logging:
            useranswer = message.content
            modal_response = self.modal_responses

            if modal_response and useranswer == modal_response:
                self.logging = False

                # Открываем соединение и создаем курсор в контексте
                with sqlite3.connect("server.db") as connection:
                    cursor = connection.cursor()

                    nagrada = 50
                    cursor.execute(f"UPDATE users SET cash = cash + {nagrada} WHERE id = ?", (message.author.id,))
                    connection.commit()

                    await self.command_author.send(f"{message.author.mention} правильно ответил на вопрос")

def setup(bot):
    bot.add_cog(Event_t(bot))