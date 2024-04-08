from ast import List
import cv2
from numpy import *


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
                
    return newImageMatrix

def threeNeighborsCheck(list:List)->bool:
    incrementer = 0
    for x in range(len(list)):
        if(x == 1):
            incrementer += 1
            if(incrementer == 3):
                return True
    return False
def generateEdgeMap(imageMatrix:BlackAndWhiteImageMatrix)->BlackAndWhiteImageMatrix:
    newImageMatrix = BlackAndWhiteImageMatrix()
    newImageMatrix.create(imageMatrix.size.x, imageMatrix.size.y)
    myNeighbors = []
    for x in range(newImageMatrix.size.x):
        for y in range(newImageMatrix.size.y):
            if(not y==newImageMatrix.size.y):
                myNeighbors.append(imageMatrix.matrix[x][y+1])
                myNeighbors.append(imageMatrix.matrix[x-1][y+1])
                myNeighbors.append(imageMatrix.matrix[x+1][y+1])
            if(not y==0):
                myNeighbors.append(imageMatrix.matrix[x][y-1])
                myNeighbors.append(imageMatrix.matrix[x-1][y-1])
                myNeighbors.append(imageMatrix.matrix[x+1][y-1])
            if(x!=0):
                myNeighbors.append(imageMatrix.matrix[x-1][y])
                myNeighbors.append(imageMatrix.matrix[x-1][y+1])
                myNeighbors.append(im1)
            if(not(y==newImageMatrix.size.y)):
                myNeighbors.append(imageMatrix.matrix[x+1][y+1])
print(matrixFromImage("test.png").matrix)
print(checkForWhiteNeighbors(matrixFromImage("test.png")))