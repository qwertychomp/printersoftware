#import all the libraries, which provide premade functions 
#(similiar to functions from math) for common tasks 
#like reading images and manipulating lists

#python is ez dubs if you just import 5 billion libraries

import cv2
from numpy import *
import sys
import minecraft
import threading
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
#command-line arguments so the user can use 
#settings other than the defaults if they want
funnyArgs = sys.argv
if(len(funnyArgs)<2):
    raise Exception("smartahh you need more arguments")
if(len(funnyArgs)>2):
    raise Exception("smartahh you need less arguments")
try:
    testingSomeStuff = int(funnyArgs[0])
except:
    raise Exception("the level of detail is a number smartahh")
level_of_detail=funnyArgs[0]
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
    def crop_y(self,start_y: int, end_y: int):
        for dumbFUnnyNumber in range(end_y-start_y):
            self.matrix.pop(dumbFUnnyNumber+start_y)
        idkImStupid = (end_y-start_y)+start_y
        for dumbAss in range(idkImStupid):
            self.matrix.pop(dumbAss+(end_y-start_y))
    def returnYRow(self,yRowNum:int):
        returnValue = []
        for iterator in len(self.matrix):
            if(self.matrix[iterator][yRowNum]!=0)
                returnValue.append(Vector2(iterator,yRowNum))
        return returnValue
        
        
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
#take a bitmap image and the position of a pixel in that image, and return its neighboring pixels
def getNeighbors(pixelPos:Vector2,otherSTupidImageThingy:BlackAndWhiteImageMatrix):
        myNeighbors =[]
        if(not otherSTupidImageThingy.y==otherSTupidImageThingy.size.y):
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x][pixelPos.y+1])
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x+1][pixelPos.y+1])
        if(not otherSTupidImageThingy.y==0):
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x][pixelPos.y-1])
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x-1][pixelPos.y-1])
        if(otherSTupidImageThingy.x!=0):
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x-1][pixelPos.y])
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x-1][pixelPos.y+1])
        if(otherSTupidImageThingy.x!=otherSTupidImageThingy.size.x):
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x+1][pixelPos.y])
            myNeighbors.append(otherSTupidImageThingy.matrix[pixelPos.x+1][pixelPos.y-1])
        return myNeighbors
def getNeighborsPos(pixelPos:Vector2,otherSTupidImageThingy:BlackAndWhiteImageMatrix):
        myNeighbors =[]
        if(not otherSTupidImageThingy.y==otherSTupidImageThingy.size.y):
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x,pixelPos.y+1))
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x+1,pixelPos.y+1))
        if(not otherSTupidImageThingy.y==0):
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x,pixelPos.y-1))
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x-1,pixelPos.y-1))
        if(otherSTupidImageThingy.x!=0):
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x-1,pixelPos.y))
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x-1,pixelPos.y))
        if(otherSTupidImageThingy.x!=otherSTupidImageThingy.size.x):
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x+1,pixelPos.y))
            myNeighbors.append(otherSTupidImageThingy.Vector2(pixelPos.x+1,pixelPos.y-1))
        return myNeighbors
#a function to see if, in a bitmap image, you can connect two points
#by following black pixels on the image (i just started working on it)
def isPathBetweenTwoPointsExistentOnGod(pos1:Vector2,pos2:Vector2,matrix:BlackAndWhiteImageMatrix):
    isResultFound = False
    stopAtYpoint = 0
    if(pos1.y<pos2.y):
        stopAtYpoint=1
    elif(pos1.y>pos2.y):
        stopAtYpoint=-1
    matrix.crop_y(pos1.y,pos2.y)
    grid = Grid(matrix=matrix.matrix)
    dumbassStartPosition = grid.Node(pos1.x,pos1.y)
    dumbassEndPosition = grid.Node(pos2.x,pos.x)
    find = AStarFinder(diagonal_movement=DiagonalMovement.always)
    #if length of path is zero, then there is no path between the two points
    path, runs = find.find_path(pos1, pos2, grid)
    if len(path)==0:
        return False
    else:
        return True
def getRidOfThatOtherThingy(theThingy:list,ohBoyIreallyLoveWritingCodeFrFrOnGodThisIsSoStupidWhatAmIEvenDoingIFeelSorryForAnyoneWhoHasToReadThisCodeWtf:Vector2):
    #hey guys whats up its me writing another stupid code comment beCAUSE I SUCK AT FOCUSING OOPS ACCidently turned on caps lock anyways gtg bye 
    #god this is so abhorrent i dont even remember what this does
    #this function is never even used god what was i thinking
    stuffToRemove = []
    thisIsSoFreakingBoringAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA = theThingy
    for hjh in theThingy.size():
        if(theThingy[hjh].y<ohBoyIreallyLoveWritingCodeFrFrOnGodThisIsSoStupidWhatAmIEvenDoingIFeelSorryForAnyoneWhoHasToReadThisCodeWtf.y):
            stuffToRemove.append(hjh)
    for qwertyuioppoiuyrsredftyuijokpkxqweiqiewiqyeiyiewiuewqiyqiweqiueqweqwyueqweqwiyewquyweqweqiyewqeiyueqw in stuffToRemove.size():
        thisIsSoFreakingBoringAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.remove(stuffToRemove[qwertyuioppoiuyrsredftyuijokpkxqweiqiewiqyeiyiewiuewqiyqiweqiueqweqwyueqweqwiyewquyweqweqiyewqeiyueqw])
    return thisIsSoFreakingBoringAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#this code executes all the stuff for the middle-end
def funnyMiddleendThingyToDoStuff(leImage:BlackAndWhiteImageMatrix)->vectorMatrixThingy:
    lodTicker = 0
    thingToReturn= vectorMatrixThingy()
    thingToReturn.create(leImage.size)

def imageMatrixChangerThing(thing:BlackAndWhiteImageMatrix,thingyToExclude:Vector2,yRowToRemove:int):
    for x in len(thing.matrix):
        if(!x )
def returnPixelFrontOfLine(pixelpos:Vector2,stupidImageThigy:BlackAndWhiteImageMatrix,amountOfThingyUnitsInFrontOfTheThingyWIthTheUntisThoThoFRFR:int)->list:
    pixelsInFront = []
    #remove the y row from image matrix because we dont want the algorithm doing anything silly like filling in a square because it takes path on the sides
    newModddedImageMatrix = stupidImageThigy

     #fill following queue with every pixel that exists on the row in front of the target pixel by the lod
    followingCheckQueue = stupidImageThigy.returnYRow(pixelpos.y+level_of_detail)
    for iteratorThing in len(followingCheckQueue):
        if(isPathBetweenTwoPointsExistentOnGod(pixelpos,followingCheckQueue)):
            pixelsInFront.append(followingCheckQueue)
    return pixelsInFront
#this takes a string (datatype for strings of characters) and converts
#it into a BlackAndWhiteImageMatrix 
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
def threeNeighborsCheck(bist:list)->bool:
    incrementer = 0
    for x in range(len(bist)):
        if(x == 1):
            incrementer += 1
            if(incrementer!=0):
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
            myNeighbors = getNeighbors(x,y,imageMatrix)
            if(threeNeighborsCheck(myNeighbors)):
                newImageMatrix.set_pixel(Vector2(x,y),1)
    return newImageMatrix
funnyhaha = matrixFromImage(funnyArgs[0])