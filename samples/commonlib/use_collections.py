#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('ooint', ['x', 'y'])
p = Point(1, 2)
print(type(p))
print('Point:', p.x, p.y)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)#Counter 对象
d=dict(c)#转成字典
print(d)
b=list(d)#字典中的key
print(b)
a=list(d.values())#字典中的key的值
print(a)
