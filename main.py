import figures as f
import board
            
game = board.Game()
pawn1 = f.whitePawn(['a',2], game)
game.printBoard()
print(f'Current pos: {pawn1.pos}')
print(f'Possible Moves: {pawn1.possibleMoves}')
print(f'Possible Beatings: {pawn1.possibleBeatings}')
pawn1.setPosition(['a',4])
print(f'Pos after movement: {pawn1.pos}')
print(f'Possible Moves: {pawn1.possibleMoves}')
pawn1.setPosition(['a',6])
print(f'Pos after movement: {pawn1.pos}')
print(f'Possible Moves: {pawn1.possibleMoves}')
