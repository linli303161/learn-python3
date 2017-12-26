#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'hello', b'lin', b'li']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 10001))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()
