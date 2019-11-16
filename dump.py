"""@client.command()
async def clear(ctx):
    await ctx.channel.purge(limit=10)"""

#@client.event
#async def on_message(message):
#    channel = message.channel
#    if message.content.startswith('.ping'):
#        await client.send_message(channel, 'Pong')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')
