#!/usr/bin/env python3

import base64
import string

INFO = "they are out for your cheese"
FLAG = "four"
print("\nYou find a note on the ground in the city, at the base of a skyscraper. It reads:\n")

print(" _     __  _       __  _    _      _  _  __")
print("| \  _/  \/ \   /\/  \/ \/\/ \__  / \/ \/  |")
print("|  \/        \_/                \/         |")
print("|                                          |")
print("|   --- TO WHOEVER THIS MAY CONCERN ---    |")
print("|                                          |")
string = base64.b64encode(INFO.encode("ascii")).decode("ascii")
print("|" + " " * ((42 - len(string)) // 2) + string + " " * ((42 - len(string)) // 2) + "|")
print("|                                          |")
print("|   --- TO WHOEVER THIS MAY CONCERN ---    |")
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