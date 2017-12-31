# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:13:08 2017

@author: likitha
"""

def pow(x,n):
    r=1
    if (x==1):
        return(x)
    if (x!=1):
        for i in range(n):
            t=int(x)
            r=int(r*t)
        print(r)
x= int(input("enter the number?" )) 
n= int(input("enter the power?" )) 
pow(x,n)