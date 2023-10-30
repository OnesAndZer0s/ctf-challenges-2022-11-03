#!/usr/bin/env python3

import base64
import string

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
          'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
          'U': 'babaa', 'V': 'babab', 'W': 'babaa', 'X': 'babab', 'Y': 'babba',
          'Z': 'babbb', ' ': ' '}
def encrypt(message):
    """Ecrypt the string according to the cipher provided."""
    # return ''.join(map(lookup.get, message))
    encrypted = []
    for letter in message:
        encrypted.append(lookup[letter])
    return ''.join(encrypted)    

INFO = "porkchop"
FLAG = "bacon"
print("\Outside of a pig barn, you find a poster on the door. It reads:\n")

print(" __________________________________________")
print("|                                          |")
print("|  X                                    X  |")
print("|         --- BEWARE THE PIGS ---          |")
print("|                                          |")
string = encrypt(INFO.upper())
print("|" + " " * ((42 - len(string)) // 2) + string + " " * ((42 - len(string)) // 2) + "|")
print("|                                          |")
print("|                   __    _________  _____ |")
print("|        _  _______/  \__/         \/     \|")
print("|__/\___/ \/                               \n")

while True:
    inp = input("What could this mean? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")