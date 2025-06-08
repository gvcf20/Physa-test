import random



class Game:

    def __init__(self, player1, player2, _debug):

        self.debug = _debug

        self.players = {1:player1,2:player2}

        self.snake_counter = {1:0,2:0}

        self.round = 1

        self.stairs = {3:16, 5:7,15:25, 18:20, 21:32} # Key represents the base and values the top of the stair
        self.stairs_base = list(self.stairs.keys())

        self.snakes = {12:2, 14:11, 17:4, 31:19, 35:22} # Key represents head and values the tail of the snake
        self.snakes_head = list(self.snakes.keys())

        pass

    def throw_dice(self):

        return random.randint(1,6)
    
    def log(self, message):
        if self.debug:
            print(message)

    
    def play_round(self):
        
        self.log(f'Round {self.round} \n')

        for player,player_position in self.players.items():

            self.log(f'Player {player} at position {player_position} \n')

            dice_result = self.throw_dice()

            self.log(f'Dice result for player {player}: {dice_result} \n')

            self.players[player] += dice_result

            self.snake_counter[player] += self.check_stairs_and_snakes(player)

            if self.players[player] >= 36:

                self.log(f'Player {player} Wins \n')

                return player
            
            self.log(f'Player {player} goes to position {self.players[player]} \n')

        return 0
    
    

    def check_stairs_and_snakes(self, player):

        if self.players[player] in self.stairs_base:

            self.log(f'Player {player} will climb a stair from {self.players[player]} to {self.stairs[self.players[player]]}\n')

            self.players[player] = self.stairs[self.players[player]]

            return 0
            
        elif self.players[player] in self.snakes_head:
            
            self.log(f'Player {player} fell into a snake and will go to position {self.snakes[self.players[player]]} \n')

            self.players[player] = self.snakes[self.players[player]]

            return 1

        return 0



