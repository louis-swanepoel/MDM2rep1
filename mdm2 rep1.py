# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:55:03 2022

@author: ashru
"""

#define a function for printing the matrix
def printArea():
    for y in range(areaHeight):
        for x in range (areaWidth):
            print(area[y][x], end = " ")
        print("\n")

    
def getAreaLayout():
    #ask for the dimensions of the area
    areaWidth = int(input('Please input the width of the area \n'))
    areaHeight = int(input('Please input the height of the area \n'))
    print("\n")
    return areaWidth, areaHeight


#create an empty 2d matrix with given dimensions
areaWidth, areaHeight = getAreaLayout()
area = [0] * areaHeight
for y in range(areaHeight):
    area[y] = [0] * areaWidth


printArea()
