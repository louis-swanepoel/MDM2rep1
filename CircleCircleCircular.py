#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:28:23 2022

@author: huw
"""

from math import floor
from numpy import sin,cos,linspace,pi,array
from matplotlib import pyplot as plt

def Plot(x,y):
        plt.title("CIRCLE") 
        plt.xlabel("x") 
        plt.ylabel("y") 
        plt.plot(x,y) 
        plt.show()

def CircleGenerator(TotalTime,t,SpeedOfSound,StartingPoint,XRange):
    YRange=[]
    for x in XRange:
        YSquared=((TotalTime-t)*SpeedOfSound)**2-(x-StartingPoint[0])**2
        if YSquared<0:
            y=[None,None]
            YRange.append(y)
            
        else:
            y=[YSquared**0.5+StartingPoint[1], -YSquared**0.5+StartingPoint[1]]
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

def CircularCircle(TotalTime,TimeRange,StartingPoint,XRange,RadiusOfCircle,SpeedOfSound):
    Y0=CircleGenerator(TotalTime,0, SpeedOfSound,StartingPoint,XRange)
    for t in TimeRange: 
        StartingPoint=array([RadiusOfCircle*cos(t)+StartingPoint[0],RadiusOfCircle*sin(t)+StartingPoint[1]])
        Y1=CircleGenerator(TotalTime,t,SpeedOfSound,StartingPoint,XRange)
        Y0=COMPILE(Y0,Y1)
    Plot(XRange,Y0)


XRange=linspace(-150,150,5000)
SpeedOfSound=5
RadiusOfCircle=10
TotalTime=4*pi
Frequency=10
TimeRange=linspace(1/Frequency,TotalTime,floor(Frequency*TotalTime))
StartingPoint=array([0,0])
CircularCircle(TotalTime,TimeRange,StartingPoint,XRange,RadiusOfCircle,SpeedOfSound)
