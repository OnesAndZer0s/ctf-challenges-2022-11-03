#!/usr/bin/env python3

import random
import string

def caesar_shift(s, n):
    alpha = string.ascii_lowercase + string.ascii_uppercase
    translated = string.ascii_lowercase[n:] + string.ascii_lowercase[:n] + string.ascii_uppercase[n:] + string.ascii_uppercase[:n]
    tab = str.maketrans(alpha, translated)

    s2 = ""
    for c in s:
        if c in string.ascii_letters:
            s2 += c.translate(tab)
        else:
            s2 += c
    return s2

for i in range(1024):
    n = random.randint(1, 25)
    s = "".join(random.choices(string.ascii_letters, k=25))
    print(f"Shift this string by {n} letters: {s}")

    c = caesar_shift(s, n)
    a = input("Caesar-Shifted String: ").strip()
    if a != c:
        print(f"Nope, the answer was {c}")
        break
else:
    print("Correct.")
