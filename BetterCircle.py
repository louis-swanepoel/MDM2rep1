#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:56:28 2022

@author: huw
"""

from numpy import linspace
from matplotlib import pyplot as plt



    
def CircleGenerator(Time,SpeedOfSound,StartingPoint,XRange):
    YRange=[]
    for x in XRange:
        YSquared=(Time*SpeedOfSound)**2-(x-StartingPoint[0])**2
        if YSquared<0:
            return 
        else:
            y=(YSquared**0.5+StartingPoint[1], -YSquared**0.5+StartingPoint[1])
            YRange.append(y)
    return YRange

X=linspace(0,1,11)
YRange=(CircleGenerator(1,1,(0,0),X))
print(YRange)

plt.title("CIRCLE") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(X,YRange) 
plt.show()       #plot comes out a bit  funky at the end but i think its due x intervals
