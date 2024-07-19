import disnake
from disnake.ext import commands
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import io
import aiohttp
import time
import asyncio

class Profil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.connection = sqlite3.connect("server.db")
        self.cursor = self.connection.cursor()
        self.update_task = self.bot.loop.create_task(self.update_voice_times())
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    name TEXT,
                    id INT PRIMARY KEY,
                    cash BIGINT,
                    cash1 BIGINT,
                    lvl INT,
                    sms INT,
                    rep INT,
                    voice_hours INT,
                    voice_minutes INT,
                    voice_seconds INT
                    )""")
        self.connection.commit()

        self.voice_states = {}

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for member in guild.members:
                if self.cursor.execute("SELECT id FROM users WHERE id = ?", (member.id,)).fetchone() is None:
                    self.cursor.execute("INSERT INTO users (name, id, cash, cash1, lvl, sms, rep, voice_hours, voice_minutes, voice_seconds) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(member), member.id, 10000, 0, 1, 0, 100, 0, 0, 0))
                    self.connection.commit()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.cursor.execute("SELECT id FROM users WHERE id = ?", (member.id,)).fetchone() is None:
            self.cursor.execute("INSERT INTO users (name, id, cash, cash1, lvl, sms, rep, voice_hours, voice_minutes, voice_seconds) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(member), member.id, 0, 0, 1, 0, 100, 0, 0, 0))
            self.connection.commit()
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        self.cursor.execute("UPDATE users SET sms = sms + 1 WHERE id = ?", (message.author.id,))
        self.connection.commit()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            # User joined a voice channel
            self.voice_states[member.id] = time.time()
        elif before.channel is not None and after.channel is None:
            # User left a voice channel
            if member.id in self.voice_states:
                start_time = self.voice_states.pop(member.id)
                session_time = int(time.time() - start_time)

                hours = session_time // 3600
                minutes = (session_time % 3600) // 60
                seconds = session_time % 60

                result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM users WHERE id = ?", (member.id,)).fetchone()
                if result:
                    current_hours, current_minutes, current_seconds = result
                    new_hours = current_hours + hours
                    new_minutes = current_minutes + minutes
                    new_seconds = current_seconds + seconds

                    # Adjust for overflow
                    if new_seconds >= 60:
                        new_minutes += new_seconds // 60
                        new_seconds = new_seconds % 60
                    if new_minutes >= 60:
                        new_hours += new_minutes // 60
                        new_minutes = new_minutes % 60

                    self.cursor.execute("UPDATE users SET voice_hours = ?, voice_minutes = ?, voice_seconds = ? WHERE id = ?", (new_hours, new_minutes, new_seconds, member.id))
                    self.connection.commit()

                    # Check if user leveled up
                    await self.check_level_up(member.id)

    async def update_voice_times(self):
        while True:
            await asyncio.sleep(10) 
            current_time = time.time()
            for member_id, start_time in list(self.voice_states.items()):
                session_time = int(current_time - start_time)

                hours = session_time // 3600
                minutes = (session_time % 3600) // 60
                seconds = session_time % 60

                try:
                    result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM users WHERE id = ?", (member_id,)).fetchone()
                    if result:
                        current_hours, current_minutes, current_seconds = result
                        new_hours = current_hours + hours
                        new_minutes = current_minutes + minutes
                        new_seconds = current_seconds + seconds

                        # Adjust for overflow
                        if new_seconds >= 60:
                            new_minutes += new_seconds // 60
                            new_seconds = new_seconds % 60
                        if new_minutes >= 60:
                            new_hours += new_minutes // 60
                            new_minutes = new_minutes % 60

                        self.cursor.execute("UPDATE users SET voice_hours = ?, voice_minutes = ?, voice_seconds = ? WHERE id = ?", (new_hours, new_minutes, new_seconds, member_id))
                        self.connection.commit()

                        # Check if user leveled up
                        await self.check_level_up(member_id)

                    self.voice_states[member_id] = current_time

                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")

    async def check_level_up(self, member_id):
        result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds, lvl FROM users WHERE id = ?", (member_id,)).fetchone()
        if result:
            current_hours, current_minutes, current_seconds, lvl = result

            total_sec = current_hours * 3600 + current_minutes * 60 + current_seconds

            required_time_for_next_level = 3600 * (2 ** (lvl - 1))
            
            if total_sec >= required_time_for_next_level:
                self.cursor.execute("UPDATE users SET lvl = lvl + 1 WHERE id = ?", (member_id,))
                self.connection.commit()
                lvl = self.cursor.execute("SELECT lvl FROM users WHERE id = ?", (member_id,)).fetchone()
                

    def text_pixel_length(self, text, font_path, font_size):
        temp_image = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(temp_image)
        font = ImageFont.truetype(font_path, font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        return text_width
    
    
        
    @commands.slash_command(name="profil", description="профиль")
    async def profil(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author

        user_exists = self.cursor.execute("SELECT 1 FROM users WHERE id = ?", (member.id,)).fetchone()
        if not user_exists:
            await ctx.send(f"Пользователь {member.name} не найден в базе данных.")
            return

        val1 = self.cursor.execute("SELECT cash FROM users WHERE id = ?", (member.id,)).fetchone()
        val1 = val1[0] if val1 else 0
        val2 = self.cursor.execute("SELECT cash1 FROM users WHERE id = ?", (member.id,)).fetchone()
        val2 = val2[0] if val2 else 0
        sms = self.cursor.execute("SELECT sms FROM users WHERE id = ?", (member.id,)).fetchone()
        sms = sms[0] if sms else 0
        rep = self.cursor.execute("SELECT rep FROM users WHERE id = ?", (member.id,)).fetchone()
        rep = rep[0] if rep else 0
        lvl = self.cursor.execute("SELECT lvl FROM users WHERE id = ?", (member.id,)).fetchone()
        lvl = lvl[0] if lvl else 0
        self.cursor.execute("SELECT id, voice_hours, voice_minutes, voice_seconds FROM users ORDER BY voice_hours DESC, voice_minutes DESC, voice_seconds DESC")
        sorted_users = self.cursor.fetchall()
        
        # Определяем место текущего пользователя в топе
        user_place = None
        for index, (user_id, hours, minutes, seconds) in enumerate(sorted_users, start=1):
            if user_id == member.id:
                user_place = index
                break
        
        result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM users WHERE id = ?", (member.id,)).fetchone()
        if result:
            voice_hours, voice_minutes, voice_seconds = result
            voice_time_formatted = f"{voice_hours}h {voice_minutes}m {voice_seconds}s"
        else:
            voice_time_formatted = "0h 0m 0s"

        result = self.cursor.execute("SELECT name1, name2, id1, id2 FROM loverum WHERE id1 = ? OR id2 = ?", (member.id, member.id)).fetchone()
        nik1 = nik2 = None
        if result:
            name1, name2, id1, id2 = result
            if member.id == id1:
                nik1 = name1
                nik2 = name2
            else:
                nik1 = name2
                nik2 = name1

        image_path = "profil.png"
        image = Image.open(image_path)
        
        draw = ImageDraw.Draw(image)
        font_path = "calibri.ttf"  
        font_size = 45 
        font = ImageFont.truetype(font_path, font_size)

        # Drawing the cash value
        text = str(val1)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (438 - pixel_length / 3, 728)
        draw.text(text_position, text, font=font, fill="white")

        text = str(val2)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (438 - pixel_length / 3, 854)
        draw.text(text_position, text, font=font, fill="white")

        font_size = 60
        text = str(voice_time_formatted)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (1065 - pixel_length / 3, 585)
        draw.text(text_position, text, font=font, fill="white")

        text = str(sms)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (1065 - pixel_length / 3, 682)
        draw.text(text_position, text, font=font, fill="white")

        text = str(user_place)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (1748 - pixel_length / 3, 585)
        draw.text(text_position, text, font=font, fill="white")

        text = str(rep)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (1748 - pixel_length / 3, 682)
        draw.text(text_position, text, font=font, fill="white")

        
        if nik1 and nik2 is not None:
            if member.name == nik2:
                text = str(nik1)
                pixel_length = self.text_pixel_length(text, font_path, font_size)
                text_position = (935, 847)
                draw.text(text_position, text, font=font, fill="white")
            elif member.name == nik1:
                text = str(nik2)
                pixel_length = self.text_pixel_length(text, font_path, font_size)
                text_position = (935, 847)
                draw.text(text_position, text, font=font, fill="white")

        
        text = str(lvl)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (1275 - pixel_length / 20, 318)
        draw.text(text_position, text, font=font, fill="white")

        level = lvl if lvl else 0
        required_time_for_next_level = 3600 * (2 ** (level - 1))
        result = self.cursor.execute("SELECT voice_hours, voice_minutes, voice_seconds FROM users WHERE id = ?", (member.id,)).fetchone()
        if result:
            current_hours, current_minutes, current_seconds = result
            total_seconds = current_hours * 3600 + current_minutes * 60 + current_seconds
            progress = min(total_seconds / required_time_for_next_level, 1.0)
            progress_width = int(839 * progress)
            draw.rectangle((870, 405, 870 + progress_width, 428), fill="#7d1010")

        font_size = 60
        font = ImageFont.truetype(font_path, font_size)
        text = str(member.name)
        pixel_length = self.text_pixel_length(text, font_path, font_size)
        text_position = (353 - pixel_length / 2, 514)
        draw.text(text_position, text, font=font, fill="white")

        async with aiohttp.ClientSession() as session:
            async with session.get(member.avatar.url if member.avatar else member.default_avatar.url) as resp:
                avatar_bytes = await resp.read()

        avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
        avatar_image = avatar_image.resize((300, 300))

        mask = Image.new("L", avatar_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + avatar_image.size, fill=255)
        avatar_image.putalpha(mask)

        image.paste(avatar_image, (231, 151), avatar_image)
        if nik1 and nik2 is not None:
            user = await self.fetch_user(id1)
            if user.name != member.name:
                async with aiohttp.ClientSession() as session:
                    async with session.get(user.avatar.url if user.avatar else user.default_avatar.url) as resp:
                        avatar_bytes = await resp.read()
                avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
                avatar_image = avatar_image.resize((115, 115))

                mask = Image.new("L", avatar_image.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + avatar_image.size, fill=255)
                avatar_image.putalpha(mask)

                image.paste(avatar_image, (793, 796), avatar_image)
            else:
                user = await self.fetch_user(id2)
                async with aiohttp.ClientSession() as session:
                    async with session.get(user.avatar.url if user.avatar else user.default_avatar.url) as resp:
                        avatar_bytes = await resp.read()
                avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
                avatar_image = avatar_image.resize((115, 115))

                mask = Image.new("L", avatar_image.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + avatar_image.size, fill=255)
                avatar_image.putalpha(mask)

                image.paste(avatar_image, (793, 796), avatar_image)

        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=disnake.File(fp=image_binary, filename="profil.png"))

    async def fetch_user(self, user_id):
        return await self.bot.fetch_user(user_id)

def setup(bot):
    bot.add_cog(Profil(bot))