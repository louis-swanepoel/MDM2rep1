# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:55:03 2022

@author: ashru
"""

import math

#define a function for getting info for the time information
def getTime():
    try:
        #ask for time peroid and step
        timePeriod = float(input("what is the time period you would like to measure over (s) \n"))
        timeStep = float(input("what is the time step you would like to use (s) \n"))
    except:
        #if invalid input, send error message and re-call function
        print("Something you entered was not a float. Please try again.\n")
        timePeriod, timeStep = getTime()
    #if invalid input, send error message and re-call function
    if(timePeriod<=0):
        print("You cannot have a time period less than or equal to 0. Please try again. \n")
        timePeriod, timeStep = getTime()
    elif(timePeriod<timeStep):
        print("you cannot have a time period less than your time step. Please try again. \n")
        timePeriod, timeStep = getTime()
    elif(timeStep<=0):
        print("You cannot have a time step less than or equal to 0. Please try again. \n")
        timePeriod, timeStep = getTime()
    return timePeriod, timeStep

def getFrequency():
    try:
       f = float(input("What is the frequency of the sound wave? \n")) 
    except:
        print("You did not enter a float. Please try again. \n")
        f =getFrequency()
    if(f<=0):
        print("Frequency must be over 0. Please try again. \n")
        f = getFrequency()
    return f

     
timePeriod, timeStep = getTime()   
f = getFrequency()


w= 2*math.pi*f
t = 0
x = t
y = t

#define a variable to hold the distance from sound emitted to the sensor
r = int()
#define a variable for time emitted, time measured, and retarded time
tE = int()
tM = []
tR = int()

#define a list for pressure measured at given times
pressure = []

def setX(t):
    x = t
    return x

def setY(t):
    y = t
    return y

stepNumber = math.floor(timePeriod/timeStep)

for i in range(stepNumber + 1):
    tM.append(i * timeStep)
    #set tE based on formula for x=t, y=t and measured from 0,0
    tE = (tM[i]*(2**.5))/(340+(2**.5))
    #set r based on formula for x=t, y=t, measured fro (0,0)
    r = (2**.5)*t
    #x = setX(tE)
    #y = setY(tE)
    if(r==0):
        pressure.append(math.sin(w*tE))
    else:
        pressure.append((1/r)*math.sin(w*tE))
    
    
print("Given a sound wave of frequency ", f, "moving with an equation of x=t, y=t over a time period of", timePeriod, "seconds, measured every", timeStep, "seconds:")
for j in range(len(tM)):
    print("The pressure at time", tM[j], "is", pressure[j])
"""print(timePeriod,timeStep)
print(stepNumber)
print(tM)
print(pressure)"""