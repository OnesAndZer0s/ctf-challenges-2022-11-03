#!/usr/bin/env python3

import random
from binascii import hexlify, unhexlify

from .util import randstring, xor

for i in range(1024):
    n = random.randint(5, 10)
    k = randstring(n)
    print(f"The key is {n} letters long.")

    s = randstring(25)
    sh = hexlify(s.encode("utf-8"))
    print(f"Hex(Original string): {sh}")

    e = hexlify(xor(s, k))
    print(f"Hex(Xor(Encrypted, Key)): {e}")

    ah = input("Hex(Key): ").strip()
    a = unhexlify(ah)
    if a != k: break
else:
    print("Correct.")

print("Wrong.")
