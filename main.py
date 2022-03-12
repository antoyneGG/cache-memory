from random import randint
from sys import stdin
from cache import CacheBlock, CacheMemory, readCache, writeCache
from ram import checkRAM, readRam, writeRam

def showCache( cacheMem ):
    print("D|V|-ADDRESS|--------------------------DATA----------------------------------")
    for block in cacheMem.cache:
        print(f'{block.dirtyBit}|{block.validBit}|{block.address}|{block.data}')

def showRAM( RAM ):
    print("--RAM---")
    for i in range(len(RAM)):
        print(f'{RAM[i]} in {i + 1}')

def generateOutput( cacheMem, hits, misses ):
    file = open("finalCache.txt", "w")
    file.write("D|V|-ADDRESS|----------------------DATA--------------------------------------\n")
    for block in cacheMem.cache:
        file.write(f'{block.dirtyBit}|{block.validBit}|{block.address}|{block.data}\n')
    if(hits > 0 or misses > 0):
        file.write(f'Hits: {(hits * 100)/(hits + misses):.2f}% / Misses: {(misses * 100)/(hits + misses):.2f}%\n')
    else:
        file.write(f'Hits: 0% / Misses: 0%\n')
    file.close()


def main():
    try:
        print("|----------------FULLY ASSOCIATIVE CACHE MEMORY - WRITE BACK AND LRU POLICYS-----------------|")
        print("----SPECS:\n-Depth: 32 blocks\n-Block size: 8 bytes")
        print("OPTIONS:\n0. Read Cache\n1. Write Cache\n2. Total hits/misses\n3. Print Cache\n4. Print RAM\n5. Exit")
        RAM = readRam()
        checkRAM( RAM )
        cacheMem = CacheMemory(8, 32)
        hits = 0
        misses = 0
        option = int(stdin.readline())
        while(option != 5):
            try:
                if(option > 5 or option < 0):
                    raise TypeError("ERROR: Invalid option")
                if(option == 0):
                    address = format(randint(0, 2047), '011b')
                    print(f'{address}')
                    if(readCache(address, RAM, cacheMem) == 1):
                        hits += 1
                    else:
                        misses += 1
                if(option == 1):
                    address = format(randint(0, 2047), '011b')
                    print(f'{address}')
                    data = format(randint(0, 255), '08b')
                    print(f'{data}')
                    if(writeCache(address, cacheMem, data, RAM) == 1):
                        hits += 1
                    else:
                        misses += 1
                if(option == 2):
                    if(hits > 0 or misses > 0):
                        print(f'Hits: {(hits * 100)/(hits + misses):.2f}% / Misses: {(misses * 100)/(hits + misses):.2f}%\n')
                    else:
                        print(f'Hits: 0% / Misses: 0%\n')
                if(option == 3):
                    showCache( cacheMem )
                if(option == 4):
                    showRAM( RAM )
                if(option == 5):
                    print("See you.")
            except TypeError as error:
                print(error)
            option = int(stdin.readline())
        writeRam( RAM )
        generateOutput( cacheMem, hits, misses )
    except TypeError as error:
        print(error)

main()
