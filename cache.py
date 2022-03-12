from functools import cache
from ram import readRam, updateRAM, writeRam
from conversions import BinToDecimal
from collections import deque

class CacheBlock:
    def __init__(self, dirtyBit, validBit, address, data):
        self.dirtyBit = dirtyBit
        self.validBit = validBit
        self.address = address
        self.data = data

class CacheMemory:
    def __init__(self, blockSize, depth):
        self.blockSize = blockSize
        self.depth = depth
        self.cache = [CacheBlock("0", "0", "00000000", "0000000000000000000000000000000000000000000000000000000000000000") for _ in range(depth)]
        self.isFull = False
        self.LRU = deque()

def readCache(address, RAM, cacheMem):
    blockAdd = address[0:8]
    offset = address[8:11]
    for block in cacheMem.cache:
        if(block.address == blockAdd):
            if(blockAdd not in cacheMem.LRU):
                cacheMem.LRU.appendleft(blockAdd)
            else:
                cacheMem.LRU.remove(blockAdd)
                cacheMem.LRU.appendleft(blockAdd)
            return 1
    for block in cacheMem.cache:
        if(block.validBit == "0"):
            block.validBit = "1"
            block.address = blockAdd
            init = int(BinToDecimal(blockAdd + "000"))
            end = int(BinToDecimal(blockAdd + "111"))
            block.data = RAM[init]
            for d in range(init + 1, end + 1):
                block.data += RAM[d]
            cacheMem.LRU.appendleft(blockAdd)
            return 0
    replacement = cacheMem.LRU.pop()
    for block in cacheMem.cache:
        if(block.address == replacement):
            newInit = int(BinToDecimal(block.address + "000"))
            newEnd = int(BinToDecimal(block.address + "111"))
            block.address = blockAdd
            init = int(BinToDecimal(blockAdd + "000"))
            end = int(BinToDecimal(blockAdd + "111"))
            dataR = block.data
            block.data = RAM[init]
            for d in range(init + 1, end + 1):
                block.data += RAM[d]
            if(block.dirtyBit == "1"):
                updateRAM( newInit, newEnd, dataR, RAM )
                block.dirtyBit = "0"
            cacheMem.LRU.appendleft(blockAdd)
            return 0

def writeCache(address, cacheMem, newData, RAM):
    blockAdd = address[0:8]
    offset = address[8:11]

    for block in cacheMem.cache:
        if(block.address == blockAdd):
            writeD = list(block.data)
            writeD[int(BinToDecimal(offset))*8:(int(BinToDecimal(offset))*8)+8] = newData
            block.data = "".join(writeD)
            block.dirtyBit = "1"
            if(blockAdd not in cacheMem.LRU):
                cacheMem.LRU.appendleft(blockAdd)
            else:
                cacheMem.LRU.remove(blockAdd)
                cacheMem.LRU.appendleft(blockAdd)
            return 1
    for block in cacheMem.cache:
        if(block.validBit == "0"):
            block.dirtyBit = "1"
            block.validBit = "1"
            block.address = blockAdd
            init = int(BinToDecimal(blockAdd + "000"))
            end = int(BinToDecimal(blockAdd + "111"))
            block.data = RAM[init]
            for d in range(init + 1, end + 1):
                block.data += RAM[d]
            writeD = list(block.data)
            writeD[int(BinToDecimal(offset))*8:(int(BinToDecimal(offset))*8)+8] = newData
            block.data = "".join(writeD)
            cacheMem.LRU.appendleft(blockAdd)
            return 0
    replacement = cacheMem.LRU.pop()
    for block in cacheMem.cache:
        if(block.address == replacement):
            newInit = int(BinToDecimal(block.address + "000"))
            newEnd = int(BinToDecimal(block.address + "111"))
            block.address = blockAdd
            init = int(BinToDecimal(blockAdd + "000"))
            end = int(BinToDecimal(blockAdd + "111"))
            dataR = block.data
            block.data = RAM[init]
            for d in range(init + 1, end + 1):
                block.data += RAM[d]
            if(block.dirtyBit == "1"):
                updateRAM( newInit, newEnd, dataR, RAM )
                block.dirtyBit = "0"

            block.dirtyBit = "1"
            writeD = list(block.data)
            writeD[int(BinToDecimal(offset))*8:(int(BinToDecimal(offset))*8)+8] = newData
            block.data = "".join(writeD)
            cacheMem.LRU.appendleft(blockAdd)
            return 0