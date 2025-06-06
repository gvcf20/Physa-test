from gameModelling.game import Game


def runGame(debug = False):

    game = Game(1,1, debug)

    winner = 0

    while winner == 0:

        winner = game.play_round()

        game.round += 1

    if debug == True:
        print(f'Player {winner} Wins')

    return winner

if __name__ == '__main__':

    runGame()