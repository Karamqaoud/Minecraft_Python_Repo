from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6 
blocktype = 4
air = 0 
mc.setBlock(x, y, z, x + width, y + height, z + length, blocktype)
