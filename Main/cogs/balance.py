import disnake
from disnake.ext import commands
import sqlite3



class Balance (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.connection = sqlite3.connect("server.db")
        self.cursor = self.connection.cursor() 


    @commands.slash_command(name="balance" , description="баланс пользователя")
    async def balance(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        balance = self.cursor.execute("SELECT cash FROM users WHERE id = ?", (member.id,)).fetchone()[0]
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        embed = disnake.Embed(
                title=f"Текущий баланс - {member.mention}",
                description=f"{balance}:coin:"
            )
        embed.set_thumbnail(url=avatar_url)
        await ctx.send(embed=embed)     


    @commands.slash_command(name="give", description="перевод средств")
    async def give(self, ctx, member: disnake.Member, сума: int):
        giver = ctx.author
        receiver = member
        amount1 =сума/100*95
        rounded_amount = int(amount1)
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        
        giver_balance = self.cursor.execute("SELECT cash FROM users WHERE id = ?", (giver.id,)).fetchone()[0]
        receiver_balance = self.cursor.execute("SELECT cash FROM users WHERE id = ?", (receiver.id,)).fetchone()[0]
        
        if giver_balance < сума:
            await ctx.send(f"{giver.mention}, у вас недостаточно средств для перевода.", ephemeral=True )
            return

        self.cursor.execute("UPDATE users SET cash = cash - ? WHERE id = ?", (сума, giver.id))
        self.cursor.execute("UPDATE users SET cash = cash + ? WHERE id = ?", (rounded_amount, receiver.id))
        self.connection.commit()
        embed = disnake.Embed(
                title="Перевод",
                description=f"Вы перевели {rounded_amount} :coin: {member.mention} "
            )
        
        embed.set_thumbnail(url=avatar_url)
        await ctx.send(embed=embed)
        




def setup(bot):
    bot.add_cog(Balance(bot))