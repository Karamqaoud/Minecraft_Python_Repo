from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Do you want blocks to be immutable? Y/N ")

worldImmutable = (answer=="Y")
if worldImmutable == True:
    print("world is immutable. ")
    
    mc.setting("world_immutable",True)
    mc.postToChat("World is immutable")
else:
    print("world is not immutable. ")

    mc.setting("world_immutable", False)
    mc.postToChat("World is not immutable")


