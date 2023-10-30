#!/usr/bin/env python3

import string
from binascii import hexlify

def xor(p, k):
    s = []
    for i, c in enumerate(p):
        kc = k[i % len(k)]
        s.append(ord(c) ^ ord(kc))
    return bytearray(s)

INFO = "information"
FLAG = "computer"
KEY = "redacted"

print("\nOne day, your printer spits out a rogue piece of paper. It reads:\n")

print(" ____________________________________")
print("|                                    |")
print("|                                    |")
print("|   H E L L O                        |")
print("|                                    |")
print("|                                    |")
print("|   I   A M   Y O U R                |")
print("|   C O M P U T E R .                |")
print("|                                    |")
print("|                                    |")
print("|   G I V E                          |")
print("|   M E                              |")
string = hexlify(xor(INFO, KEY))
print("|" + " " * ((28 - len(string)) // 2) + string.decode("utf-8") + " " * ((44 - len(string)) // 2) + "|")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|            T H A N K   Y O U ,     |")
print("|                                    |")
print("|              -  C O M P U T E R    |")
print("|                                    |")
print("|                                    |")
print("|____________________________________|\n")

while True:
    inp = input("What is your computer looking for? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")