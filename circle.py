#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:55:03 2022

@author: huw
"""

def Circle(t,v,x0,y0,x):
    
    bigy=(t*v)**2 - (x-x0)**2
    if bigy<0:
        return 'x value not in circle'
    else:
        yvalue1=(bigy**0.5+y0)
        yvalue2=-(bigy**0.5+y0)

        return x,yvalue1,yvalue2
def CircleOutput(values):

    if values[1]==values[2]:
        return values[0], values[1]
    else:
        return values[0], values[1], values[2]

StartingPositionX=0
StartingPositionY=0
v=1
SecondPositionX=5
SecondPositionY=0
t=5
givenpoint=5

circle1=(Circle(t,v,StartingPositionX,StartingPositionY,givenpoint))

circle2=Circle(t-1,v,SecondPositionX,SecondPositionY,givenpoint)

print(CircleOutput(circle1))
print(CircleOutput(circle2))

T=(linspace(0,10,11))
for t in T:
    NewPositionX=StartingPositionX+t*v
    NewPositionY=StartingPositionY+t*v
    print(CircleOutput((Circle(t,v,NewPositionX,NewPositionY,givenpoint))))
