import disnake
from disnake.ext import commands
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import io
import aiohttp
import time
import asyncio


class Lprofil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = sqlite3.connect("server.db")
        self.cursor = self.connection.cursor()
        self.voice_states = {}
        self.bot.loop.create_task(self.update_voice_times())
        self.bot.add_listener(self.on_voice_state_update, 'on_voice_state_update')

    def text_pixel_length(self, text, font_path, font_size):
        temp_image = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(temp_image)
        font = ImageFont.truetype(font_path, font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        return text_width

    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            self.voice_states[member.id] = time.time()
        elif before.channel is not None and after.channel is None:
            if member.id in self.voice_states:
                start_time = self.voice_states.pop(member.id)
                session_time = int(time.time() - start_time)

                hours = session_time // 3600
                minutes = (session_time % 3600) // 60
                seconds = session_time % 60

                result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM loverum WHERE id1 = ? or id2 = ?", (member.id, member.id)).fetchone()
                if result:
                    current_hours, current_minutes, current_seconds = result
                    new_hours = current_hours + hours
                    new_minutes = current_minutes + minutes
                    new_seconds = current_seconds + seconds

                    if new_seconds >= 60:
                        new_minutes += new_seconds // 60
                        new_seconds = new_seconds % 60
                    if new_minutes >= 60:
                        new_hours += new_minutes // 60
                        new_minutes = new_minutes % 60

                    self.cursor.execute("UPDATE loverum SET voice_hours = ?, voice_minutes = ?, voice_seconds = ? WHERE id1 = ? or id2 = ?", (new_hours, new_minutes, new_seconds, member.id, member.id))
                    self.connection.commit()

    async def update_voice_times(self):
        while True:
            await asyncio.sleep(10)
            current_time = time.time()

            for member_id, start_time in list(self.voice_states.items()):
                guild = self.bot.get_guild(1181153675838763079)  # Replace with your guild ID
                if guild:
                    member = guild.get_member(member_id)
                    if member:
                        voice_state = member.voice
                        if voice_state and voice_state.channel and voice_state.channel.category_id == 1195782915150315520:  # Replace with your category ID
                            session_time = int(current_time - start_time)

                            hours = session_time // 3600
                            minutes = (session_time % 3600) // 60
                            seconds = session_time % 60

                            result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM loverum WHERE id1 = ? or id2 = ?", (member_id, member_id)).fetchone()
                            if result:
                                current_hours, current_minutes, current_seconds = result
                                new_hours = current_hours + hours
                                new_minutes = current_minutes + minutes
                                new_seconds = current_seconds + seconds

                                if new_seconds >= 60:
                                    new_minutes += new_seconds // 60
                                    new_seconds = new_seconds % 60
                                if new_minutes >= 60:
                                    new_hours += new_minutes // 60
                                    new_minutes = new_minutes % 60

                                self.cursor.execute("UPDATE loverum SET voice_hours = ?, voice_minutes = ?, voice_seconds = ? WHERE id1 = ? or id2 = ?", (new_hours, new_minutes, new_seconds, member_id, member_id))
                                self.connection.commit()

                            self.voice_states[member_id] = current_time

    @commands.slash_command(name="lprofil", description="любовный профиль")
    async def profil(self,  inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        await inter.response.defer()
        if member is None:
            member = inter.author

        # Check if the member exists in the loverum table
        result = self.cursor.execute(
            "SELECT name1, name2, id1, id2, cash FROM loverum WHERE id1 = ? OR id2 = ?",
            (member.id, member.id)
        ).fetchone()

        if not result:
            if member.id == inter.author.id:
                await inter.edit_original_response(content=f"{member.mention}, у вас нет пары.")
                return
            else:
                await inter.edit_original_response(content=f"у {member.mention} нет пары." )
                return

        nik1, nik2, id1, id2, cash = result

        result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM loverum WHERE id1 = ? or id2 = ?", (member.id, member.id)).fetchone()
        
        voice_hours = voice_minutes = voice_seconds = 0
        if result:
            voice_hours, voice_minutes, voice_seconds = result

        voice_time_formatted = f"{voice_hours}h {voice_minutes}m {voice_seconds}s"

        # Updated line based on table schema
        self.cursor.execute("SELECT id1, id2, voice_hours, voice_minutes, voice_seconds FROM loverum ORDER BY voice_hours DESC, voice_minutes DESC, voice_seconds DESC")
        sorted_users = self.cursor.fetchall()

        # Определяем место текущего пользователя в топе
        user_place = None
        for index, (id1, id2, hours, minutes, seconds) in enumerate(sorted_users, start=1):
            if id1 == member.id or id2 == member.id:
                user_place = index
                break

        image_path = "love_profil.png"
        image = Image.open(image_path)

        draw = ImageDraw.Draw(image)
        font_path = "calibri.ttf"
        font_size = 60
        font = ImageFont.truetype(font_path, font_size)

        if nik1:
            text = str(nik1)
            pixel_length = self.text_pixel_length(text, font_path, font_size)
            text_position = (257 - pixel_length / 20, 510)
            draw.text(text_position, text, font=font, fill="white")

        if nik2:
            text = str(nik2)
            pixel_length = self.text_pixel_length(text, font_path, font_size)
            text_position = (1375 - pixel_length / 20, 510)
            draw.text(text_position, text, font=font, fill="white")

        font_size = 45
        font = ImageFont.truetype(font_path, font_size)

        if cash is not None:
            text = str(cash)
            pixel_length = self.text_pixel_length(text, font_path, font_size)
            text_position = (445 - pixel_length / 20, 874)
            draw.text(text_position, text, font=font, fill="white")

        text = str(voice_time_formatted)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (997 - pixel_length / 2, 874)
        draw.text(text_position, text, font=font, fill="white")

        text = str(user_place)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (1586 - pixel_length / 2, 874)
        draw.text(text_position, text, font=font, fill="white")

        if nik1 and nik2 is not None:
            user = await self.bot.fetch_user(id1)

            async with aiohttp.ClientSession() as session:
                async with session.get(user.avatar.url if user.avatar else user.default_avatar.url) as resp:
                    avatar_bytes = await resp.read()
            avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
            avatar_image = avatar_image.resize((275, 275))

            mask = Image.new("L", avatar_image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + avatar_image.size, fill=255)
            avatar_image.putalpha(mask)

            image.paste(avatar_image, (264, 177), avatar_image)

            user = await self.bot.fetch_user(id2)

            async with aiohttp.ClientSession() as session:
                async with session.get(user.avatar.url if user.avatar else user.default_avatar.url) as resp:
                    avatar_bytes = await resp.read()
            avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
            avatar_image = avatar_image.resize((275, 275))

            mask = Image.new("L", avatar_image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + avatar_image.size, fill=255)
            avatar_image.putalpha(mask)

            image.paste(avatar_image, (1382, 177), avatar_image)

        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            file = disnake.File(fp=image_binary, filename='love_profil.png')
            await inter.edit_original_response(file=file)

def setup(bot):
    bot.add_cog(Lprofil(bot))