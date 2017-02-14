# Mod-Divmod
# https://www.hackerrank.com/challenges/python-mod-divmod

from __future__ import division
a = int(raw_input())
b = int(raw_input())

first = a // b
second = a % b
print(first)
print(second)
print((first, second))
