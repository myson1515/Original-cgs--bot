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
player = None
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
    mesStringFinal5 = mesString[12:]
    mesStringFinal4 = mesString[10:]
    mesStringFinal = mesString[8:]
    mesStringFinal2 = mesString[13:]
    fileToWrite.write(mesStringFinal)
 #   print(mesStringFinal5)
    fileToWrite.close()
    os.system("python2 readToFile.py")
    fileToOpen2 = open("transfer.txt").read()
    text = fileToOpen2
    channel = message.channel
    badWords = ("fuck", "bitch", "dick", "shit")
    for i in range(0, len(badWords)):
        if badWords[i] in str(message.content):
            print(i)
            swearFile = open("SwearUsers.txt", "a+")
            swearFile.write(str(message.author) + "\n")
            await bot.send_message(channel, str(message.author) + " Please do not swear anytime on this server.  Your message has been deleted. This incident will be recorded.")
            await bot.delete_message(message)
            swearFile.close()
#        else:
#            break
       # await bot.edit_message(message,"~~" + message.content + "~~")
        #print(text)
        #await client.edit_role(message.server, message.author.roles[1], colour=discord.Colour.red())
    if message.content.startswith("!knowAll"):
        await bot.send_message(channel, text)
    elif message.content.startswith("!help"):
        helpMessage = "Welcome to help!\n  -----------------  \nTo talk to my AI type !knowAll then what you would like to say to the AI \n ----------------- \nI am still in beta testing so if there is something wrong or you have suggestions please give feedback here: @myson1515#2928 \n  -----------------  \nI also have the capability to change your color role. \nTo get a list of available color roles please type !listRoles in the talk-with-a-bot channel. \nWhen you have found a nice color type !changeColor <the color you want>. \n ----------------- \nTo get a gif from Giphy type !getGif <the keyword of the gif you want>.\n ----------------- \nYou can make suggestions on songs to play with an Admin or Moderator in the playlist_suggestions channel.  If they approve of a song I will play it in the music channel. \n  ----------------- \nIf you are an Ambassador or a Teacher please use this command !changeRole to change to the role you belong in (The options are Japanese, Chinese, and Arabic)."
        await bot.send_message(channel, helpMessage)
    elif message.content.startswith("!listRoles"):
        allroles = bot.get_server("362621829569052676").roles
        count = 1
        finalMessage = "\n"
        for y in allroles[1:]:
           finalMessage += str(y) + "\n"
        await bot.send_message(channel, "The Following are the Roles of this Server: \n" + finalMessage)

    elif message.content.startswith("!getGif"):
        #img = translate(mesStringFinal)
        #await bot.send_message(channel, img.url)
        x = ""
        x = list(x)
        g = giphypop.Giphy()
        results = [x for x in g.search(mesStringFinal3)]
        await bot.send_message(channel, results[0])
    elif message.content.startswith("!playMusic"):
        searchText = mesStringFinal4
        query = urllib.parse.urlencode({"search_query": searchText})
        url = "https://www.youtube.com/results?search_query=" + query
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        global finalLink
        finalLink = "http://www.youtube.com/watch?v=" + search_results[0]
        global voice
        global player
        channel2 = bot.get_channel("400765530950074368")
        #voice = await bot.join_voice_channel(channel2)
        if player is None:
            print("Starting Music...")
            voice = await bot.join_voice_channel(channel2)
            player = await voice.create_ytdl_player(finalLink)
            player.start()
        else:
#        await bot.send_message(channel2, "Starting the music player.")
        #player.stop()
            player = await voice.create_ytdl_player(finalLink)
            player.start()
    elif message.content.startswith("!stopMusic"):
        #if voice.is_connected():
         #   print("Connected")
#        voice.disconnect()
#        stopMusic()
#        await bot.send_message(channel2, "Stopping the music player.")
        if player == None:
#            player = await voice.create_ytdl_player(finalLink)
            print("Stopping...")
            player.stop()
        else:
#            player = await voice.create_ytdl_player(finalLink)
            print("Stopping...")
            player.stop()
#        player = await voice.create_ytdl_player(finalLink)
    elif message.content.startswith("!changeRole"):
        allroles = bot.get_server("362621829569052676").roles
        authorRoles = []
        for role in message.author.roles:
            authorRoles.append(str(role.name))
            print(str(role.name))
        if mesStringFinal5 == "Chinese":
           if "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
               await bot.send_message(channel, "You already have a Role.  For more info please contact an Admin.")
           else:
               await bot.add_roles(message.author, allroles[3])
               await bot.send_message(channel, "The Role has been changed.")
        elif mesStringFinal5 == "Japanese":
           if "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
               await bot.send_message(channel, "You already have a Role.  For more information please contact an Admin.")
           else:
               await bot.add_roles(message.author, allroles[2])
               await bot.send_message(channel, "The Role has been changed.")
        elif mesStringFinal5 == "Arabic":
           if "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
               await bot.send_message(channel, "You already have a Role.  For more information please contact an Admin.")
           else:
               await bot.add_roles(message.author, allroles[4])
               await bot.send_message(channel, "The Role has been changed.")
        elif mesStringFinal5 == "Ambassador":
           await bot.send_message(channel,"To change to this role you must contact an Admin.")
        elif mesStringFinal5 == "Teacher":
           await bot.send_message(channel,"To change to this role you must contact an Admin.")
    elif message.content.startswith("!changeColor"):
        authorRoles = []
        for role in message.author.roles:
            authorRoles.append(str(role.name))
            print(str(role.name))
        print("--------")
        print(authorRoles[2])
        rememberRole = message.author.roles[2]
        #await bot.edit_role(message.server, message.author.roles[1], colour=discord.Colour.red(), name='Test')
        #print("###Roles###")
        allroles = bot.get_server("362621829569052676").roles
        if mesStringFinal2 == "Yellow":
           if "Admin" in authorRoles:
               await bot.replace_roles(message.author, allroles[13], allroles[1], allroles[5])
               await bot.add_roles(message.author, rememberRole)
           elif "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
#               rememberRole = authorRole[3]
#               print("HERE!!!!!")
#               print(rememberRole)
               await bot.replace_roles(message.author, allroles[13])
               await bot.add_roles(message.author, rememberRole)
               await bot.send_message(channel, "The Color has been changed.")

           else:
               await bot.add_roles(message.author, allroles[13])
#               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Pink":
           if "Admin" in authorRoles:
               await bot.replace_roles(message.author, allroles[12], allroles[1], allroles[5])
               await bot.add_roles(message.author, rememberRole)
           elif "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
#               rememberRole = authorRole[3]
#               print("HERE!!!!!")
#               print(rememberRole)
               await bot.replace_roles(message.author, allroles[12])
               await bot.add_roles(message.author, rememberRole)
               await bot.send_message(channel, "The Color has been changed.")

           else:
               await bot.add_roles(message.author, allroles[12])
#               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Green":
           if "Admin" in authorRoles:
               await bot.replace_roles(message.author, allroles[11], allroles[1], allroles[5])
               await bot.add_roles(message.author, rememberRole)
           elif "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
#               rememberRole = authorRole[3]
#               print("HERE!!!!!")
#               print(rememberRole)
               await bot.replace_roles(message.author, allroles[11])
               await bot.add_roles(message.author, rememberRole)
               await bot.send_message(channel, "The Color has been changed.")

           else:
               await bot.add_roles(message.author, allroles[11])
#               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")
        #await bot.add_roles(message.author, allroles[8])
        #for y in allroles:
         #   print(y)
        #if "Purple" in [y.name.lower() for y in message.author.roles]:
           # print("Purple spotted")
        elif mesStringFinal2 == "Blue":
           if "Admin" in authorRoles:
               await bot.replace_roles(message.author, allroles[10], allroles[1], allroles[5])
               await bot.add_roles(message.author, rememberRole)
           elif "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
#               rememberRole = authorRole[3]
#               print("HERE!!!!!")
#               print(rememberRole)
               await bot.replace_roles(message.author, allroles[10])
               await bot.add_roles(message.author, rememberRole)
               await bot.send_message(channel, "The Color has been changed.")

           else:
               await bot.add_roles(message.author, allroles[10])
#               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Red":
           if "Admin" in authorRoles:
               await bot.replace_roles(message.author, allroles[9], allroles[1], allroles[5])
               await bot.add_roles(message.author, rememberRole)
           elif "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
#               rememberRole = authorRole[3]
#               print("HERE!!!!!")
#               print(rememberRole)
               await bot.replace_roles(message.author, allroles[9])
               await bot.add_roles(message.author, rememberRole)
               await bot.send_message(channel, "The Color has been changed.")

           else:
               await bot.add_roles(message.author, allroles[9])
#               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")
        elif mesStringFinal2 == "Purple":
           if "Admin" in authorRoles:
               await bot.replace_roles(message.author, allroles[8], allroles[1], allroles[5])
               await bot.add_roles(message.author, rememberRole)
           elif "Chinese Students" in authorRoles or "Japanese Students" in authorRoles or "Arabic Students" in authorRoles:
#               rememberRole = authorRole[3]
#               print("HERE!!!!!")
#               print(rememberRole)
               await bot.replace_roles(message.author, allroles[8])
               await bot.add_roles(message.author, rememberRole)
               await bot.send_message(channel, "The Color has been changed.")

           else:
               await bot.add_roles(message.author, allroles[8])
#               await bot.replace_roles(message.author, allroles[12])
           #await bot.add_roles(message.author, allroles[12])
           await bot.send_message(channel, "The Color has been changed.")    
    elif text == " ":
        print("AIML code is incorrect please go back and check it.")
    else:
        print("There are no Errors in the code.")
bot.run('MzYzNDY2Njg2MTMwODE0OTg3.DON7bg.tHigSHJgbaVEBguNea2V3IVH-EQ')

