import figures as f
import board
            
game = board.Game()
pawn1 = f.whitePawn('a2', game)
game.print_board()
pawn1.move('a4')
print(pawn1.pos)


# game.pawn_movement(2, 3)
