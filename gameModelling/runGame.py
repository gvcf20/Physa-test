from gameModelling.game import Game


def runGame(init1 = 1, init2 = 1,debug = False):

    game = Game(init1,init2, debug)

    winner = 0

    while winner == 0:

        winner = game.play_round()

        game.round += 1

    if debug == True:
        print(f'Player {winner} Wins')

    return winner, game

if __name__ == '__main__':

    runGame()