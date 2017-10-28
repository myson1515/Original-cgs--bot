import aiml
import os

def memory():
    print("Getting memory...")
    kern.loadBrain("brain.brn")
    kern.learn('smallTalk.aiml')
    kern.saveBrian("brain.brn")
kern = aiml.Kernel()
fileToOpen = open("transfer.txt").read()
text = fileToOpen
kern.learn("smallTalk.aiml")
fileToWrite = open("transfer.txt", "w")
fileToWrite.write(kern.respond(text))
fileToWrite.close()

