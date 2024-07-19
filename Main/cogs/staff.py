import disnake
from disnake.ext import commands
from disnake import ButtonStyle, TextInputStyle


CHANNEL_ID = 1181658965285801984

SUBMISSIONS_CHANNEL_ID = 1181659122874208256

class Moderatorl(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Moderator```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)

class Designer(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Designer```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)

class Eventsmod(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Eventsmod```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)

class Creativet(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Creativet```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)

class Content_Maker(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Content_Maker```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)

class Support(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Support```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)


class Tribunemod(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Tribunemod```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)


class PRmanager(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```PRmanager```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)



class Streamer(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Streamer```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)        

class Helper(disnake.ui.Modal):
    def __init__(self, *args, **kwargs):
        components = [
            disnake.ui.TextInput(
                label="ваше имя, ворзаст", # имя возраст
                placeholder="Гриша, 16 лет",
                custom_id="name",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс ", #часовой пояс(от мск)
                placeholder="мск+1",
                custom_id="msc",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени вы готовы уделять серверу", #время уделение серверу
                placeholder="2 часа",
                custom_id="time",
                style=TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="был ли у вас опыт на даной должности и какой?", #опыт
                placeholder="да",
                custom_id="experience",
                style=TextInputStyle.paragraph
            ),
            
            
        ]
        super().__init__(title="заявка  Staff", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        name = interaction.text_values["name"]
        msc = interaction.text_values["msc"]
        time = interaction.text_values["time"]
        exp = interaction.text_values["experience"]

        submissions_channel = interaction.guild.get_channel(SUBMISSIONS_CHANNEL_ID)
        if submissions_channel:
            
            avatar_url = interaction.author.avatar.url if interaction.author.avatar else interaction.author.default_avatar.url
            
            embed= disnake.Embed(
                
                title=f"заявка Staff | {interaction.author.mention}"

            )
            embed.add_field(name=">>> Имя, возраст", value=f"```{name}```", inline=True),
            embed.add_field(name=">>> Часовой пояс", value=f"```{msc}```", inline=True),
            embed.add_field(name=">>> Должность", value="```Helper```", inline=True),
            embed.add_field(name=">>> Время, которое вы можете уделять серверу", value=f"```{time}```", inline=False),
            embed.add_field(name=">>> Опыт и другие проекты", value=f"```{exp}```", inline=False)
            embed.set_thumbnail(url=avatar_url)
            


            await submissions_channel.send(embed=embed)
            await interaction.response.send_message("Ваша заявка была отправлена.", ephemeral=True)




class CustomButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Moderator", style=ButtonStyle.grey)
    async def send_message_button1(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Moderatorl()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Designer", style=ButtonStyle.grey)
    async def send_message_button2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Designer()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Eventsmod", style=ButtonStyle.grey)
    async def send_message_button3(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Eventsmod()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Creativet", style=ButtonStyle.grey)
    async def send_message_button4(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Creativet()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Content_Maker", style=ButtonStyle.grey)
    async def send_message_button5(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Content_Maker()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Support", style=ButtonStyle.grey)
    async def send_message_button6(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Support()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Tribunemod", style=ButtonStyle.grey)
    async def send_message_button7(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Tribunemod()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="PRmanager", style=ButtonStyle.grey)
    async def send_message_button8(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = PRmanager()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Streamer", style=ButtonStyle.grey)
    async def send_message_button9(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Streamer()
        await interaction.response.send_modal(modal)

    @disnake.ui.button(label="Helper", style=ButtonStyle.grey)
    async def send_message_button10(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = Helper()
        await interaction.response.send_modal(modal)

class CustomButtons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(CHANNEL_ID)
        if channel:
            embed = disnake.Embed(
                title="Нажмите на кнопку, чтобы отправить сообщение:"
            )

            await channel.send(embed=embed, view=CustomButton())

def setup(bot):
    bot.add_cog(CustomButtons(bot))