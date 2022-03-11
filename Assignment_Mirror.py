# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:57:16 2022

@author: 105043702
"""
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")