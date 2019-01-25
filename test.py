#!/usr/bin/env python
# encoding: utf-8

from qwert import dict_fn

a = {
    'abc': 1,
    'abd': 12,
    'abe': 123,
    'abf': 1234,
    'xx': 12345,
    'yy': 1123456,
}

d = {
    'abe': 'go',
    'abf': 'media',
    'xe': 'halo',
}

j = '{"abc": 1, "abd": 12, "abe": 123, "abf": 1234, "xx": 12345, "yy": 1123456}'

print(dict_fn.get_dict_by_keys(j, d))
