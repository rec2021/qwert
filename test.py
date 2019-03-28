#!/usr/bin/env python
# encoding: utf-8
from qwert import ethereum

address, private_key = ethereum.generate_address_and_private_key()

print(address, private_key)

