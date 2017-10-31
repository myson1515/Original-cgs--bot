import aiml
import os
import datetime
print(datetime.datetime.now())
kern = aiml.Kernel()
fileToOpen = open("transfer.txt").read()
text = fileToOpen
kern.learn("smallTalk.aiml")
kern.saveBrain("brain.brn")
fileToWrite = open("transfer.txt", "w")
fileToWrite.write(kern.respond(text))
fileToWrite.close()
