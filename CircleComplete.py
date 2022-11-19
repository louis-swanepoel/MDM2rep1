#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:31:21 2022

@author: huw
"""
from numpy import linspace,array,transpose
from matplotlib import pyplot as plt

def Plot(x,y):
    plt.title("CIRCLE") 
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.plot(x,y) 
    plt.show()

    
def CircleGenerator(Time,t,SpeedOfSound,StartingPoint,SpeedOfParticle,Frequency,XRange):
    YRange=[]
    NewStartingPoint=StartingPoint+t*SpeedOfParticle
    for x in XRange:
        YSquared=((Time-t)*SpeedOfSound)**2-(x-NewStartingPoint[0])**2
        if YSquared<0:
            y=[0,0]
            YRange.append(y)
            
        else:
            y=[YSquared**0.5+NewStartingPoint[1], -YSquared**0.5+NewStartingPoint[1]]
            YRange.append(y)
    return YRange


def COMPILE(range1,range2):
    
    MainSize=len(range1)
    MainSizeRange=linspace(0,MainSize-1,MainSize)
    LittleSize=len(range2[0])
    LittleSizeRange=linspace(0,LittleSize-1,LittleSize)
    for a in MainSizeRange:
        for b in LittleSizeRange:
            range1[int(a)].append(range2[int(a)][int(b)])
    return range1


Time=5
Frequency=2
TimeRange=linspace(Time/(Frequency*Time),Time,Frequency*Time)
SpeedOfSound=1
StartingPoint=array([0,0])
XRange=(linspace(0,5,1000))
SpeedOfParticle=array([1,0])
Y0=CircleGenerator(Time,0,SpeedOfSound,StartingPoint,SpeedOfParticle,Frequency,XRange)
#print(Y0)
for t in TimeRange:
    Y1=CircleGenerator(Time,t,SpeedOfSound,StartingPoint,SpeedOfParticle,Frequency,XRange)
    Y0=COMPILE(Y0,Y1)
Plot(XRange,Y0)
