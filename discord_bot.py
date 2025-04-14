import discord
from discord.ext import commands
from app import get_password

intens = discord.Intents.default()
intens.message_content = True

bot = commands.Bot(command_prefix='/',intents=intens)

@bot.event
async def on_ready():
    print("El bot esta en linea")


@bot.command()
async def hola(ctx):
    await ctx.send("Hola,soy un bot de prueba")

@bot.command()
async def adios(ctx):
    await ctx.send("Adios, fue un placer")

@bot.command()
async def password(ctx):
    await ctx.send("Ingresa la longitud de la contraseña")

    def verificar(m):
        return m.author == ctx.author and m.channel == ctx.channel
    

    longitud = await bot.wait_for('message', check=verificar, timeout=40)

    longitud = int(longitud.content)

    password = get_password(longitud)
    await ctx.send(f"Tu contraseña es {password}")


bot.run("") 
