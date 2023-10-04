# first oops concept project TIC TAC TOE
class Game:
    def start():
       board = [[" " for _ in range(3)] for _ in range(3)]
    #    print(board)
       for row in board:
        print(" | ".join(row))
        print("-" * 9)     
                  




if __name__=="__main__":
    print("Welcome to Tic-Tac-Toe!")

    Game.start()