#!/usr/bin/env python3

import random
import string
from binascii import hexlify, unhexlify

def xor(p, k):
    s = []
    for i, c in enumerate(p):
        kc = k[i % len(k)]
        s.append(ord(c) ^ ord(kc))
    return bytearray(s)

for i in range(1024):
    n = random.randint(5, 10)
    k = "".join(random.choices(string.ascii_letters, k=n))
    print(f"The key is {n} letters long.")

    s = "".join(random.choices(string.ascii_letters, k=25))
    sh = hexlify(s.encode("utf-8"))
    print(f"Hex(Original string): {sh}")
    e = hexlify(xor(s, k))
    print(f"Hex(Xor-Encrypted): {e}")

    ah = input("Hex(Key): ").strip()
    a = unhexlify(ah)
    if a != k: break
else:
    print("Correct.")

print("Wrong.")
