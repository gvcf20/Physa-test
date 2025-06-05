from game import Game


def runGame(debug):

    game = Game(1,1, debug)

    winner = 0

    while winner == 0:

        winner = game.play_round()

        game.round += 1

    print(f'Player {winner} Wins')

    return winner

if __name__ == '__main__':

    runGame(False)