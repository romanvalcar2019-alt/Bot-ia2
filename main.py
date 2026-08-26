import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()

async def check(ctx):

    if ctx.message.attachments:

        for attachment in ctx.message.attachments:

            file_name = attachment.filename

            url = attachment.url

            await attachment.save(f"./{file_name}")

            await ctx.send(get_class(modelpath="./keras_model.h5", labels="labels.txt", imagepath=f"./{attachment.filename}"))

    else:

        await ctx.send("no hay ninguna imagen enviada")        

@bot.event

async def on_ready():

    print(f'We have logged in as {bot.user}')



@bot.command()

async def hello(ctx):

    await ctx.send(f'Hi! I am a bot {bot.user}!')



@bot.command()

async def heh(ctx, count_heh = 5):

    await ctx.send("he" * count_heh)

# Reemplaza 'TU_NUEVO_TOKEN' con el token regenerado
bot.run("TOKEN")