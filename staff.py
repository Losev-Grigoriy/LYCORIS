import disnake
from disnake.ext import commands
from disnake import ButtonStyle, TextInputStyle


CHANNEL_ID = 1271171550065856552

SUBMISSIONS_CHANNEL_ID = 1271171550065856552

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
            await self.clear_channel(channel)
            embed = disnake.Embed(
                title= f" <:1_a4:1089952877897846955> Наш стафф.",
                description= (
                    f" <a:softheartbk:1122098922878410752> **<@450603556941201409>** — создатель проекта.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1193226850940502026>** — руки и глаза овнера.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1089521532759449640>** — главное, но не высшее звено ответственности и полномочий.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1089524144841949205>** — лучшие в своем деле.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1089523604565274746>** — знают что хорошо, а что плохо.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1260619724342038630>** — проводит активности.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1115956471730012190>** — визуальная составляющая сервера.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1089524284151570452>** — гид для новичков.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1089524364648644728>** — создатель мероприятий и их ведение.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1139600451617169550>** — знают какой контент вам нужен.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1089524436551610499>** — реклама сервера.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1260619897650544652>** — проводит трибунки.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1260618568060633108>** — прописуют команды поднятия сервера.\n"
                    f" <a:softheartbk:1122098922878410752> **<@1139623051290488953>** — активно занимаются ведением Twitch.\n"
                ),
                color= 5814783
                
            )
            embed.set_image(url="https://cdn.discordapp.com/attachments/1258883465265287169/1271121980577550346/5fc54d4d39f9b585.png?ex=66b63018&is=66b4de98&hm=56a488424770dbf9f026107b47bb8f387ad75bed37b45a71fda44ad4c943bcae&")

            await channel.send(embed=embed, view=CustomButton())

            
    async def clear_channel(self, channel):
        # Функция для очистки сообщений в канале, если необходимо
        if channel:
            await channel.purge(limit=100)
def setup(bot):
    bot.add_cog(CustomButtons(bot))