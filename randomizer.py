from random import randint
from collections import deque

ramFile = open("RAM.txt", "w")
RAM = ["" for _ in range(2048)]
for i in range(2048):
    RAM[i] = format(randint(0, 255), '08b') + "\n"
ramFile.writelines(RAM)
ramFile.close()

a = "00011111111"
print(f'Tag: {a[0:3]}, Index: {a[3:8]}, Offset: {a[8:11]}')
lista = deque()
lista.appendleft(5)
def something(lista):
    lista.appendleft(6)
    lista.appendleft(7)
something(lista)
print(lista)
print(lista.pop())
print(lista)

string = "Hola"
listica = list(string)
print(listica)
stringnuevo = "".join(listica)
print(stringnuevo)