# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:55:03 2022

@author: ashru
"""
import math
from scipy.optimize import fsolve
from PIL import Image#, ImageDraw
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
        

        

SPEEDOFSOUND = 343.2

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
timePeriod, timeStep = 1,1
#define the frequency of the sound source
f = 50
#calculate the number of timeSteps the script will go through
stepNumber = math.floor(timePeriod/timeStep)
print(stepNumber)

#define the height and width of the continuous model picture in pixels (wavefront will be double the size)
areaWidth, areaHeight = 400, 400

#define the distance between each pixel in the image
dist = 2
#define the x and y equation m & b (in the form x=xEM*t+xEB etc)
xEM, xEB, yEM, yEB = 0, -50, 0,-50


""" End of inputs """

#create an empty 2d matrix with given dimensions 

areaWidth, areaHeight = 400, 400
area = [0] *(stepNumber)
#areaBW = [0] *(stepNumber+1)
for i in range(stepNumber):
    area[i] = [0] * areaHeight
    #areaBW[i] = [0] * areaHeight
    for j in range(areaHeight):
        area[i][j] = [0] * areaWidth
        #areaBW[i][j] = [0] * areaWidth
        
areaBW = np.zeros((areaHeight,areaWidth))





totalWidthDistHalf = dist*areaWidth/2
totalHeightDistHalf = dist*areaHeight/2

w= 2*math.pi*f



tEList=[]

plt.rcParams["figure.figsize"] = [areaWidth/100, areaHeight/100]
plt.rcParams["figure.autolayout"] = True

plt.title("Wavefront Diagram of a Single Point Sound Source with Equations: \n x="+str(xEM)+"t+"+str(xEB)+", y="+str(yEM)+"t+"+str(yEB)+"\n at Time: t="+str(round(timeStep*(stepNumber),3)))
plt.xlabel("x (m)") 
plt.ylabel("y (m)") 
plt.axis([-totalWidthDistHalf, totalWidthDistHalf, -totalHeightDistHalf, totalHeightDistHalf])
plt.axis('square')
plt.gcf().set_size_inches(areaWidth/50, areaWidth/50)



numCircles = math.floor((stepNumber)*f*timeStep)
circlesList = []
for i in range(numCircles):
    circTime = i/f
    circlesList.append([circTime,circTime*xEM+xEB,circTime*yEM+yEB])
    c = plt.Circle((circTime*xEM+xEB,circTime*yEM+yEB), radius =(SPEEDOFSOUND*(timeStep*stepNumber-circTime)), fill = False)
    plt.gca().add_artist(c)
print(circlesList)
imgData = str(timePeriod) + ',' + str(timeStep) + ',' + str(f) + ',' + str(areaHeight) + ',' + str(areaWidth) + ',' + str(dist) + ',' +  str(xEM) + ',' + str(xEB) + ',' + str(yEM) + ',' + str(yEB)
dataFolder = Path("C:/Users/ashru/Desktop/"+imgData)
p = dataFolder.mkdir(parents=True, exist_ok=True)
plt.savefig("C:/Users/ashru/Desktop/"+imgData+ '/'+imgData +",Wavefront.png",dpi=100)
plt.show()

yEM, yEB= yEM * -1, yEB * -1
speedEst = yEM+xEM


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
                return (x+y-tM, x-((((xEM*y+xEB)-xM)**2+((yEM*y+yEB)-yM)**2)**.5)/340,)
                #return (x+y-tM, x-((((xEM*y+xEB)-xM)**2+((yEM*y+yEB)-yM)**2)**.5)/340)
            """
            if(speedEst>=SPEEDOFSOUND):
                tETotal = 0
                tR, tE=  fsolve(equations, (0, 0))
                if (tE>=0 and tE<= tM):
                    if(tE in tEList==False):
                        tEList.append(tE)
                        tETotal+=tE
                tR, tE=  fsolve(equations, (stepNumber*timeStep, stepNumber*timeStep))
                if (tE>=0 and tE<= tM):
                    if(tE in tEList==False):
                        tEList.append(tE)
                        tETotal+=tE
                area[i][j][k] = (math.sin(w*tETotal))
                tEList = []
            else:
                tR, tE=  fsolve(equations, ((tM/2), (tM/2)))
                if (tE>=0 and tE<= tM):
                    area[i][j][k] = (math.sin(w*tE))
            """
            tR, tE=  fsolve(equations, ((tM/2), (tM/2)))
            if (tE>=0 and tE<= tM):
                area[i][j][k] = (math.sin(w*tE))
print('equations done')




#yN = input("Would you like to make any of the time slots into an image (enter y for yes).")
#if(yN=='y'):im
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
    #name1 = "C:/Users/ashru/Desktop/"+imgData+ '/Circle'+ imgData + ',' + str(k) +".png"
    newImg.save(name)
f = open("C:/Users/ashru/Desktop/"+imgData+ '/'+ imgData + ',' + str(k) +".txt",'w')
write1 = "x = "+str(xEM)+"t + "+str(xEB)
write2 = "y = "+str(yEM)+"t + "+str(yEB)
write3 = "time step "+str(timeStep)+", time measured "+str(timePeriod)
write4 = "frequency "+str(f)
f.write(write1)
f.write(write2)
f.write(write3)
f.write(write4)
print('done')
