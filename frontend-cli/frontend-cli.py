
import cv2
from numpy import *
import sys
import networkx as nx
funnyArgs = sys.argv
if(len(funnyArgs)<1):
    raise Exception("smartahh you need more arguments")
if(len(funnyArgs)>1):
    raise Exception("smartahh you need less arguments")
print(funnyArgs)
def cropArrayYStuff(yaxisA:int,yaxisB:int,leArray:array):
    funnyArrayThingy = leArray
    for x in range(yaxisA):
        delete(leArray,x,0)
    for y in range(yaxisB):
        delete(leArray,y+(yaxisA+(yaxisB-yaxisA)),0)
    return funnyArrayThingy
class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other):
        Vector2(self.x + other.x, self.y + other.y)
        
    def __minus__(self, other):
        Vector2(self.x - other.x, self.y - other.y)

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
def isMoreThanOnePossibleWays(list:list):
    maNeighborsPos = []
    incrementDaGoofy= 0
    for x in range(len(list)):
        incrementDaGoofy+=1
        if(x == 1):
            maNeighborsPos.append(incrementDaGoofy)
    return maNeighborsPos
def isPathBetweenTwoPointsExistentOnGod(pos1:Vector2,pos2:Vector2,matrix:list):
    #time to use some weird library that does weird node graph stuff i dont understand 
    things = nx.DiGraph(npArrayFromMatrix(cropArrayYStuff(pos1.y if pos2.y<pos1.y else pos2.y,pos2.y if pos2.y<pos1.y else pos1.y,matrix)))
    
def iKnowWhatImDoing(importantFunnyNumberTHingy:int,x:int,y:int):
    if(importantFunnyNumberTHingy>0):
        return x>y
    else:
        return x<y
def funnyMiddleendThingyToDoStuff(leImage:BlackAndWhiteImageMatrix):
    level_of_detail = 50
    lePointImageTHingy = vectorMatrixThingy()
    lePointImageTHingy.create(leImage.size)
    lodTicker = 0
   

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
def npArrayFromMatrix(funnyMatrixThing:BlackAndWhiteImageMatrix)->array:
    return array(funnyMatrixThing.matrix)
def threeNeighborsCheck(list:List)->bool:
    incrementer = 0
    for x in range(len(list)):
        if(x == 1):
            incrementer += 1
            if((incrementer < 8 and incrementer < 7)):
                return True
    return False
def getNeighbors(imageMatrix:BlackAndWhiteImageMatrix,pixelPos:Vector2):
    myNeighbors =[]
    if(not y==newImageMatrix.size.y):
        myNeighbors.append(imageMatrix.matrix[x][y+1])
        myNeighbors.append(imageMatrix.matrix[x+1][y+1])
    if(not y==0):
        yNeighbors.append(imageMatrix.matrix[x][y-1])
        yNeighbors.append(imageMatrix.matrix[x-1][y-1])
    if(x!=0):
        myNeighbors.append(imageMatrix.matrix[x-1][y])
        myNeighbors.append(imageMatrix.matrix[x-1][y+1])
    if(x!=newImageMatrix.size.x):
        myNeighbors.append(imageMatrix.matrix[x+1][y])
        myNeighbors.append(imageMatrix.matrix[x+1][y-1])

def generateEdgeMap(imageMatrix:BlackAndWhiteImageMatrix)->BlackAndWhiteImageMatrix:
    newImageMatrix = BlackAndWhiteImageMatrix()
    newImageMatrix.create(imageMatrix.size.x, imageMatrix.size.y)
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

