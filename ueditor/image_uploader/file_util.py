# -*- coding: utf-8 -*-
'''
Created on 2013-5-10

@author: xiaoxuwang
'''

import re
import os.path
import random
from datetime import datetime


#在上传的文件名后面追加一个日期时间+随机,如abc.jpg--> abc_20120801202409.jpg
def make_rand_filename(filename):
    name, ext = os.path.splitext(filename)
    dt_str = datetime.now().strftime("%Y%m%d_%H%M%S_")
    return "%s_%s%s%s" % (name, dt_str, random.randrange(10, 99), ext)


_size_unit = (
        ('Byte', 1),
        ('KB', 1024),
        ('MB', 1024*1024),
        ('GB', 1024*1024*1024),
        ('TB', 1024*1024*1024*1024)
)


def get_friendly_size(size):
    for u, s in _size_unit:
        if size / s < 1024:
            break
    return ((size % s == 0) and
            str(size / s) + u or
            '%.2f' % (size / float(s)) + u)


def get_byte_size(size):
    if isinstance(size, int, long):
        return size
    if isinstance(size, basestring):
        pattern = re.compile(r'(\d*\.?(?=\d)\d*)\s*(Byte|KB|MB|GB|TB)', re.I)
        m = pattern.match(size.strip())
        if m:
            s, u = m.groups()
            try:
                s = float(s)
            except ValueError:
                return 0
            s *= dict(_size_unit).get(u.upper(), 1)
            return long(s)
    return 0

