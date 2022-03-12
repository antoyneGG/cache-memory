from sys import stdin

hex_bin = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}

bin_hex = {
    "0000" : "0",
    "0001" : "1",
    "0010" : "2",
    "0011" : "3",
    "0100" : "4",
    "0101" : "5",
    "0110" : "6",
    "0111" : "7",
    "1000" : "8",
    "1001" : "9",
    "1010" : "A",
    "1011" : "B",
    "1100" : "C",
    "1101" : "D",
    "1110" : "E",
    "1111" : "F"
}

hex_decimal = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}

def checkHex(num):
    if(num[:2] == "0x"):
        return True
    return False

def checkNum2(num):
    num = str(num)
    for i in num:
        if(i != "0" and i != "1"):
            return True
    return False

def checkNum(num):
    if(num.isdigit()):
        return True
    return False

def HexToBin(num):
    hex = num[2:]
    for i in hex:
        if(i == "0"):
            hex = hex[1:]
    binarie = ""
    for i in hex:
        binarie += hex_bin[i]
    return binarie

def DecimalToBin(num):
    num = abs(int(num))
    binarie = ""
    while(num != 0):
        binarie += str(num%2)
        num = num//2
    return binarie[::-1]

def HexToDecimal(num):
    hex = num[2:]
    pot = int(len(hex) - 1)
    decimal = 0
    for i in hex:
        decimal += hex_decimal[i] * (16**pot)
        pot -= 1
    return decimal

def BinToHex(num):
    hex = "0x"
    while(len(num)%4 != 0):
        num = num.zfill(len(num)+1)
    first = 0
    last = 4
    while(last != len(num)):
        hex += bin_hex[num[first:last]]
        first += 4
        last += 4
    hex += bin_hex[num[first:last]]
    return hex

def BinToDecimal(num):
    decimal = 0
    exp = 0
    num = int(num)
    while(num != 0):
        decimal += (2**exp)*(num%10)
        num = num//10
        exp += 1
    return str(decimal)



