#!/usr/bin/env python3

import random

from .util import caesar_shift, randstring

for i in range(1024):
    n = random.randint(1, 25)
    s = randstring(25)
    print(caesar_shift(f"This string is rotated by an unknown amount: {s}", n))

    a = input("Original string: ").strip()
    if a != s: break
else:
    print("Correct.")

print("Wrong.")
