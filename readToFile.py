import aiml
import os

kern = aiml.Kernel()
fileToOpen = open("transfer.txt")
lines = fileToOpen.readlines()
text = lines[0]
#kern.learn("smallTalk.aiml")
num = lines[1]
if num == 1:
    kern.learn("smallTalk.aiml")
    kern.saveBrain("brain.brn")
    fileToWrite = open("transfer.txt", "w")
#    print(text)
    print(kern.respond(text)+ "<--" )
    fileToWrite.write(kern.respond(str(text)))
    fileToWrite.close()
else:
    kern.loadBrain("brain.brn")
    fileToWrite = open("transfer.txt", "w")
#    print(text)
    state = kern.respond(text)
    print(kern.respond(text) + "<--")
    fileToWrite.write(state)
    fileToWrite.close()
    kern.saveBrain("brain.brn")

