from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -18.1
y = 0.0
z = 7.9
gift = mc.getBlock(x, y, z)


if gift == 57:
    print("Thanks for the diamond. ")

elif gift == 6:
    print("I guess tree sapings are as good as diamonds... ")

else:
    mc.postToChat("Bring a gift to " + str(-18.1) +"," + str(0.0) + "," + str(7.9))
