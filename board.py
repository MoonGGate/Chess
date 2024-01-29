class Game:
    
    ### Need classes for each fig ###
    ### Will contain init pos, movement funcs (beat/move/switch) ###

    ####################################
    ##       Initial Game State       ##
    ####################################

    def __init__(self):
        self.board = [[[], [], [], [], [], [], [], []], 
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], []]]
        
        # White are positive values from 1 to 6, Black are negative values from -1 to -6.
        self.squareList = {
            0: "Empty", 

            1: "White Pawn", 
            2: "White Knight",
            3: "White Bishop", 
            4: "White Rook", 
            5: "White Queen", 
            6: "White King",

            -1: "Black Pawn", 
            -2: "Black Knight", 
            -3: "Black Bishop", 
            -4: "Black Rook", 
            -5: "Black Queen", 
            -6: "Black King",
        }

        self.emptySpaceLocation =  ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
                                    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
                                    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
                                    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']
    
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.checkboard()

    def getEmptySpaceLocations(self):
        return self.emptySpaceLocation
    
    def print_board(self):
        for i in self.board:
            print(i)

    ## Creates a checkboard with values on the grid, such as a8, b5, c3, etc
    def checkboard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = [chr(97 + col) + str(8 - row)]

        return self.board
    
    #######################
    ##       Rules       ##
    #######################