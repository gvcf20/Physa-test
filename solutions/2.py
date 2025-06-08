import sys
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gameModelling.runGame import runGame


def count_snakes():

    snake_counter = []

    for i in (range(10000)):

        _, game = runGame()

        snake_counter.append(game.snake_counter)

    return snake_counter


if __name__ == '__main__':

    avg_snakes = {1:[],2:[]}

    for i in tqdm(range(1000)):
        snake_counter = count_snakes()

        snakes_player1 = 0
        snakes_player2 = 0
        for dicio in snake_counter:
            snakes_player1 += dicio[1]
            snakes_player2 += dicio[2]

        avg_snakes_p1 = snakes_player1/10000
        avg_snakes_p2 = snakes_player2/10000

        avg_snakes[1].append(avg_snakes_p1)
        avg_snakes[2].append(avg_snakes_p2)

    df = pd.DataFrame(avg_snakes)

    df.to_csv('avg_snakes.csv')
    
    for key,list in avg_snakes.items():

        plt.hist(list, bins=5, edgecolor='black')

        plt.title(f'Histograma dos Dados P{key}')
        plt.xlabel('Valor')
        plt.ylabel('Frequência')

        plt.show()
