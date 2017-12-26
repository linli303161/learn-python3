#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('E:\\')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    f=os.path.join(pwd,f)   #注意要整合文件路径；
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
