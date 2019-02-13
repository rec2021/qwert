#!/usr/bin/env python
# encoding: utf-8

from qwert import file_fn

a = {
    'abc': 1,
    'abd': 12,
    'abe': 123,
    'abf': 1234,
    'xx': 12345,
    'yy': 1123456789,
}

r = file_fn.cache_to_file('qwert-test', a)
print(r)

r = file_fn.read_cache_from_file('qwert-test', remove=True)
print(r)

