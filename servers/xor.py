#!/usr/bin/env python3

import random
import string
from binascii import hexlify, unhexlify



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

# for i in range(1024):
#     n = random.randint(5, 10)
#     k = "".join(random.choices(string.ascii_letters, k=n))
#     print(f"The key is {n} letters long.")

#     s = "".join(random.choices(string.ascii_letters, k=25))
#     sh = hexlify(s.encode("utf-8"))
#     print(f"Hex(Original string): {sh}")
#     e = hexlify(xor(s, k))
#     print(f"Hex(Xor(Encrypted, Key)): {e}")

#     ah = input("Hex(Key): ").strip()
#     a = unhexlify(ah).decode("utf-8")
#     if a != k:
#         kh = hexlify(k.encode("utf-8"))
#         print(f"Nope, the answer was {kh}")
#         break
# else:
#     print("Correct.")

while True:
    inp = input("What is your computer looking for? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")