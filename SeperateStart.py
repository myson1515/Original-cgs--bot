import aiml
kern = aiml.Kernel()

kern.learn("smallTalk.aiml")
kern.saveBrain("brain.brn")
