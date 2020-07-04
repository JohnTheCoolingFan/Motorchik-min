from discord.ext import commands
import discord


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description='\"Hello\" in English', brief='\"Hello\" in English', help='Returns \"Hello\" in English')
    async def hello(self, ctx: commands.Context):
        await ctx.send('Hello!')

    @commands.command(aliases=['gutentag'], description='\"Hello\" in German', brief='\"Hello\" in German', help='Returns \"Hello\" in German')
    async def hello_german(self, ctx: commands.Context):
        await ctx.send('Guten tag')

    @commands.command(aliases=['privet'], description='\"Hello\" in Russian', brief='\"Hello\" in Russian', help='Returns \"Hello\" in Russian')
    async def hello_russian(self, ctx: commands.Context):
        await ctx.send('Приветствую!')

    @commands.command(hidden=True, help='tag')
    async def guten(self, ctx: commands.Context):
        await ctx.send('tag')

    @commands.command(hidden=True, aliases=['живой?'])
    async def is_alive_rus(self, ctx: commands.Context):
        await ctx.send('Да')

    @commands.command(hidden=True, aliases=['youok?'])
    async def is_alive_eng(self, ctx: commands.Context):
        await ctx.send('yes')


def setup(bot):
    bot.add_cog(Greetings(bot))
