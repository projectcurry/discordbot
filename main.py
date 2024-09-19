import os,random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    image = random.choice(os.listdir("mem"))
    with open(f'mem/{image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def diy(ctx):
    image = random.choice(os.listdir("diy"))
    with open(f'diy/{image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    if image=="plastic1.jpg":
        await ctx.send("we need 2 bottle and 6 cap",file=picture)

    if image=="plastic2.jpg":
        await ctx.send("we need 4 bottle and marker",file=picture)

    if image=="plastic3.jpg":
        await ctx.send("one bottle one cap and 2 stikes",file=picture)


