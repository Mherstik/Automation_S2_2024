#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:30:42 2024

@author: marcus
"""

a = [631, 53, 53]
print(type(a))
mod = str(a)
moda = str(a).replace(',', ';')
moda = moda.strip('[]')

modb = str(a).replace(',', ';').strip('[]')
print(moda)
print(modb)
