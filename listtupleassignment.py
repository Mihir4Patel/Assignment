# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:15:21 2022

@author: 105043702
"""

def last(n): return n[-1]  
  
def sort_list_last(tuples):  
  return sorted(tuples, key=last)  
  
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))