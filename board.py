class Game:
    
    ### Need classes for each fig ###

    ####################################
    ##       Initial Game State       ##
    ####################################
    # tst1
    def __init__(self):
        self.board = [[[], [], [], [], [], [], [], []],     # Only idea is to use it for graphics
                      [[], [], [], [], [], [], [], []],     # Can remove/replace for something else
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []]]
        
        # White are positive values from 1 to 6, Black are negative values from -1 to -6.
        self.figureLocations = {}

        self.emptySpaceLocation =  [['a',6], ['b',6], ['c',6], ['d',6], ['e',6], ['f',6], ['g',6], ['h',6],
                                    ['a',5], ['b',5], ['c',5], ['d',5], ['e',5], ['f',5], ['g',5], ['h',5],
                                    ['a',4], ['b',4], ['c',4], ['d',4], ['e',4], ['f',4], ['g',4], ['h',4],
                                    ['a',3], ['b',3], ['c',3], ['d',3], ['e',3], ['f',3], ['g',3], ['h',3]]
    
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.checkBoard()

    def getEmptySpaceLocations(self):
        return self.emptySpaceLocation
    
    def printBoard(self):
        for i in self.board:
            print(i)

    ## Creates a checkboard with values on the grid, such as a8, b5, c3, etc
    def checkBoard(self):
        for row in range(self.rows):                            # WHY?????? #
            for col in range(self.cols):
                self.board[row][col] = [chr(97 + col), 8 - row]

        return self.board
    
    #######################
    ##       Rules       ##
    #######################