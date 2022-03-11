# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:45:19 2022

@author: 105043702
"""

nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))