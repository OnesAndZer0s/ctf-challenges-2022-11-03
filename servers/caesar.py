#!/usr/bin/env python3

import random

from .util import caesar_shift, randstring

for i in range(1024):
    n = random.randint(1, 25)
    s = randstring(25)
    print(f"Shift this string by {n} letters: {s}")

    c = caesar_shift(s, n)
    a = input("Encrypted version: ").strip()
    if a != c: break
else:
    print("Correct.")

print("Wrong.")
