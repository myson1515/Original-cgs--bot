import aiml


fileToOpen = open("transfer.txt").read()
text = fileToOpen
kern = aiml.Kernel()
y = "smallTalk.aiml"
kern.learn(y)
fileToWrite = open("transfer.txt", "w")
fileToWrite.write(kern.respond(text))
fileToWrite.close()

