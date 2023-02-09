from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x_start, y_start, z_start = mc.player.getTilePos()
size = 35
mc.setBlocks(x_start, y_start - 1, z_start, x_start + size, y_start - 1, z_start + size, 4)
mine = 171
for x in range(size):
    for z in range(0, size):
        mc.setBlock((x_start + x, y_start, z_start + z, random.choice([171, 0, 0, 0, 0])))
lava = 10
mc.setBlocks(x_start, y_start - 4, z_start, x_start + size, y_start - 4, z_start + size, lava)
while True:
    x, y, z = mc.player.getTilePos()
    if mc.getBlock(x, y, z) == 171:
        mc.player.setTilePos(x_start, y_start - 4, z_start)
        mc.postToChat("игра окончена")
        break