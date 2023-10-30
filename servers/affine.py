#!/usr/bin/env python3

import base64
import string

def affine_encode(plaintext, a, b):
    ciphertext = ""
    for c in plaintext:
        if c.isupper():
            ciphertext += chr(((ord(c) - ord("A")) * a + b) % 26 + ord("A"))
        else:
            ciphertext += chr(((ord(c) - ord("a")) * a + b) % 26 + ord("a"))
    return ciphertext

INFO = "hypotenuse"
FLAG = "triangle"

print("\nYou find this note on the slope of a hill. It reads:\n")

print("|\\")
print("| \\")
print("|  \\  /\\")
print("|   \\/  \\")
print("|        \\")
print("|         \\")
print("|   --- T H\\")
print("|           \\")
print("|       --- O\\")
print("|             \\    /\\")
print("|     --- T R I\\  /N \\      /\\")
print("|               \\/    \\    /  \\")
print("|                      \\  /    \\")
print("|                       \\/      \\")
print("|      2   2   2                 \\       ")
print("|     a + b = c                   \\      ")
print("|                                  \\/\\     ")
print("|                                     \\ ")
print("|                                      \\ ")
print("|            obtuse                     \\/\\ ")
print("|                                          |")
print("|                                          |")
string = affine_encode(INFO, 5, 8)
print("|" + " " * ((42 - len(string)) // 2) + string + " " * ((42 - len(string)) // 2) + "|")
print("|                                          |")
print("|                                          |")
print("|                    ______________________|")
print("|___________________/                   \n")

while True:
    inp = input("What could this mean? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")