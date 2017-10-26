import os
import asyncio
import discord
from daemonize import Daemonize
from discord.ext import commands
bot = commands.Bot(command_prefix='prefix', description='Chatterbox')
pid = "/tmp/cgsbot.pid"
@bot.event
async def on_message(message):
    mesString = message.content
    fileToWrite = open("transfer.txt", "w")
    mesStringFinal = mesString[8:]
    fileToWrite.write(mesStringFinal)
    fileToWrite.close()
    os.system("python2 readToFile.py")

    fileToOpen = open("transfer.txt").read()
    text = fileToOpen
    channel = message.channel
    if message.content.startswith("!cgsbot"): await bot.send_message(channel, text)

daemon = Daemonize(app="cgsbot", pid=pid, action=on_message)



bot.run('MzYzNDY2Njg2MTMwODE0OTg3.DNEpwg.J9xWSLkaiqOerH1CiZDQgu7ktYA')
daemon.start()

