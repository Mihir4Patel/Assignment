# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:33:56 2022

@author: 105043702
"""

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))