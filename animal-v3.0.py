#I added a death programm
#
#

from mcpi.minecraft import Minecraft
import time
import random


mc = Minecraft.create()

air = 0
stone = 57
dirt = 2

class animal:
    def __init__(self, x, y, z, mode):
        self.x = x
        self.y = y
        self.z = z
        self.mode = mode
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y-2, self.z, stone)

    def animate(self):
        x, y, z = mc.player.getPos()
        if 0 == mc.getBlock(self.x, self.y, self.z):
            self.terminate()
        else:
            pass

        #clear the space
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y-2, self.z, air)
        if self.mode == 0:
            if random.randint(0, 1) == 1:
                self.x = self.x + random.randint(-1, 1)
            else:
                self.z = self.z + random.randint(-1, 1)
            if random.randint(1, 5) == 5:
                self.y = self.y + random.randint(-1, 1)
        elif self.mode == 1:
            #hunt
            if self.x - x  < 1:
                self.x = self.x + 1
            if self.x - x  > -1:
                self.x = self.x -1
            if self.z - z < 1:
                self.z = self.z + 1
            if self.z - z > 1:
                self.z = self.z - 1
            if self.y - y < 1:
                self.y = self.y + 1
            if self.y - y > 1:
                self.y = self.y - 1

            #print(self.z - z > 1)
        elif self.mode == 2:
            #run
            if self.x - x  < 1:
                self.x = self.x - 1
            if self.x - x  > -1:
                self.x = self.x +1
            if self.z - z < 1:
                self.z = self.z - 1
            if self.z - z > 1:
                self.z = self.z + 1
            #print(self.z - z > 1)

        #check for death

        mc.setBlocks(self.x, self.y, self.z, self.x, self.y-2, self.z, stone)
        #print(self.x, self.y, self.z)
    def terminate(self):
        print("died")
        
        
#x, y, z = mc.player.getPos()
x = random.randint(-100, 100)
y = random.randint(-100, 100)
z = random.randint(-100, 100)
a0 = animal(x, y, z, 1)
##a1 = animal(x, y, z, 0)
##a2 = animal(x, y, z, 0)
##a3 = animal(x, y, z, 0)
##a4 = animal(x, y, z, 0)
##a5 = animal(x, y, z, 0)
##a6 = animal(x, y, z, 0)
##a7 = animal(x, y, z, 0)
##a8 = animal(x, y, z, 0)
##a9 = animal(x, y, z, 0)

#main loop

time.sleep(1)

while True:
    a0.animate()
##    a1.animate()
##    a2.animate()
##    a3.animate()
##    a4.animate()
##    a5.animate()
##    a6.animate()
##    a7.animate()
##    a8.animate()
##    a9.animate()
    time.sleep(0.15)
