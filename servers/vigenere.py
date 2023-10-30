#!/usr/bin/env python3

import string

def vig_encode(plaintext, key):
    ciphertext = ""
    for i, c in enumerate(plaintext):
        shift = ord(key[i % len(key)]) - ord("a")
        if c.isupper():
            ciphertext += chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
        else:
            ciphertext += chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
    return ciphertext

INFO = "glasses"
FLAG = "sight"
KEY = "eye"
print("\nYou find a note written by a visionary. It reads:\n")

print("                              _  __  ______")
print("               __  __________/ \/  \/      |")
print("|\____________/  \/                        |")
print("|                                          |")
print("|   HELP!!                                 |")
print("|                                     ____/")
print("|     I was working on my greatest fe/     ")
print("|  yet, but for some reason, my ____/      ")
print("|                              /           ")
print("|      I                       \_________  ")
print("|          need                          \_")

string = vig_encode(INFO, KEY)
print("|" + " " * ((43 - len(string)) // 2) + string + " " * ((42 - len(string)) // 2) + "|")
print("|                                          |")
print("|                       __    _________  __|")
print("|   ____     _  _______/  \__/         \/  ")
print("|__/    \___/ \/                           \n")

while True:
    inp = input("What does this visionary need? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")