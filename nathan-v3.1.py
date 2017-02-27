from mcpi.minecraft import Minecraft
import time
from time import sleep
import random


mc = Minecraft.create()

mc.postToChat("Comands active.")


def goTo(x, y, z):
       mc.player.setPos(x, y, z)

def house():
       x, y, z = mc.player.getPos()
       mc.setBlocks(x+5, y+5, z+5, x-5, y-5, z-5, 1)
       mc.setBlocks(x+4, y+4, z+4, x-4, y-4, z-4, 0)

def mansion():
    stone = 1
    lava = 246
    x, y, z = mc.player.getPos()
    #set foundation
    mc.setBlocks(x-10, y-7, z-10, x+10, y+70, z+10, air)
    #floor
    mc.setBlocks(x-8, y-5, z-8, x+8, y-5, z+8, 4)
    #wall
    mc.setBlocks(x-8, y-5, z-8, x-8, y+10, z+8, 4)
    #wall
    mc.setBlocks(x+8, y-5, z-8, x+8, y+10, z+8, 4)
    #wall
    mc.setBlocks(x-8, y-5, z+8, x+8, y+10, z+8, 4)
    #wall
    mc.setBlocks(x-8, y-5, z-8, x+8, y+10, z-8, 4)
    #ceiling
    mc.setBlocks(x+8, y+5, z-10, x-10, y+8, z+8, 18)

def post(text):
       str_text = str(text)
       mc.postToChat(str_text)

def trace(timeToTrace, item):
    trace = True
    start = time.time()
    while trace == True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, item, 1)
        if time.time() - start > timeToTrace:
               trace = False

def tnt():
    tnt = 46
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y-1, z, tnt, 1)

def STntB():
    tnt = 46
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-1, y-1, z-1, x+1, y-1, z+1, tnt, 1)

def TntB():
    tnt = 46
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-1, y-1, z-1, x+1, y-2, z+1, tnt, 1)

def LTntB():
    tnt = 46
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-2, y-2, z-2, x+2, y-5, z+1, tnt, 1)


def placeLava():
    lava = 10
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, lava, 1)

def volc():
    x, y, z = mc.player.getPos()


    lava = 10
    water = 8
    air = 0
    h = 0
    mc.setBlocks(x-5, y, z-5, x+5, y+60, z+5, air)

    r = True
    while r == True:
        time = random.randint(10, 30)
        sleep(time)
        time = random.randint(10, 60)


        mc.setBlock(x, y+h, z, lava)
        sleep(time)
        mc.setBlock(x, y+h, z, water)
        sleep(time/2)
        mc.setBlock(x, y+h, z, air)
        h = h+1

"""
BLOCKS
    air                 = Block(0)
    STONE               = Block(1)
    GRASS               = Block(2)
    DIRT                = Block(3)
    COBBLESTONE         = Block(4)
    WOOD_PLANKS         = Block(5)
    SAPLING             = Block(6)
    BEDROCK             = Block(7)
    WATER_FLOWING       = Block(8)
    WATER               = WATER_FLOWING
    WATER_STATIONARY    = Block(9)
    LAVA_FLOWING        = Block(10)
    LAVA                = LAVA_FLOWING
    lava_stationary     = Block(11)
    SAND                = Block(12)
    GRAVEL              = Block(13)
    GOLD_ORE            = Block(14)
    IRON_ORE            = Block(15)
    COAL_ORE            = Block(16)
    WOOD                = Block(17)
    LEAVES              = Block(18)
    GLASS               = Block(20)
    LAPIS_LAZULI_ORE    = Block(21)
    LAPIS_LAZULI_BLOCK  = Block(22)
    SANDSTONE           = Block(24)
    BED                 = Block(26)
    COBWEB              = Block(30)
    GRASS_TALL          = Block(31)
    WOOL                = Block(35)
    FLOWER_YELLOW       = Block(37)
    FLOWER_CYAN         = Block(38)
    MUSHROOM_BROWN      = Block(39)
    MUSHROOM_RED        = Block(40)
    GOLD_BLOCK          = Block(41)
    IRON_BLOCK          = Block(42)
    STONE_SLAB_DOUBLE   = Block(43)
    STONE_SLAB          = Block(44)
    BRICK_BLOCK         = Block(45)
    TNT                 = Block(46)
    BOOKSHELF           = Block(47)
    MOSS_STONE          = Block(48)
    OBSIDIAN            = Block(49)
    TORCH               = Block(50)
    FIRE                = Block(51)
    STAIRS_WOOD         = Block(53)
    CHEST               = Block(54)
    DIAMOND_ORE         = Block(56)
    DIAMOND_BLOCK       = Block(57)
    CRAFTING_TABLE      = Block(58)
    FARMLAND            = Block(60)
    FURNACE_INACTIVE    = Block(61)
    FURNACE_ACTIVE      = Block(62)
    DOOR_WOOD           = Block(64)
    LADDER              = Block(65)
    STAIRS_COBBLESTONE  = Block(67)
    DOOR_IRON           = Block(71)
    REDSTONE_ORE        = Block(73)
    SNOW                = Block(78)
    ICE                 = Block(79)
    SNOW_BLOCK          = Block(80)
    CACTUS              = Block(81)
    CLAY                = Block(82)
    SUGAR_CANE          = Block(83)
    FENCE               = Block(85)
    GLOWSTONE_BLOCK     = Block(89)
    BEDROCK_INVISIBLE   = Block(95)
    STONE_BRICK         = Block(98)
    GLASS_PANE          = Block(102)
    MELON               = Block(103)
    FENCE_GATE          = Block(107)
    GLOWING_OBSIDIAN    = Block(246)
    NETHER_REACTOR_CORE = Block(247)
"""
