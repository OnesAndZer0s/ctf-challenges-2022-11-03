#!/usr/bin/env python3

from ctypes import wstring_at
import random
import string
from binascii import hexlify, unhexlify

primes = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063,
          1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
          1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229,
          1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301,
          1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409,
          1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481,
          1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553,
          1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619,
          1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709,
          1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789,
          1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879,
          1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,
          1993, 1997, 1999]

def lcg(m, a, c, s):
    while True:
        s = (a * s + c) % m
        yield s

g = lcg(1667, 43, 11, 1023)

INFO = "you look stupid"
FLAG = "congruence"
print("\nA mathematician slips you a note, thinking you cannot read it. It reads:\n")

print(" ____________________________________")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")

# shift each character by the next value in the LCG
string = "".join([chr(ord(c) + next(g)) for c in INFO])
print("|" + " " * ((40 - len(string)) // 2) + string + " " * ((40 - len(string)) // 2) + "|")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                                    |")
print("|                 :)                 |")
print("|                                    |")
print("|                                    |")
print("|____________________________________|\n")

while True:
    inp = input("What does it say? ").strip()
    if inp == INFO:
        print(f'Correct. gopher{"{"+FLAG+"}"}')
        break
    else:
        print("Wrong.")