#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:13:55 2022

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

def StraightLine(TotalTime,TimeRange,StartingPoint,XRange,InitialSpeedOfParticle,AccelerationOfParticle,SpeedOfSound):
    Y0=CircleGenerator(TotalTime,0,SpeedOfSound,StartingPoint,XRange)
    for t in TimeRange:
        StartingPoint=InitialSpeedOfParticle*t+0.5*AccelerationOfParticle*t*2
        Y1=CircleGenerator(TotalTime,t,SpeedOfSound,StartingPoint,XRange)
        Y0=COMPILE(Y0,Y1)
    
    Plot(XRange,Y0)
    
TotalTime=5
Frequency=20
TimeRange=linspace(TotalTime/(Frequency*TotalTime),TotalTime,Frequency*TotalTime)
StartingPoint=array([0,0])
XRange=linspace(-3,8,5000)
InitialSpeedOfParticle=array([1,0])
AccelerationOfParticle=array([0.5,0])
SpeedOfSound=0.5
StraightLine(TotalTime,TimeRange,StartingPoint,XRange,InitialSpeedOfParticle,AccelerationOfParticle,SpeedOfSound)
