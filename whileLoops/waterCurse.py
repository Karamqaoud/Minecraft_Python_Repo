from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

count = 0
while count <= 30:
    time.sleep(1)
    print(count)
    count += 1
    

pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 8)
