import sys
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from gameModelling.game import Game

from gameModelling.runGame import runGame

def winningProbability():

    player1 = 0
    player2 = 0

    for i in (range(10000)):

        winner,_ = runGame()

        if winner == 1:
            player1 += 1
        elif winner == 2:
            player2 += 1

    prob1 = player1/(player1+player2)
    prob2 = player2/(player1+player2)

    # print(prob1)

    return prob1

if __name__ == '__main__':

    prob_range = []
    for i in tqdm(range(1000)):
        prob_range.append(winningProbability())
        
    plt.hist(prob_range, bins=5, edgecolor='black')

    plt.title('Histograma dos Dados')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')

    plt.show()