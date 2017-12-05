from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x, y, z)

noMelon = input("Melons near by: ")
nearMelons = melon > 10 and melon < 20
print(" Near melons: " + str(nearMelons))

mc.postToChat("You need to ge some food: " + str(noMelon))
