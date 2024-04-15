import figures as f
import board
            
game = board.Game()


# white pawn 
wPawn1 = f.whitePawn('Pawn', 'White', ['a', 2], game)
wPawn2 = f.whitePawn('Pawn', 'White', ['b', 2], game)
wPawn3 = f.whitePawn('Pawn', 'White', ['c', 2], game)
wPawn4 = f.whitePawn('Pawn', 'White', ['d', 2], game)
wPawn5 = f.whitePawn('Pawn', 'White', ['e', 2], game)
wPawn6 = f.whitePawn('Pawn', 'White', ['f', 2], game)
wPawn7 = f.whitePawn('Pawn', 'White', ['g', 2], game)
wPawn8 = f.whitePawn('Pawn', 'White', ['h', 2], game)

# black pawn
bPawn1 = f.blackPawn('Pawn', 'Black', ['a',7], game)
bPawn2 = f.blackPawn('Pawn', 'Black', ['b',7], game)
bPawn3 = f.blackPawn('Pawn', 'Black', ['c',7], game)
bPawn4 = f.blackPawn('Pawn', 'Black', ['d',7], game)
bPawn5 = f.blackPawn('Pawn', 'Black', ['e',7], game)
bPawn6 = f.blackPawn('Pawn', 'Black', ['f',7], game)
bPawn7 = f.blackPawn('Pawn', 'Black', ['g',7], game)
bPawn8 = f.blackPawn('Pawn', 'Black', ['h',7], game)


# print(f'Starting locations {game.figureLocations}')
wPawn1.setPosition(['a', 4])
wPawn2.setPosition(['b', 4])
wPawn2.setPosition(['b', 5])
bPawn2.setPosition(['b', 6])
wPawn1.setPosition(['a', 5])
game.visualizeBoard()
# print(f'Final locations {game.figureLocations}')
# print(f'Current pos: {pawn3.pos}')
print(f'Possible Moves: {bPawn2.possibleMoves}')
# print(f'Possible Beatings: {pawn2.possibleBeatings}')
print(f'Possible Beatings: {wPawn1.possibleBeatings}')
print(f'Possible Moves: {wPawn2.possibleMoves}')
# print(f'Pos after movement: {pawn1.pos}')
# print(f'Possible Moves: {pawn1.possibleMoves}')