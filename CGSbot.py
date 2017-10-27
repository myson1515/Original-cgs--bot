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
    if message.content.startswith("!help"):
        await bot.send_message(channel,"Welcome to help!\n --------------")
        await bot.send_message(channel, "To talk to my artificial inteligence module please type !cgsbot 'what you want to say to the bot'")
        await bot.send_message(channel, "This bot is still in beta testing and may go offline occasionally.  This is because we are working on adding some new features to benefit you.")
        await bot.send_message(channel, "--------------\n If there are any issues with the bot or you have suggestions to add to the bot please DM the developer at @myson1515#2928")

bot.run('MzYzNDY2Njg2MTMwODE0OTg3.DNEpwg.J9xWSLkaiqOerH1CiZDQgu7ktYA')
