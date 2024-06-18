import time, random
import pygame
from math import random

windowWidth = 1280
windowHeight = 720
columnCoords = []
rowCoords = []

class tile:
    def __init__(self, column, row, type, revealed=False):
        self.column = column
        self.row = row
        self.type = type
        self.revealed = revealed
    def __str__(self):
        return f"{self.type} ({self.column},{self.row})"

class coordinate:
    def __init__(self, minX=0, maxX=0, columnNum=0, minY=0, maxY=0, rowNum=0):
        self.minX = minX
        self.maxX = maxX
        self.columnNum = columnNum
        self.minY = minY
        self.maxY = maxY
        self.rowNum = rowNum
    def __str__(self):
        return f"({self.columnNum}, {self.rowNum})"

'''    
class column:
    def __init__(self, minX, maxX, columnNumber):
        self.minX = minX
        self.maxX = maxX
        self.columnNumber = columnNumber
    def __str__(self):
        return f"Column {self.columnNumber} ({self.minX}, {self.maxX})"
    
class row:
    def __init__(self, minY, maxY, rowNumber):
        self.minY = minY
        self.maxY = maxY
        self.rowNumber = rowNumber
    def __str__(self):
        return f"Row {self.rowNumber} ({self.minY}, {self.maxY})"
'''
class grid:
    def __init__(self, width, height, tiles, size=0, startX = 0, padding=10):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.size  = size
        self.padding = padding
        self.startX = startX
        self.coordList = []
    def drawNewGrid (self, padding=10):
        global columnCoords, rowCoords
        '''size = (windowHeight - padding * (self.height + 1))
        size = size - (size % self.height)
        size = size / self.height'''
        if padding != self.padding:
            self.padding = padding
        self.size = windowHeight
        self.size = self.size / self.height
        self.size = (self.size - self.padding) - (self.padding / (self.height + 1))
        self.startX = (self.size * self.width) + (self.padding * self.width - 1)
        self.startX =  ((windowWidth - self.startX) / 2) - ((windowWidth - self.startX) % 2)
        currentY = self.padding
        currentX = self.startX
        for h in range(self.height):
            for w in range(self.width):
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(currentX, currentY, self.size, self.size))
                columnCoords.append((currentX, (currentX + self.size + self.padding))) 
                currentX = currentX + self.size + self.padding
                tempCoords = coordinate()
            rowCoords.append((currentY, (currentY + self.size + self.padding)))       
            currentX = self.startX
            currentY = currentY + self.size + self.padding
        for add in range(columns):
            for i in range(rows):
                tempCoords = coordinate()
                tempCoords.minX = columnCoords[add][0]
                tempCoords.maxX = columnCoords[add][1]
                tempCoords.columnNum = add + 1
                tempCoords.minY = rowCoords[i][0]
                tempCoords.maxY = rowCoords[i][1]
                tempCoords.rowNum = i + 1
                self.coordList.append(tempCoords)
    def printAllCoords(self):
        for coord in self.coordList:
            print(f"({coord.columnNum},{coord.rowNum}) Min X: {coord.minX} Max X: {coord.maxX} Min Y: {coord.minY} Max Y: {coord.maxY}")


    def refreshGrid (self):
        i = 0
        currentX = self.startX
        currentY = self.padding
        for h in range(self.height):
            for w in range(self.width):
                match self.tiles[i].revealed:
                    case False:
                        tempColor = (0, 255, 0)
                    case True:
                        if self.tiles[i].type == "Mine":
                            tempColor = (255, 0, 0)
                        elif self.tiles[i].type == "Blank":
                            tempColor = (225, 225, 225)
                i += 1
                
                pygame.draw.rect(screen, tempColor, pygame.Rect(currentX, currentY, self.size, self.size))
                currentX = currentX + self.size + self.padding
            currentX = self.startX
            currentY = currentY + self.size + self.padding
    def randomizeGrid(self):
        mousePos = pygame.mouse.get_pos
        tempCoord = coordinate()
        for coord in self.coordlist:
            if isInRange(mousePos):
                tempCoord = coord
        tempCoordList = self.coordList
        self.tiles[0].column = tempCoord.columnNum
        self.tiles[0].row = tempCoord.rowNum
        for tile in self.tiles:
            if tile.column != 0 and tile.row != 0:
                pass
            else:
                tempIndex = random.randint(len(tempCoordList)) 
                tile.column = tempCoordList[tempIndex].column
                tile.row = tempCoordList[tempIndex].row
                tempCoordList.remove(tempCoordList[tempIndex])

firstClick = False

def isInRange(pos, coord):
    if pos(0) >= coord.minX and pos(0) <= coord.maxX and pos(1) >= coord.minY and pos(1) <= coord.maxY: #AND THIS ONE TOO! THIS SHOULD HELP OPTIMIZE A BIT
        return True
    else:
        return False

def changeTile(type):
    color = screen.get_at()
    if firstClick and color == (0, 255, 0, 255): #THIS IS THE LINE I WAS WORKING ON PLEASE DON'T FORGET IT I REALLY NEED TO REMEMBER THIS
        gameGrid.randomizeGrid()
    else:
        for tile in gameGrid.tiles:
            if isInRange((tile.column, tile.row), ):
                pass

'''def getClickedTile():
    #Globalize the Necessary Variables
    global columnCoords, rowCoords, gameGrid
    #Gets the Mouse Position
    posToCheck = pygame.mouse.get_pos()
    #For every x value in the current Column
    for x in columnCoords:
        #Checks what column the mouse was in
        if posToCheck(0) >= x(0) and posToCheck (0) <= x(1):
            mouseColumn = x
    #For every y value in the current row
    for y in rowCoords:
        #Checks what row the mouse was in
        if posToCheck(1) >= y(0) and posToCheck(1) <= y(1):
            mouseRow = y
    #For every tile within the current grid
    for tile in gameGrid.tiles:
        #Check if the current tile matches the current clicked area
        if (tile.x >= mouseColumn(0) and tile.x <= mouseColumn(1)) and (tile.y >= mouseRow(0) and tile.y <= mouseRow(1)):
            return tile'''
                    
mines = 5
rows = 8
columns = 8
totalTiles = rows * columns
tileList = []

for i in range(totalTiles - mines):
    tempTile = tile(0, 0, "Blank")
    tileList.append(tempTile)
for t in range(mines):
        tempTile = tile(0, 0, "Mine")
        tileList.append(tempTile)

for i in range(totalTiles):
     print(tileList[i])
gameGrid = grid(columns, rows, tileList)

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
running = True
screen.fill("blue")
gameGrid.drawNewGrid()
framesPressed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    
    #Detect Clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
        framesPressed += 1
        if event.button == 1:
            if framesPressed == 1:
                changeTile("Remove")
                gameGrid.refreshGrid()
                print(gameGrid.printAllCoords())
        elif event.button == 3:
            if framesPressed == 1:
                changeTile("Flag")
                gameGrid.refreshGrid()
                print("Flag")
    if event.type == pygame.MOUSEBUTTONUP:
        framesPressed = 0
    
    pygame.display.update()
    clock.tick(30)
pygame.quit()