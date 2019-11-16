#!/usr/bin/python
import discord
import os.path
from discord.ext import commands

TOKEN = 'NjQ0NjA4NjgyNjI1MzM1Mjk2.Xc2iHw.OlBfobKgi3b5TqXr9t1YqfXPVIY'

client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
    print('Bot is  ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.command()
async def hi(ctx):
    await ctx.send(f'Hey')
    in_cmd = ctx.message.content
    add_history(in_cmd)


def add_history(cmd):
    if os.path.exists('history.txt'):
        file = open('history.txt','a+')
        file.write(f'{cmd}\n')
    else:
        file = open('history.txt','a+')
        file.write(f'{cmd}\n')

client.run(TOKEN)
