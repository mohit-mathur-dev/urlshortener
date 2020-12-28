# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:39:09 2020

@author: Mohit Mathur
"""

import pyshorteners

url= input("Enter your URL:")
short= pyshorteners.Shortener()
a=short.tinyurl.short(url)
print(a)