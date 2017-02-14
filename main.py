import server
import asyncio
import discord

server.selfbot = True

client = server.client

@server.command(".rev")
def reverse_text(message):
    yield from client.send_message(message.channel, u"\u202E" + message.content[5:])
    yield from client.delete_message(message)

server.start()
