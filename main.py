import figures as f
import board
            
game = board.Game()
pawn1 = f.whitePawn('Pawn', 'White', ['a', 2], game)
pawn2 = f.blackPawn('Pawn', 'Black', ['b',7], game)
pawn3 = f.whitePawn('Pawn', 'White', ['b', 2], game)
print(f'Starting locations {game.figureLocations}')
pawn1.setPosition(['a', 4])
pawn3.setPosition(['b', 4])
pawn3.setPosition(['b', 5])
pawn1.setPosition(['a', 4])     # At this point we see that white pawn cannot beat another white pawn
pawn2.setPosition(['b', 6])
print(f'Final locations {game.figureLocations}')
# print(f'Current pos: {pawn3.pos}')
print(f'Possible Moves: {pawn2.possibleMoves}')
# print(f'Possible Beatings: {pawn2.possibleBeatings}')
print(f'Possible Beatings: {pawn1.possibleBeatings}')
# print(f'Pos after movement: {pawn1.pos}')
# print(f'Possible Moves: {pawn1.possibleMoves}')