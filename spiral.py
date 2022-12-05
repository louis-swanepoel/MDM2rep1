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
from matplotlib import pyplot as plt

#Change data folder to wherever on your 
data_folder = "C:/Users/ashru/Desktop"

#define a function for printing the matrix
def printArea():
    for i in range(len(area)):
        for j in range (len(area[0])):
            print(area[i][j], end = " ")
            print("\n")
        print("\n")

#define variables for x measured, y measured 
xM = int()
yM = int()

#define a variable for time emitted, time measured, and retarded time
tE = float()
tMList = []
tR = float() 
tM= 0
pressure = []

#define speed of sound        
SPEEDOFSOUND = 343.2

""" Beginning of inputs """

#define timePeriod and timeStep
timePeriod, timeStep = 5,5
#define the frequency of the sound source
f = 50
#calculate the number of timeSteps the script will go through
stepNumber = math.floor(timePeriod/timeStep)

#define the height and width of the continuous model picture in pixels (wavefront will be double the size)
areaWidth, areaHeight = 400, 400

#define the distance between each pixel in the image
dist = 2

#define the x and y equation's omega & amplitude (in the form x=xAmplitude*sin(xOmegat+xOffset) etc)
xOmega,xAmplitude,yOmega,yAmplitude = 2*math.pi, 50, 2*math.pi, 50
#define the x and y offset. use math.pi/2 for cosine 
xOffset, yOffset =math.pi/2,0

""" End of inputs """

totalWidthDistHalf = dist*areaWidth/2
totalHeightDistHalf = dist*areaHeight/2

w= 2*math.pi*f


#create an empty 2d matrix with given dimensions 


area = [0] *(stepNumber)
#areaBW = [0] *(stepNumber+1)
for i in range(stepNumber):
    area[i] = [0] * areaHeight
    #areaBW[i] = [0] * areaHeight
    for j in range(areaHeight):
        area[i][j] = [0] * areaWidth
        #areaBW[i][j] = [0] * areaWidth
        
areaBW = np.zeros((areaHeight,areaWidth))





plt.rcParams["figure.figsize"] = [areaWidth/100, areaHeight/100]
plt.rcParams["figure.autolayout"] = True

plt.title("Wavefront Diagram of a Single Point Sound Source with Equations: \n x="+str(round(xAmplitude,3))+"/sqrt(t)*sin("+str(round(xOmega,3))+'t+'+str(round(xOffset,3))+"), y="+str(round(yAmplitude,3))+"/sqrt(t)*sin("+str(round(yOmega,3))+'t+'+str(round(yOffset,3))+")\n at Time: t="+str(round(timeStep*(stepNumber),3)))
plt.xlabel("x (m)") 
plt.ylabel("y (m)") 
plt.axis([-totalWidthDistHalf, totalWidthDistHalf, -totalHeightDistHalf, totalHeightDistHalf])
plt.axis('square')
plt.gcf().set_size_inches(areaWidth/50, areaWidth/50)



numCircles = math.floor((stepNumber)*f*timeStep)
circlesList = []
for i in range(numCircles):
    circTime = i/f
    try:
        circlesList.append([circTime,xAmplitude/(circTime**.5)*math.sin(xOmega*circTime+xOffset),yAmplitude/(circTime**.5)*math.sin(yOmega*circTime+yOffset)])
        c = plt.Circle((xAmplitude/(circTime**.5)*math.sin(xOmega*circTime+xOffset),yAmplitude/(circTime**.5)*math.sin(yOmega*circTime+yOffset)), radius =(SPEEDOFSOUND*(timeStep*stepNumber-circTime)), fill = False)
    except:
        circlesList.append([circTime,xAmplitude*math.sin(xOmega*circTime+xOffset),yAmplitude*math.sin(yOmega*circTime+yOffset)])
        c = plt.Circle((xAmplitude*math.sin(xOmega*circTime+xOffset),yAmplitude*math.sin(yOmega*circTime+yOffset)), radius =(SPEEDOFSOUND*(timeStep*stepNumber-circTime)), fill = False)
    plt.gca().add_artist(c)
print(circlesList)
imgData = str(timePeriod) + ',' + str(timeStep) + ',' + str(f) + ',' + str(areaHeight) + ',' + str(areaWidth) + ',' + str(dist) + ',' +  str(xAmplitude) + ',' + str(xOmega)+','+str(xOffset) + ','+str(yAmplitude) +','+ str(yOmega) + ',' + str(yOffset)+'circ'
dataFolder = Path("C:/Users/ashru/Desktop/"+imgData)
p = dataFolder.mkdir(parents=True, exist_ok=True)
plt.savefig("C:/Users/ashru/Desktop/"+imgData+ '/'+imgData +",Wavefront.png",dpi=100)
plt.show()

yAmplitude*=-1

for j in range(len(area[0])):
    yM = j * dist - totalHeightDistHalf
    for k in range(len(area[0][0])):  
        xM = k * dist - totalWidthDistHalf
        for i in range(stepNumber):
            #set xM and yM based on current place measured * dist
            tM = (i+1) * timeStep
            tMList.append(tM)
            def equations(p):
                x, y = p
                return (x+y-tM, x-((((xAmplitude/(y**.5)*math.sin(xOmega*y+xOffset))-xM)**2+(yAmplitude/(y**.5)*math.sin((yOmega*y+yOffset))-yM)**2)**.5)/SPEEDOFSOUND)
                #return (x+y-tM, x-((((xOmega*y+xAmplitude)-xM)**2+((yOmega*y+yAmplitude)-yM)**2)**.5)/SPEEDOFSOUND)
            tR, tE=  fsolve(equations, ((i*timeStep/2), (i*timeStep/2)))
            if(tE>=0):
                #x = setX(tE)
                #y = setY(tE)
                #create a variable for the farthest 
                """
                #set r based on formula for x=t, y=t, measured fro (0,0)
                r = (((xAmplitude*math.sin(xOmega*y+xOffset))-xM)**2+(yAmplitude*math.sin((yOmega*y+yOffset))-yM)**2)**.5
                if(r==0):
                    area[i][j][k] = (math.sin(w*tE))
                else:
                    area[i][j][k] = (math.sin(w*tE)/(r**2))
                """
                area[i][j][k] = (math.sin(w*tE))

print('equations done')

images= []
dataFolder = Path("C:/Users/ashru/Desktop/"+imgData)
p = dataFolder.mkdir(parents=True, exist_ok=True)
#yN = input("Would you like to make any of the time slots into an image (enter y for yes).")
#if(yN=='y'):
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
    newImg = Image.fromarray(np.uint8(areaBW))

    name = "C:/Users/ashru/Desktop/"+imgData+ '/'+ imgData + ',' + str(k) +".png"
    newImg.save(name)
f = open("C:/Users/ashru/Desktop/"+imgData+ '/'+ imgData + ',' + str(k) +".txt",'w')
write1 = "x = "+str(xAmplitude)+"sin("+str(xOmega)+'t+'+str(xOffset)+"), "
write2 = "y="+str(yAmplitude)+"sin("+str(yOmega)+'t+'+str(yOffset)+')'
write3 = "time step "+str(timeStep)+", time measured "+str(timePeriod)
write4 = "frequency "+str(f)
f.write(write1)
f.write(write2)
f.write(write3)
f.write(write4)
print('done')
print('done')