# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:27:59 2022

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