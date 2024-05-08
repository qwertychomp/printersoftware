#import all the libraries, which provide premade functions 
#(similiar to functions from math) for common tasks 
#like reading images and manipulating lists
import cv2
from numpy import *
import sys
import minecraft
#command-line arguments so the user can use 
#settings other than the defaults if they want
funnyArgs = sys.argv
if(len(funnyArgs)<1):
    raise Exception("smartahh you need more arguments")
if(len(funnyArgs)>1):
    raise Exception("smartahh you need less arguments")
print(funnyArgs)
#classes (objects that hold functions and value)

#vector2 (a coordinate pair)
class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other):
        Vector2(self.x + other.x, self.y + other.y)
        
    def __minus__(self, other):
        Vector2(self.x - other.x, self.y - other.y)

#a matrix/grid object (like from math!) to store an image 
#made of pixels (a bitmap image!) in a form that can easily be
#manipulated through the built-in list functions
class BlackAndWhiteImageMatrix:
    def __init__(self) -> None:
        self.size = Vector2(0, 0)
        self.matrix = []

    def create(self, size: Vector2):
        for x in range(size.x):
            new_x = []
            for y in range(size.y):
                new_x.append(0)

            self.matrix.append(new_x)

        self.size = size

    def set_pixel(self, pos: Vector2, value: int):
        if value == 0 or value == 1:
            self.matrix[pos.x][pos.y] = value
        else:
            raise Exception("imageMatrix is black and white only")
#an object for storing an image made of lines as opposed to pixels (a vector image)
class vectorMatrixThingy(BlackAndWhiteImageMatrix):
    def __init__(self) -> None:
        super().__init__()
        self.pointConnectionMatrix = []
    def set_pixel(self, pos1: Vector2, value: int, pos2:Vector2):
        super().set_pixel(pos1, 1)
        self.pointConnectionMatrix[pos2.x][pos2.y]=pos1
    def create(self, size: Vector2):
        super().create(size)
        for x in range(size.x):
            new_x = []
            for y in range(size.y):
                new_x.append(0)

            self.pointConnectionMatrix.append(new_x)
#a function to see if, in a bitmap image, you can connect two points
#by following black pixels on the image (i just started working on it)
def isPathBetweenTwoPointsExistentOnGod(pos1:Vector2,pos2:Vector2,matrix:list):
    isResultFound = False
    stopAtYpoint = 0
    if(pos1.y<pos2.y):
        stopAtYpoint=1
    elif(pos1.y>pos2.y):
        stopAtYpoint=-1
    while(not isResultFound):
        pass
#this code executes all the stuff for the middle-end, which im still working on
def funnyMiddleendThingyToDoStuff(leImage:BlackAndWhiteImageMatrix):
    level_of_detail = 50
    lePointImageTHingy = vectorMatrixThingy()
    lePointImageTHingy.create(leImage.size)
    lodTicker = 0
    currentFunnyThingies = []
    for n in len(leImage.matrix.y):
        if (lodTicker==0 or lodTicker==level_of_detail):
            for x in len(leImage.matrix.x):
                if(leImage.matrix[x][n]==1):
                    if(n!=0):
                        if(len(currentFunnyThingies)==0):
                            currentFunnyThingies.append(Vector2(x,n))
                           
                    else:
                        pass
        lodTicker+=1
        if (lodTicker>level_of_detail):
            lodTicker=0
#this takes a string (datatype for strings of characters) and converts
#it into aBlackAndWhiteImageMatrix 
def matrixFromImage(fileLocation:str)->BlackAndWhiteImageMatrix:
    newImage = cv2.imread(fileLocation, cv2.IMREAD_GRAYSCALE)
    newImageMatrix = BlackAndWhiteImageMatrix()
    newImageMatrix.create(Vector2(newImage.shape[0], newImage.shape[1]))
    
    for x in range(newImage.shape[0]):
        for y in range(newImage.shape[1]):
            if(newImage[x][y] < 152):
                newImageMatrix.set_pixel(Vector2(x, y), 1)
            else:
                newImageMatrix.set_pixel(Vector2(x, y), 0)
    newImageMatrix = generateEdgeMap(newImageMatrix)
    return newImageMatrix
#simple code to take 9 pixels and see if the center one  has three
#black pixels neighboring it
def threeNeighborsCheck(list:List)->bool:
    incrementer = 0
    for x in range(len(list)):
        if(x == 1):
            incrementer += 1
            if(incrementer == 3):
                return True
    return False
#take an image matrix and convert it to a new image matrix that 
#only includes the pixels that are neighboring 3 or more white pixels
def generateEdgeMap(imageMatrix:BlackAndWhiteImageMatrix)->BlackAndWhiteImageMatrix:
    newImageMatrix = BlackAndWhiteImageMatrix()
    newImageMatrix.create(imageMatrix.size.x, imageMatrix.size.y)
    myNeighbors = []
    for x in range(newImageMatrix.size.x):
        for y in range(newImageMatrix.size.y):
            if(not y==newImageMatrix.size.y):
                myNeighbors.append(imageMatrix.matrix[x][y+1])
                myNeighbors.append(imageMatrix.matrix[x+1][y+1])
            if(not y==0):
                myNeighbors.append(imageMatrix.matrix[x][y-1])
                myNeighbors.append(imageMatrix.matrix[x-1][y-1])
            if(x!=0):
                myNeighbors.append(imageMatrix.matrix[x-1][y])
                myNeighbors.append(imageMatrix.matrix[x-1][y+1])
            if(x!=newImageMatrix.size.x):
                myNeighbors.append(imageMatrix.matrix[x+1][y])
                myNeighbors.append(imageMatrix.matrix[x+1][y-1])
            if(threeNeighborsCheck(myNeighbors)):
                newImageMatrix.set_pixel(Vector2(x,y),1)
    return newImageMatrix
funnyhaha = matrixFromImage(funnyArgs[0])

