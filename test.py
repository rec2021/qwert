#!/usr/bin/env python
# encoding: utf-8

from qwert import FileCache

fc = FileCache('qwert')

a = 'hahahaha'

print(fc.put('a', a))

b = fc.get('a')
print(b)

c = fc.pull('a')
print(c)

d = fc.get('a')
print(d)
