import sys
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gameModelling.runGame import runGame


def count_dice_throws():

    dice_counter = []

    for i in (range(10000)):

        _, game = runGame()

        dice_counter.append(game.dice_throws)

    return dice_counter

if __name__ == '__main__':

    avg_dices = {1:[],2:[]}

    for i in tqdm(range(1000)):

        dice_counter = count_dice_throws()

        dices_player1 = 0
        dices_player2 = 0
        for dicio in dice_counter:
            dices_player1 += dicio[1]
            dices_player2 += dicio[2]

        avg_dices_p1 = dices_player1/10000
        avg_dices_p2 = dices_player2/10000

        avg_dices[1].append(avg_dices_p2)
        avg_dices[2].append(avg_dices_p2)

    df = pd.DataFrame(avg_dices)

    df.to_csv('avg_dices.csv')
    
    for key,list in avg_dices.items():

        plt.hist(list, bins=5, edgecolor='black')

        plt.title(f'Histograma dos Dados P{key}')
        plt.xlabel('Valor')
        plt.ylabel('Frequência')

        plt.show()
