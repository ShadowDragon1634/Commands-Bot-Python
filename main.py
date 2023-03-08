import discord
from discord.ext import commands
import os
from discord import DMChannel
from discord import activity
import random
import string




intents = discord.Intents.all()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix="prefix", intents=intents, activity=discord.Game(name="TESTING BOT"))


@client.event
async def on_ready():
    print("Online")

@client.command()
async def embinfo (ctx):
    Embed = discord.Embed(
        title="**Title Messagio**",
        url="",
        description="*description*", color=discord.Color.dark_green()
    )
    Embed.set_author(
        name="Name",
        icon_url=""
    )
    await ctx.send(embed=Embed)




@client.command()
@commands.cooldown(1, 15, commands.BucketType.default)
async def dm(ctx):
    user = ctx.author
    await user.send("Messagio che manda in dm")



@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f"{message}" .format(message))




@client.command()
async def ping(ctx):
    await ctx.send("Pong")




client.run("TOKEN")