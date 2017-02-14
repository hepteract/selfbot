"""Base code for making and running a server"""

import discord
import random
import asyncio
import logging
import json
import sys

selfbot = False

logging.basicConfig(level=logging.WARN)

client = discord.Client()
config = json.load(open("config.json"))

@client.event
@asyncio.coroutine
def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    
    yield from client.change_presence(afk = True)
    print("Set to AFK!")
    print("----------")

commands = {}

def command(name):
    def decorator(func):
        commands[name] = func
        return asyncio.coroutine(func)
    return decorator

@client.event
@asyncio.coroutine
def on_message(message):
    if selfbot is True and message.author.id != client.user.id:
        return

    elif selfbot is False and message.author.id == client.user.id:
        return

    for command, function in commands.items():
        if message.content.startswith(command):
            yield from function(message)
            break

def start():  
    if "username" in config:
        client.run(config["username"], config["password"])
    else:
        client.run(config["token"])
