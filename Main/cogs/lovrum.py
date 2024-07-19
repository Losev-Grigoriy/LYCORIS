import disnake
from disnake.ext import commands, tasks
import sqlite3

class VoiceManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.created_channels = {}
        self.TRIGGER_CHANNEL_ID = 1195783332831698954  # Replace with your channel ID
        self.connection = sqlite3.connect("server.db")
        self.cursor = self.connection.cursor()
        self.check_empty_channels.start()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        
        if after.channel and after.channel.id == self.TRIGGER_CHANNEL_ID and not before.channel:
            category = after.channel.category
            
            query = "SELECT name1, name2, id1, id2 FROM loverum WHERE id1 = ? OR id2 = ?"
            self.cursor.execute(query, (member.id, member.id))
            result = self.cursor.fetchone()
            if result:
                name1, name2, id1, id2 = result
                channel_name = f'{name1} 💝 {name2}'
            else:
                channel_name = 'Private Channel'
            
            new_channel = await category.create_voice_channel(channel_name, user_limit=2)
            
            if result:
                permissions = disnake.PermissionOverwrite(connect=True, speak=True, stream=True)
                await new_channel.set_permissions(member.guild.get_member(id1), overwrite=permissions)
                await new_channel.set_permissions(member.guild.get_member(id2), overwrite=permissions)
            
            await member.move_to(new_channel)
            
            self.created_channels[new_channel.id] = new_channel

        # When the user leaves a voice channel
        if before.channel and before.channel.id in self.created_channels:
            if len(before.channel.members) == 0:
                await before.channel.delete()
                del self.created_channels[before.channel.id]

    @tasks.loop(minutes=1)
    async def check_empty_channels(self):
        for channel_id in list(self.created_channels):
            channel = self.bot.get_channel(channel_id)
            if channel and len(channel.members) == 0:
                await channel.delete()
                del self.created_channels[channel_id]

    @check_empty_channels.before_loop
    async def before_check_empty_channels(self):
        await self.bot.wait_until_ready()

# Register Cogs
def setup(bot):
    bot.add_cog(VoiceManager(bot))