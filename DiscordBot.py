# helper bot by lmfao#1111/tegz

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import asyncio
import time
import logging
import random
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Game
import json
import ctypes
from itertools import cycle
import aiofiles
import logging 
import os 


client = commands.Bot(command_prefix='.')
client.remove_command("help")
status = cycle(['Buy coding/hacking products from lmfao#1111', 'Follow us on all socials!'])

client.remove_command("help")


@client.event
async def on_ready():
    change_status.start()
    print ("Bot Is Ready")

@tasks.loop(seconds=1000)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))




@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use $help <command> for extended information on a command.",color = ctx.author.color)
    
    em.add_field(name = "Moderation", value = "kick,ban,purge")
    em.add_field(name = "Fun", value ="ping,info,invite")
    
    await ctx.send(embed = em)
    
@help.command()
async def kick(ctx):
    
    em = discord.Embed(title = "kick", description = "Kicks a member from the guild",color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = ".kick <member> [reason]")
    
    await ctx.send(embed = em)
    
@help.command()
async def ban(ctx):
    
    em = discord.Embed(title = "ban", description = "Bans a member from the guild",color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = ".ban <member> [reason]")
    
    await ctx.send(embed = em)

@help.command()
async def purge(ctx):
    
    em = discord.Embed(title = "purge", description = "Purges an amount of messgaes",color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = ".purge <amount>")
    
    await ctx.send(embed = em)
    





@client.command(pass_context=True)
async def pingeveryone(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await channel.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    channel = ctx.message.channel
    if member is None:
        await channel.send('Please input a user.')
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))

@client.command(pass_context=True)
async def kick(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send("Kicked **{}**, Damn kid".format(member.name))
            await member.kick()
    else:
        await channel.send('You lack permission to perform this action')

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send("Banned **{}**".format(member.name))
            await member.ban()
    else:
        await channel.send('You lack permission to perform this action')


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")


    
    
@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Deleted by {}'.format(ctx.author.mention))
        await ctx.message.delete()


    
client.run("Insert Token Here")
