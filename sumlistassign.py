# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:32:13 2022

@author: 105043702
"""

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))