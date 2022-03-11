# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:47:44 2022

@author: 105043702
"""

def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))