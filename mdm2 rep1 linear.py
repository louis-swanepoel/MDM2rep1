# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:55:03 2022

@author: ashru
"""
import math
from scipy.optimize import fsolve
from PIL import Image
import numpy as np
from pathlib import Path



data_folder = Path("C:/Users/ashru/Desktop")

#define a function for printing the matrix
def printArea():
    for i in range(len(area)):
        for j in range (len(area[0])):
            print(area[i][j], end = " ")
            print("\n")
        print("\n")
    
def getAreaLayout():
    try:
        #ask for the dimensions of the area
        areaWidth = int(input('Please input the width of the area \n'))
        areaHeight = int(input('Please input the height of the area \n'))
        print("\n")
    except:
        print("Something you entered was not an integer. Please try again. \n")
        areaWidth, areaHeight = getAreaLayout()
    if(areaWidth < 1):
        print("Area width must be greater than zero. Please try again. \n")
        areaWidth, areaHeight = getAreaLayout()
    if(areaHeight < 1):
        print("Area height must be greater than zero. Please try again. \n")
        areaWidth, areaHeight = getAreaLayout()
    return areaWidth, areaHeight

def getAreaDist():
    try:
        dist = float(input("Please input the distance between each measuring point in the area (m) \n"))
    except:
        print("The distance must be a float. Please try again. \n")
        dist = getAreaDist()
    if(dist<=0):
        print("The distance must be greater than zero. Please try again. \n")
        dist = getAreaDist()
    return dist


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

def getXY():
    try:
        xEM = float(input("What would you like the slope of x to equal (in terms of t)? \n"))
        xEB = float(input("What would you like the starting value of x to equal? \n"))
        yEM = float(input("What would you like the slope of y to equal (in terms of t)? \n"))
        yEB = float(input("What would you like the starting value of y to equal? \n"))
    except:
        print("You must enter a float. Please try again. \n")
        xEM, xEB,yEM,yEB = getXY()
    return xEM, xEB, yEM, yEB


#define variables for x measured, y measured 
xM = int()
yM = int()

#define a variable for time emitted, time measured, and retarded time
tE = float()
tEList = []
tMList = []
tR = float() 
tM= 0
pressure = []


timePeriod, timeStep = getTime()   
f = getFrequency()
stepNumber = math.floor(timePeriod/timeStep)

#create an empty 2d matrix with given dimensions 

areaWidth, areaHeight = getAreaLayout()
area = [0] *(stepNumber+1)
#areaBW = [0] *(stepNumber+1)
for i in range(stepNumber+1):
    area[i] = [0] * areaHeight
    #areaBW[i] = [0] * areaHeight
    for j in range(areaHeight):
        area[i][j] = [0] * areaWidth
        #areaBW[i][j] = [0] * areaWidth
        
areaBW = np.zeros((areaHeight,areaWidth))



dist = getAreaDist()
xEM,xEB,yEM,yEB = getXY()


w= 2*math.pi*f


for j in range(len(area[0])):
    yM = j * dist
    for k in range(len(area[0][0])):  
        xM = k * dist
        for i in range(stepNumber + 1):
            #set xM and yM based on current place measured * dist
            tM = i * timeStep
            tMList.append(tM)
            def equations(p):
                x, y = p
                return (x+y-tM, x-((((xEM*y+xEB)-xM)**2+((yEM*y+yEB)-yM)**2)**.5)/340)
                #return (x+y-tM, x-((((xEM*y+xEB)-xM)**2+((yEM*y+yEB)-yM)**2)**.5)/340)
            tR, tE=  fsolve(equations, ((i*timeStep/2), (i*timeStep/2)))
            if(tE>=0):
                tEList.append(tE)
                #set r based on formula for x=t, y=t, measured fro (0,0)
                r = ((tE-xM)**2+(tE-yM)**2)**.5
                #x = setX(tE)
                #y = setY(tE)
                #create a variable for the farthest 
                """
                if(r==0):
                    area[i][j][k] = (math.sin(w*tE))
                else:
                    area[i][j][k] = (math.sin(w*tE)/(r**2))
                """
                area[i][j][k] = (math.sin(w*tE))



printArea()
images= []

yN = input("Would you like to make any of the time slots into an image (enter y for yes).")
if(yN=='y'):
    #step = int(input("Which step would you like to use (start at 1)"))-1
    for k in range(len(area)):
        for i in range(len(area[k])):
            for j in range(len(area[k][i])):
                bV = area[k][i][j]
                if(bV>1):
                    bv=1
                elif(bV<-1):
                    bV = -1
                areaBW[i][j] = int(round(127.5*(bV+1)))
        areaBW = areaBW.astype('i')
        print(areaBW)
        newImg = Image.fromarray(np.uint8(areaBW))
        name = "C:/Users/ashru/Desktop/newImg"+str(k)+".png"
        newImg.save(name)
        #images.append(newImg)
#images2gif.writeGif("C:/Users/ashru/Desktop/images.gif",images,duration=0.3,dither=0)
#images[0].save('images.gif',save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
#print(images)
    
