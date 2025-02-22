#!/usr/bin/env python3

import string

def caesar_encode(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        if c.isupper():
            ciphertext += chr((ord(c) - ord("A") + key) % 26 + ord("A"))
        else:
            ciphertext += chr((ord(c) - ord("a") + key) % 26 + ord("a"))
    return ciphertext

INFO = "stab wounds"
FLAG = "salad"
KEY = 14
print("\nYou find a prophetic carving written in marble. It reads:\n")

print(" ___________                                         ___________ ")
print("|           |_______________________________________|           |")
print("|___________|                                       |___________|")
print("   | | | |                                             | | | | ")
print("   | | | |                                             | | | | ")
print("   | | | |                    CAESAR                   | | | | ")
print("   | | | |                                             | | | | ")
print("   | | | |                    WILL                     | | | | ")
print("   | | | |                                             | | | | ")
print("   | | | |                    DIE                      | | | | ")
print("   | | | |                                             | | | | ")
print("   | | | |                    BY                       | | | | ")
print("   | | | |                                             | | | | ")
string = caesar_encode(INFO, KEY)
print("   | | | |" + " " * ((46 - len(string)) // 2) + string + " " * ((45 - len(string)) // 2) + "| | | |   ")
print("   | | | |                                             | | | | ")
print("   | | | |                                             | | | | ")
print(" __|_|_|_|__                                         __|_|_|_|__ ")
print("|           |_______________________________________|           |")
print("|___________|                                       |___________|\n")

while True:
    inp = input("How will Caesar die? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")