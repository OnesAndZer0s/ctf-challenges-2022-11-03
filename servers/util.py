import string
import random

def randstring(n):
    return "".join(random.choices(string.ascii_letters, k=n))

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

def xor(p, k):
    s = []
    for i, c in enumerate(p):
        kc = k[i % len(k)]
        s.append(ord(c) ^ ord(kc))
    return bytearray(s)

