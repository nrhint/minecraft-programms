from mcpi.minecraft import Minecraft
import time
import random


mc = Minecraft.create()

air = 0
stone = 57
dirt = 2

class animal:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y-2, self.z, stone)

    def animate(self):
        #clear the space
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y-2, self.z, air)
        self.x = self.x + random.randint(-1, 1)
        self.z = self.y + random.randint(-1, 1)
        if random.randint(1, 5) == 5:
            self.y = self.z + random.randint(-1, 1)
        print(self.x, self.y, self.z)
        mc.setBlock(self.x, self.y, self.z, stone)
        
x, y, z = mc.player.getPos()
a1 = animal(x, y, z)
   
#main loop

time.sleep(3)

while True:
    a1.animate()
    time.sleep(1)
