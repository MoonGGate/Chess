import board
from string import ascii_lowercase

 ### Will contain, movement funcs (beat/move/switch) ###

class Figure:
    def __init__(self, name, color, pos, gameInstance):
        self.name = name
        self.color = color
        self.pos = pos
        self.gameInstance = gameInstance
        self.figLocations = self.gameInstance.figureLocations
        self.setPosition(pos)

    # Checks if passed pos is empty (Can be inherited)
    def posCheck(self, pos):
        if pos in self.gameInstance.getEmptySpaceLocations():
            return True
        else:
            return False
    
    # Used to convert pos to str
    def convertPosToString(self, pos):
        return pos[0] + str(pos[1])
    
    # Used to convert pos back to lst
    # def convertPosToList(self, pos):
    #     return [pos[0], int(pos[1])]
    
    # Example movement func for pawn class (Can be inherited)
    def setPosition(self, pos):
        # To update possible moves and beatings for figs that didnt move
        if pos == self.pos:
            self.possibleMoves = self.getPossibleMoves()
            self.possibleBeatings = self.getPossibleBeatings()
            self.gameInstance.figureLocations[self.convertPosToString(pos)] = self
            return print('Obj created/updated')

        elif pos in self.possibleMoves:
            del self.gameInstance.figureLocations[self.convertPosToString(self.pos)]
            self.gameInstance.figureLocations[self.convertPosToString(pos)] = self
            self.gameInstance.emptySpaceLocation.remove(pos)
            self.gameInstance.emptySpaceLocation.append(self.pos)
            self.pos = pos
            self.possibleMoves = self.getPossibleMoves()
            self.possibleBeatings = self.getPossibleBeatings()

        else:
            return print('Invalid Move')
        return print('Moved successfully')
    
    # Example beat func for pawn class (Can be inherited)
    def beatFigure(self, pos):
        if pos in self.possibleBeatings:
            self.gameInstance.emptySpaceLocation.append(self.pos)
            # Remove the figure to be beated (Unimplemented) 
            self.pos = pos
        return print('Beated the figure successfully')

class whitePawn(Figure):
    def __init__(self, name, color, pos, gameInstance):
        super().__init__(name, color, pos, gameInstance)
    
    # Will be different for every figure
    def getPossibleMoves(self):
        pos = self.pos
        possiblePositions = []

        # Checks for possible moves
        if pos[1] + 1 <= 8:
            possiblePos = pos[:]
            possiblePos[1] += 1
            if self.posCheck(possiblePos):
                possiblePositions.append(possiblePos)
        
        # First move case
        if pos[1] == 2:
            if pos[1] + 2 <= 8:
                possiblePos = pos[:]
                possiblePos[1] += 2
                if self.posCheck(possiblePos):
                    possiblePositions.append(possiblePos)

        return possiblePositions
    
    # Will be different for every figure
    def getPossibleBeatings(self):
        pos = self.pos
        possiblePositions = []

        # Checks for possible beatings
        if chr(ord(pos[0]) + 1) <= 'h' and pos[1] + 1 <= 8:
            possiblePos = pos[:]
            possiblePos[0] = chr(ord(pos[0]) + 1)
            possiblePos[1] += 1
            if not self.posCheck(possiblePos) and self.figLocations[self.convertPosToString(possiblePos)].color == 'Black':  # Need to also check the color of the taken spot
                possiblePositions.append(possiblePos)

        if chr(ord(pos[0]) - 1) >= 'a' and pos[1] + 1 <= 8:
            possiblePos = pos[:]
            possiblePos[0] = chr(ord(pos[0]) - 1)
            possiblePos[1] += 1
            if not self.posCheck(possiblePos) and self.figLocations[self.convertPosToString(possiblePos)].color == 'Black':  # Need to also check the color of the taken spot
                possiblePositions.append(possiblePos)

        return possiblePositions
        

class blackPawn(Figure):
    def __init__(self, name, color, pos, gameInstance):
        super().__init__(name, color, pos, gameInstance)
    
    # Will be different for every figure
    def getPossibleMoves(self):
        pos = self.pos
        possiblePositions = []

        # Checks for possible moves
        if pos[1] - 1 >= 1:
            possiblePos = pos[:]
            possiblePos[1] -= 1
            if self.posCheck(possiblePos):
                possiblePositions.append(possiblePos)

        # First move case
        if pos[1] == 7:
            if pos[1] - 2 >= 1:
                possiblePos = pos[:]
                possiblePos[1] -= 2
                if self.posCheck(possiblePos):
                    possiblePositions.append(possiblePos)

        return possiblePositions
    
    # Will be different for every figure
    def getPossibleBeatings(self):
        pos = self.pos
        possiblePositions = []

        # Checks for possible beatings
        if chr(ord(pos[0]) + 1) <= 'h' and pos[1] - 1 >= 1:
            possiblePos = pos[:]
            possiblePos[0] = chr(ord(pos[0]) + 1)
            possiblePos[1] -= 1
            if not self.posCheck(possiblePos) and self.figLocations[self.convertPosToString(possiblePos)].color == 'White': # Need to also check the color of the taken spot
                possiblePositions.append(possiblePos)

        if chr(ord(pos[0]) - 1) >= 'a' and pos[1] - 1 >= 1:
            possiblePos = pos[:]
            possiblePos[0] = chr(ord(pos[0]) - 1)
            possiblePos[1] -= 1
            if not self.posCheck(possiblePos) and self.figLocations[self.convertPosToString(possiblePos)].color == 'White': # Need to also check the color of the taken spot
                possiblePositions.append(possiblePos)

        return possiblePositions