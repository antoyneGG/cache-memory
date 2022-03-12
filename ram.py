from conversions import DecimalToBin, HexToBin, checkHex, checkNum2

def writeRam( RAM ):
    ramFile = open("RAM.txt", "w")
    for i in range(2048):
        RAM[i] += "\n"
    ramFile.writelines(RAM)
    ramFile.close()

def checkRAM( RAM ):
    if(len(RAM) > 2048 or len(RAM) < 2048):
        raise TypeError("Invalid RAM size in RAM.txt")
    for i in range(len(RAM)):
        if(checkHex(RAM[i])):
            RAM[i] = HexToBin(RAM[i])
            RAM[i] = RAM[i].zfill(8)
        if(checkNum2(RAM[i])):
            RAM[i] = DecimalToBin(RAM[i])
            RAM[i] = RAM[i].zfill(8)
        if(len(RAM[i]) > 8 or len(RAM[i]) < 8):
            raise TypeError(f'Invalid lenght of {RAM[i]}')

def readRam():
    ramFile = open("RAM.txt", "r")
    RAM = [line.rstrip() for line in ramFile.readlines()]
    ramFile.close()
    return RAM

def updateRAM( init, end, data, RAM ):
    cont1 = 0
    cont2 = 8
    for d in range(init, end + 1):
        RAM[d] = data[cont1:cont2]
        cont1 += 8
        cont2 += 8