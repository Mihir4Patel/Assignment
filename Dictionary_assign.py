# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:19:35 2022

@author: 105043702
"""

# Create the dictionary
my_dict = {}

# Now populate it
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dict[chr(i)] = i

# Print the populated dictionary
print(my_dict)