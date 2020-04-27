import pygame
import random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Heroine Game')
ScreenWidth = 650
ScreenHeight = 650
MapSize = 25  # how many tiles in either direction
TileWidth = 20  # pixel sizes for grid squares
TileHeight = 20
TileMargin = 4
Screen = pygame.display.set_mode([ScreenHeight, ScreenWidth])
Done = False  # variable keeping track

Colors = {'Black': (0, 0, 0),
          'White': (255, 255, 255),
          'Green': (0, 255, 0),
          'Red': (255, 0, 0),
          'Blue': (0, 0, 255)}


def drawMap(self, screen, camera_x, camera_y):
    for y in range(self.height):
        for x in range(self.width):
            tile_position_x = (x * TileWidth) - camera_x
            tile_position_y = (y * TileHeight) - camera_y
            if onscreen(tile_position_x, tile_position_y):
                self._mapData[y][x].draw(screen, x * TileWidth, y * TileHeight)


def onscreen(x, y):
    return not (x < TileWidth or x > ScreenWidth or
                y < TileHeight or y > ScreenHeight)


class MapTile(object):  # The main class for stationary things that inhabit the grid ... grass, trees, rocks and stuff.
    def __init__(self, Name, column, row):
        self.Name = Name
        self.Column = column
        self.Row = row


class Character(object):  # Characters can move around and do cool stuff
    def __init__(self, Name, HP, column, row):
        self.Name = Name
        self.HP = HP
        self.Column = column
        self.Row = row

    def Move(self, Direction):  # This function is how a character moves around in a certain direction

        if Direction == "UP":
            if self.Row > 0:  # If within boundaries of grid
                if not self.CollisionCheck("UP"):  # And nothing in the way
                    self.Row -= 1  # Go ahead and move

        elif Direction == "LEFT":
            if self.Column > 0:
                if not self.CollisionCheck("LEFT"):
                    self.Column -= 1

        elif Direction == "RIGHT":
            if self.Column < MapSize - 1:
                if not self.CollisionCheck("RIGHT"):
                    self.Column += 1

        elif Direction == "DOWN":
            if self.Row < MapSize - 1:
                if not self.CollisionCheck("DOWN"):
                    self.Row += 1

        Map.update()

    def CollisionCheck(self, Direction):  # Checks if anything is on top of the grass in the direction that the
        # character wants to move. Used in the move function
        if Direction == "UP":
            if len(Map.Grid[self.Column][self.Row - 1]) > 1:
                return True
        elif Direction == "LEFT":
            if len(Map.Grid[self.Column - 1][self.Row]) > 1:
                return True
        elif Direction == "RIGHT":
            if len(Map.Grid[self.Column + 1][self.Row]) > 1:
                return True
        elif Direction == "DOWN":
            if len(Map.Grid[self.Column][self.Row + 1]) > 1:
                return True
        return False

    def Location(self):
        print("Coordinates: " + str(self.Column) + ", " + str(self.Row))


class Map(object):  # The main class; where the action happens
    global MapSize

    Grid = []

    for Row in range(MapSize):  # Creating grid
        Grid.append([])
        for Column in range(MapSize):
            Grid[Row].append([])

    for Row in range(MapSize):  # Filling grid with grass
        for Column in range(MapSize):
            TempTile = MapTile("Grass", Column, Row)
            Grid[Column][Row].append(TempTile)

    for Row in range(MapSize):  # Putting some rocks near the top
        for Column in range(MapSize):
            TempTile = MapTile("Rock", Column, Row)
            if Row == 1:
                Grid[Column][Row].append(TempTile)

    for i in range(10):  # Placing Random trees
        RandomRow = random.randint(0, MapSize - 1)
        RandomColumn = random.randint(0, MapSize - 1)
        TempTile = MapTile("Tree", RandomColumn, RandomRow)
        Grid[RandomColumn][RandomRow].append(TempTile)

    RandomRow = random.randint(0, MapSize - 1)  # Dropping the hero in
    RandomColumn = random.randint(0, MapSize - 1)
    Hero = Character("Hero", 10, RandomColumn, RandomRow)

    def update(self):  # Very important function
        # This function goes through the entire grid
        # And checks to see if any object's internal coordinates
        # Disagree with its current position in the grid
        # If they do, it removes the objects and places it
        # on the grid according to its internal coordinates

        for column in range(MapSize):
            for Row in range(MapSize):
                for i in range(len(Map.Grid[column][Row])):
                    if Map.Grid[column][Row][i].Column != column:
                        Map.Grid[column][Row].remove(Map.Grid[column][Row][i])
                    elif Map.Grid[column][Row][i].Name == "Hero":
                        Map.Grid[column][Row].remove(Map.Grid[column][Row][i])
        Map.Grid[int(Map.Hero.Column)][int(Map.Hero.Row)].append(Map.Hero)


Map = Map()

while not Done:  # Main pygame loop

    for event in pygame.event.get():  # catching events
        if event.type == pygame.QUIT:
            Done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Pos = pygame.mouse.get_pos()
            Column = Pos[0] // (TileWidth + TileMargin)  # Translating the position of the mouse into rows and columns
            Row = Pos[1] // (TileHeight + TileMargin)
            print(str(Row) + ", " + str(Column))

            for i in range(len(Map.Grid[Column][Row])):
                print(str(Map.Grid[Column][Row][i].Name))  # print stuff that inhabits that square

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Map.Hero.Move("LEFT")
            if event.key == pygame.K_RIGHT:
                Map.Hero.Move("RIGHT")
            if event.key == pygame.K_UP:
                Map.Hero.Move("UP")
            if event.key == pygame.K_DOWN:
                Map.Hero.Move("DOWN")

    Screen.fill(BLACK)

    for Row in range(MapSize):  # Drawing grid
        for Column in range(MapSize):
            for i in range(0, len(Map.Grid[Column][Row])):
                Color = Colors['White']
                if len(Map.Grid[Column][Row]) == 2:
                    Color = Colors['Red']
                if Map.Grid[Column][Row][i].Name == "Hero":
                    Color = Colors['Green']

            pygame.draw.rect(Screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                             (TileMargin + TileHeight) * Row + TileMargin,
                                             TileWidth,
                                             TileHeight])

    clock.tick(60)  # Limit to 60 fps or something

    pygame.display.flip()  # Honestly not sure what this does, but it breaks if I remove it
    Map.update()

pygame.quit()
