from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 2.7
y = 15.0
z = -42.4

gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        x = 3.7
        y = 14.0
        z = -41.7
        blockType = 0
        mc.setBlocks(x, y, z, blockType)

else:
    mc.postToChat("Place an offering on the pedestal.")
