import nacl
import giphypop
import youtube_dl
import urllib
from giphypop import translate
import datetime
import os
import re
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
    mesStringFinal3 = mesString[7:]
    mesStringFinal4 = mesString[10:]
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
        helpMessage = "Welcome to help!\n  -----------------  \nTo talk to my AI type !cgsbot then what you would like to say to the AI \n ----------------- \nThis bot is still in beta testing so if there is something wrong or you have suggestions please give feedback here: @myson1515#2928 \n  -----------------  \nCGSbot also has the capability to change your color role. \nTo get a list of available color roles please type !listRoles in the talk-with-a-bot channel. \nWhen you have found a nice color type !changeColor <the color you want>. \n ----------------- \nTo get a gif from Giphy type !getGif <the keyword of the gif you want>."
        await bot.send_message(channel, helpMessage)
    if message.content.startswith("!listRoles"):
        allroles = bot.get_server("362621829569052676").roles
        count = 1
        finalMessage = "\n"
        for y in allroles[8:]:
           finalMessage += str(y) + "\n"
        await bot.send_message(channel, "The Following are the Roles of this Server: \n" + finalMessage)

    if message.content.startswith("!getGif"):
        #img = translate(mesStringFinal)
        #await bot.send_message(channel, img.url)
        x = ""
        x = list(x)
        g = giphypop.Giphy()
        results = [x for x in g.search(mesStringFinal3)]
        await bot.send_message(channel, results[0])
    if message.content.startswith("!playMusic"):
        searchText = mesStringFinal4
        query = urllib.parse.urlencode({"search_query": searchText})
        url = "https://www.youtube.com/results?search_query=" + query
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        finalLink = "http://www.youtube.com/watch?v=" + search_results[0]
        global voice
        channel2 = bot.get_channel("400765530950074368")
        voice = await bot.join_voice_channel(channel2)
        global player
        player = await voice.create_ytdl_player(finalLink)
#        await bot.send_message(channel2, "Starting the music player.")
        player.start()
    if message.content.startswith("!stopMusic"):
#        await bot.send_message(channel2, "Stopping the music player.")
        player.stop()
    if message.content.startswith("!changeColor"):
        #await bot.edit_role(message.server, message.author.roles[1], colour=discord.Colour.red(), name='Test')
        #print("###Roles###")
        allroles = bot.get_server("362621829569052676").roles
        if mesStringFinal2 == "Yellow":
           if str(message.author) == "myson1515#2928":
               await bot.replace_roles(message.author, allroles[13], allroles[1], allroles[5])

               #await bot.replace_roles(message.author, allroles[13], allroles[5])
           elif str(message.author) == "Maosre#6219":
               await bot.replace_roles(message.author, allroles[13], allroles[1], allroles[5])
           else:
               await bot.replace_roles(message.author, allroles[13])
           #await bot.add_roles(message.author, allroles[13])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Pink":
           if str(message.author) == "myson1515#2928":
               await bot.replace_roles(message.author, allroles[12], allroles[1], allroles[5])
           elif str(message.author) == "Maosre#6219":
               await bot.replace_roles(message.author, allroles[12], allroles[1], allroles[5])
           else:
               await bot.add_roles(message.author, allroles[13])
               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Green":
           if str(message.author) == "myson1515#2928":
               await bot.replace_roles(message.author, allroles[11], allroles[5])
           elif str(message.author) == "Maosre#6219":
               await bot.replace_roles(message.author, allroles[11], allroles[1], allroles[5])
           else:
               await bot.replace_roles(message.author, allroles[11])
           #await bot.replace_roles(message.author,allroles[11])
           #await bot.add_roles(message.author, allroles[11])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Blue":
           if str(message.author) == "myson1515#2928":
               await bot.replace_roles(message.author, allroles[10], allroles[1], allroles[5])
               #await bot.replace_roles(message.author, allroles[10], allroles[5])
           elif str(message.author) == "Maosre#6219":
               await bot.replace_roles(message.author, allroles[10], allroles[1], allroles[5])
           else:
               await bot.replace_roles(message.author, allroles[10])
           #await bot.add_roles(message.author, allroles[10])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Red":
           if str(message.author) == "myson1515#2928":
               await bot.replace_roles(message.author, allroles[9], allroles[1], allroles[5])

               #await bot.replace_roles(message.author, allroles[9], allroles[5])
           elif str(message.author) == "Maosre#6219":
               await bot.replace_roles(message.author, allroles[9], allroles[1], allroles[5])
           else:
               await bot.replace_roles(message.author, allroles[9])
           #await bot.replace_roles(message.author, allroles[9])
           #await bot.add_roles(message.author, allroles[9])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Purple":
           if str(message.author) == "myson1515#2928":
               await bot.replace_roles(message.author, allroles[8], allroles[1], allroles[5])
               #await bot.replace_roles(message.author, allroles[8], allroles[5])
           elif str(message.author) == "Maosre#6219":
               await bot.replace_roles(message.author, allroles[8], allroles[1], allroles[5])
           else:
               await bot.replace_roles(message.author, allroles[8])
           await bot.send_message(channel, "The Color has been changed.")
        else:
           await bot.send_message(channel, "Not a valid role please read !listRoles")


        #await bot.edit_role(message.server, allroles[8], colour=discord.Colour.red())
        #await bot.add_roles(message.author, allroles[8])
        #for y in allroles:
         #   print(y)
        #if "Purple" in [y.name.lower() for y in message.author.roles]:
           # print("Purple spotted")
    if text == " ":
        print("AIML code is incorrect please go back and check it.")
    else:
        print("There are no Errors in the code.")
bot.run('MzYzNDY2Njg2MTMwODE0OTg3.DON7bg.tHigSHJgbaVEBguNea2V3IVH-EQ')


