from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def murase(ctx):    
    await ctx.send(':fire:')
    
@bot.command()
async def yama(ctx):
    await ctx.send('anpan')
    
@bot.command()
async def せやな(ctx):
    await ctx.send('そやな')
    
    
bot.run(token)







