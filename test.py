#!/usr/bin/env python
# encoding: utf-8
from qwert import text_fn
#
# address, private_key = ethereum.generate_address_and_private_key()
#
# print(address, private_key)

a = 10000

print(text_fn.gram_align_right('{:.2f} VNET'.format(a)))
