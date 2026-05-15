import discord
from discord.ext import commands
import random


bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all()
)

@bot.event
async def on_ready():

    print("Bot is online!")

@bot.command()
async def hello(ctx):

    await ctx.send("Hello!")

@bot.command()
async def ping(ctx):

    await ctx.send("Pong!")

@bot.command()
async def joke(ctx):

    jokes = [
        "Programming is fun.",
        "Python makes coding easier.",
        "Debugging is like solving puzzles."
    ]

    await ctx.send(random.choice(jokes))

@bot.command()
async def roll(ctx):

    number = random.randint(1, 6)

    await ctx.send(
        "You rolled " + str(number)
    )

@bot.command()
async def motivate(ctx):

    quotes = [
        "Keep learning every day.",
        "Consistency creates success.",
        "Practice improves coding skills."
    ]

    await ctx.send(random.choice(quotes))


bot.run("YOUR_BOT_TOKEN")