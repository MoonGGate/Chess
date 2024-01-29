import board
class whitePawn:
    def __init__(self, pos, gameInstance):
        self.pos = pos
        self.gameInstance = gameInstance
    
    # To verify positions returned by movement funcs
    def posCheck(self, pos):
        tempPos = list(pos)
        if int(tempPos[1]) + 1 <= 8 and int(tempPos[1]) - 1 >= 1 and tempPos[0] >= 'a' and tempPos[0]<= 'h':
            if pos in self.gameInstance.getEmptySpaceLocations():
                return True
            else:
                raise ValueError('Position is not empty')
        else:
            raise ValueError('Invalid position')
        
    # Example movement func for pawn class #
    def move(self, pos):
        #returns new pos but doesn't assign it yet bc unchecked
        if self.posCheck(pos):
            self.pos = pos
        return print('Moved successfully')
    
    # Example beat func for pawn class #
    def beat(self, pos):
        #same as move
        pass

class blackPawn(whitePawn):
    def move(self, pos):
        #override#
        pass
    
    def beat(self, pos):
        #override#
        pass