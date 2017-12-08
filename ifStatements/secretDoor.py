from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -8.3
y = 11.0
z = -28.9

gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        x = -7.4
        y = 10.0
        z = -27.5
        blockType = 0
        mc.setBlock(x, y, z, blockType)
        x = -7.4
        y = 10.0
        z = -27.5
        blockType = 0
        mc.setBlock(x, y + 1, z, blockType)


else:
    mc.postToChat("Place an offering on the pedestal.")
