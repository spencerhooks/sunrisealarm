#!/usr/bin/python

a = 255
b = 150

c = a/b+1 if a%b>0 else a/b

for i in range(b):
    a = max(0, a-c)
    print(a)
