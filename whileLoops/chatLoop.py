from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    message = input("Enter a message: ")
    mc.postToChat(message)
    if message == "exit": 
        break
    print(message)
print("Loop exited")

