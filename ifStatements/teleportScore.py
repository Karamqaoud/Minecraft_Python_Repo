from mcpi.minecraft import Minecraft
mc = Minecraft.create()

point = int(input("Enter your points: "))
if point > 2:
    mc.player.setPos(112, 10, 112)
elif point <= 2:
    mc.player.setPos(0, 12, 20)
elif points > 4:
    mc.player.setPos(60, 20, 32)
elif points > 6:
    mc.player.setPos(32, 18, -38)
else:
    mc.postToChat("I don't know what to do with that information.")
    
