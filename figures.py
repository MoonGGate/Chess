import board
from string import ascii_lowercase

 ### Will contain, movement funcs (beat/move/switch) ###

class whitePawn:
    def __init__(self, pos, gameInstance):
        self.pos = pos
        self.color = 'White'
        self.gameInstance = gameInstance
        self.possibleMoves = self.getPossibleMoves()
        self.possibleBeatings = self.getPossibleBeatings()
    
    # Checks if passed pos is empty (Can be inherited)
    def posCheck(self, pos):
        if pos in self.gameInstance.getEmptySpaceLocations():
            return True
        else:
            return False
        
    # Example movement func for pawn class (Can be inherited)
    def setPosition(self, pos):
        if pos in self.possibleMoves:
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

        # Checks for possibel beatings
        if chr(ord(pos[0]) + 1) < 'h' and pos[1] + 1 < 9:
            possiblePos = pos[:]
            possiblePos[0] = chr(ord(pos[0]) + 1)
            possiblePos[1] += 1
            if not self.posCheck(possiblePos):          # Need to also check the color of the taken spot
                possiblePositions.append(possiblePos)

        if chr(ord(pos[0]) - 1) > 'a' and pos[1] + 1 < 9:
            possiblePos = pos[:]
            possiblePos[0] = chr(ord(pos[0]) - 1)
            possiblePos[1] += 1
            if not self.posCheck(possiblePos):          # Need to also check the color of the taken spot
                possiblePositions.append(possiblePos)

        return possiblePositions
        

class blackPawn(whitePawn):
    def move(self, pos):
        #override#
        pass
    
    def beat(self, pos):
        #override#
        pass