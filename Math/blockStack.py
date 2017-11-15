from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.setBlock(6, 5, 28, 103)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 6
y = 5
z = 28
blocktype = 103
mc.setBlock(x, y, z, 103)
y = y + 1
mc.setBlock(x, y, z, 103)
    
