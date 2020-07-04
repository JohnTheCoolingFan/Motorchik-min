#! /usr/bin/python3


from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$!'))


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

bot.load_extension('fun_commands')
bot.load_extension('greetings')
bot.load_extension('miscellaneous')
bot.load_extension('moderation')
bot.load_extension('service_tools')
bot.load_extension('test_commands')

with open('token.txt', 'r') as token_file:
    bot.run(token_file.read().rstrip())
