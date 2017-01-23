#!/usr/bin/python

from __future__ import division

#
# a = 255
# b = 150
#
# c = a/b+1 if a%b>0 else a/b
#
# for i in range(b):
#     a = max(0, a-c)
#     print(a)


foo = 150
bar = 120

delta = foo / bar

count = 0
while foo > 0:
  count += 1
  foo -= delta
  print(int(round(max(0, foo))))

print count-1
