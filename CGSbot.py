import datetime
import os
import asyncio
import discord
from daemonize import Daemonize
from discord.ext import commands
#print(datetime.datetime.now())
#print("Bot File loaded...")
count = 0
def empty():
    print("Memory Loaded.")
bot = commands.Bot(command_prefix='prefix', description='Chatterbox')
pid = "/tmp/cgsbot.pid"

#fileToWrite = open("transfer.txt", "w")
#startREAD = "start"

#fileToWrite.write("hi \n1")
#fileToWrite.close()
#os.system("python2 readToFile.py")
#fileToOpen = open("transfer.txt").read()
#text = fileToOpen


def get_role(server_roles, target_name):
    for each in server_roles:
        if each.name == target_name:
            return each
        return None
@bot.event
async def on_message(message):
    mesString = message.content
    fileToOpen = open("transfer.txt")
    lines = fileToOpen.readlines()
    #os.system("python2 readToFile.py")
#    if lines[0] == 1:
#        fileToWrite = open("transfer.txt", "w")
#        fileToOpen = open("transfer.txt")
#        lines = fileToOpen.readlines()
#        mesStringFinal = mesString[8:]
#        fileToWrite.write(mesStringFinal)
    fileToWrite = open("transfer.txt", "w")
    fileToOpen = open("transfer.txt")
    lines = fileToOpen.readlines()
    mesStringFinal = mesString[8:]
    mesStringFinal2 = mesString[13:]
    fileToWrite.write(mesStringFinal)
    print(mesStringFinal2)
    fileToWrite.close()
    os.system("python2 readToFile.py")
    fileToOpen2 = open("transfer.txt").read()
    text = fileToOpen2
    channel = message.channel
    if message.content.startswith("!cgsbot"):
        #print(text)
        #await client.edit_role(message.server, message.author.roles[1], colour=discord.Colour.red())
        await bot.send_message(channel, text)
    if message.content.startswith("!help"):
        await bot.send_message(channel,"Welcome to help!\n --------------")
        await bot.send_message(channel, "To talk to my artificial inteligence module please type !cgsbot 'what you want to say to the bot'")
        await bot.send_message(channel, "This bot is still in beta testing and may go offline occasionally.  This is because we are working on adding some new features to benefit you.")
        await bot.send_message(channel, "--------------\n If there are any issues with the bot or you have suggestions to add to the bot please DM the developer at @myson1515#2928")
    if message.content.startswith("!listRoles"):
        allroles = bot.get_server("362621829569052676").roles
        count = 1
        finalMessage = " "
        for y in allroles:
           finalMessage += str(y) + "\n"
        await bot.send_message(channel, "The Following are the Roles of this Server (The bottom 6 are the ones you can change too): \n" + finalMessage)
    if message.content.startswith("!changeColor"):
        #await bot.edit_role(message.server, message.author.roles[1], colour=discord.Colour.red(), name='Test')
        print("###Roles###")
        allroles = bot.get_server("362621829569052676").roles
        if mesStringFinal2 == "Yellow":
           await bot.add_roles(message.author, allroles[13])
        if mesStringFinal2 == "Pink":
           await bot.add_roles(message.author, allroles[12])
        if mesStringFinal2 == "Green":
           await bot.add_roles(message.author, allroles[11])
        if mesStringFinal2 == "Blue":
           await bot.add_roles(message.author, allroles[10])
        if mesStringFinal2 == "Red":
           await bot.add_roles(message.author, allroles[9])
        if mesStringFinal2 == "Purple":
           await bot.add_roles(message.author, allroles[8])


        #await bot.edit_role(message.server, allroles[8], colour=discord.Colour.red())
        #await bot.add_roles(message.author, allroles[8])
        #for y in allroles:
         #   print(y)
        #if "Purple" in [y.name.lower() for y in message.author.roles]:
           # print("Purple spotted")
        await bot.send_message(channel, "The Color has been changed.")
    if text == " ":
        print("AIML code is incorrect please go back and check it.")
    else:
        print("There are no Errors in the code.")
bot.run('MzYzNDY2Njg2MTMwODE0OTg3.DON7bg.tHigSHJgbaVEBguNea2V3IVH-EQ')


