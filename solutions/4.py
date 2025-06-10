import sys
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from gameModelling.game import Game

from gameModelling.runGame import runGame

def winningProbability(j):

    player1 = 0
    player2 = 0

    for i in (range(10000)):

        winner,_ = runGame(init2=j)

        if winner == 1:
            player1 += 1
        elif winner == 2:
            player2 += 1

    prob1 = player1/(player1+player2)
    prob2 = player2/(player1+player2)

    if prob1 == prob2:
        return j
    elif prob1 - prob2 <= 0.01 and prob1 - prob2 >= -0.01:
        return (j,0.01)
    else:
        return False
    
from collections import Counter

def count_numbers(list):
    counter = Counter()

    for sublist in list:
        for item in sublist:
            if isinstance(item, tuple):
                numero = item[0]
                counter[numero] += 1
            else:
                 counter[item] += 1

    return counter
    
if __name__ == '__main__':

    start_position2 = []
    
    for i in tqdm(range(100)):
        numeros = []
        for j in range(1,37):

            k = winningProbability(j=j)

            if k != False:

                numeros.append(k)

        start_position2.append(numeros)

    resultado = count_numbers(start_position2)
    print(resultado)
    with open("resultado4.txt", "w") as f:
        for numero, count in resultado.items():
            f.write(f"{numero}: {count}\n")