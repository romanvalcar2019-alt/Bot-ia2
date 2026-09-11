


import discord
from discord.ext import commands
from model import get_class  # Tu función o script que procesa la imagen con la IA

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'SafeVision conectado como {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"./{file_name}"
            
            # Guardar la imagen localmente
            await attachment.save(file_path)
            await ctx.send("🔍 Analizando imagen con la IA...")
            
            # Pasar la imagen guardada a la IA
            nombre_clase, porcentaje_confianza = get_class(file_path)
            
            # Decisión basada en la clasificación
            if "Inapropiado" in nombre_clase:
                await ctx.message.delete()
                await ctx.send(f"⚠️ {ctx.author.mention}, tu imagen fue eliminada por ser clasificada como sensible/inapropiada ({porcentaje_confianza}% de certeza).")
            else:
                await ctx.send(f"✅ Imagen segura. Clasificada como: **{nombre_clase}** ({porcentaje_confianza}% de certeza).")
    else:
        await ctx.send("No adjuntaste ninguna imagen para analizar.")

# Reemplaza 'TU_NUEVO_TOKEN' con el token regenerado
bot.run("TOKEN")
