from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input("This is my world")
mc.postToChat(message)
