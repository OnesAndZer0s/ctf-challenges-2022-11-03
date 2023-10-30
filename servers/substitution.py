#!/usr/bin/env python3

from ctypes import wstring_at
import random
import string
from binascii import hexlify, unhexlify

def alphabetical_substitution_encode(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        if ord(c) - ord("a") >= len(key) or ord(c) - ord("a") < 0:
            ciphertext += c
        else:
            ciphertext += key[ord(c) - ord("a")]
    return ciphertext

KEY = "maroon"
ALPHABET = "zyxwvutsrqponmlkjihgfedcba"
INFO = "my favorite color is maroon.\nhow is your day today?\n my day is good.\n i hope you are having a good day."
FLAG = "substitution"
print("\nAn english major slips you a note, thinking you cannot read it. It reads:\n")

print(" ____________________________________")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")

# shift each character by the next value in the LCG
string = alphabetical_substitution_encode(INFO, ALPHABET)
# split the string, and run a for loop for each newline
for line in string.split("\n"):
    print("|" + " " * ((36 - len(line)) // 2) + line + " " * ((37 - len(line)) // 2) + "|")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|____________________________________|\n")

while True:
    inp = input("What is the teachers favorite color? ").strip()
    if inp == KEY:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")