from mcpi.minecraft import Minecraft
import time
import random


mc = Minecraft.create()

air = 0
stone = 1
dirt = 2

class animal:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        mc.setBlock(self.x, self.y, self.z, stone)

    def animate(self):
        #clear the space
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y-1, self.z, air)
        self.x = self.x + random.randint(-1, 1)
        self.y = self.y + random.randint(-1, 1)
        if random.randint(1, 10) == 5:
            self.z = self.z + random.randint(-2, 2)
        print(self.x)
        print(self.y)
        print(self.z)
        mc.setBlock(self.x, self.y, self.z, stone)
        
        
#main loop
#while True:
#    pass
