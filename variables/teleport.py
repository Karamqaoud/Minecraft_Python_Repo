from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 

x = 10.0
y = 110.0
z = 12.0

mc.player.setPos(x, y, z)

time.sleep(10)

x = 55.0
y = 115.0
z = 20.0

mc.player.setPos(x, y, z)
