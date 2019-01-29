#!/usr/bin/python
# -*- coding: UTF-8 -*-

import redis


re = redis.Redis(
    host = '127.0.0.1',
    port = 6379
)

re.set('test1','cherish')