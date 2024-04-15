class Game:
    
    ### Need classes for each fig ###

    ####################################
    ##       Initial Game State       ##
    ####################################
    
    def __init__(self):
        # For broad visualization
        self.board = [[[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]],
                      [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]]]
        
        self.figureLocations = {}

        # Will remove after adapting figures 
        self.emptySpaceLocation =  [['a',6], ['b',6], ['c',6], ['d',6], ['e',6], ['f',6], ['g',6], ['h',6],
                                    ['a',5], ['b',5], ['c',5], ['d',5], ['e',5], ['f',5], ['g',5], ['h',5],
                                    ['a',4], ['b',4], ['c',4], ['d',4], ['e',4], ['f',4], ['g',4], ['h',4],
                                    ['a',3], ['b',3], ['c',3], ['d',3], ['e',3], ['f',3], ['g',3], ['h',3]]

        self.letterToColumn = {'a':0,
                               'b':1,
                               'c':2,
                               'd':3,
                               'e':4,
                               'f':5,
                               'g':6,
                               'h':7}
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.createLocations()

    # Initializes all positions as empty in figureLocations dictionary
    def createLocations(self):
        for row in range(8):
            for col in range(8):
                self.figureLocations[f'{chr(97 + col)}{8 - row}'] = None
    
    # Visualizes the board based on the board var
    def visualizeBoard(self):
        for item in self.figureLocations:
            if self.figureLocations[item]:
                obj = self.figureLocations[item]
                row = obj.pos[1] - 1
                column = self.letterToColumn[obj.pos[0]]

                self.board[row][column] = [f'{obj.color} {obj.name}']
                
        for i in range(len(self.board)-1,-1,-1):
            print(self.board[i])
    
    #######################
    ##       Rules       ##
    #######################