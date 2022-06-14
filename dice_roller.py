import random


class Player:
    def __init__(self):
        self.score = 0
        self.turn_score = 0
        self.turn_over = False
        self.turn_count = 0
        self.turn_total = 0
        self.turn_rolls = 0
        self.turn_roll_count = 0
        self.turn_roll_total = 0
        self.turn_roll_average = 0
        self.turn_roll_average_total = 0
        self.turn_roll_average_count = 0
        self.turn_roll_average_average = 0
        self.turn_roll_average_average_total = 0

    def roll(self):
        self.turn_rolls += 1
        self.turn_roll_count += 1
        self.turn_roll_total += random.randint(1, 6)
        self.turn_roll_average = self.turn_roll_total / self.turn_roll_count
        self.turn_roll_average_total += self.turn_roll_average
        self.turn_roll_average_count += 1
        self.turn_roll_average_average = self.turn_roll_average_total / \
            self.turn_roll_average_count
        return self.turn_roll_average

    def hold(self):
        self.score += self.turn_score
        self.turn_over = True
        self.turn_count += 1
        self.turn_total += self.turn_score
        self.turn_rolls = 0
        self.turn_roll_count = 0
        self.turn_roll_total = 0
        self.turn_roll_average = 0
        self.turn_roll_average_total = 0
        self.turn_roll_average_count = 0
        self.turn_roll_average_average = 0
        self.turn_roll_average_average_total = 0
        return self.score

    def reset(self):
        self.score = 0
        self.turn_score = 0
        self.turn_over = False
        self.turn_count = 0
        self.turn_total = 0
        self.turn_rolls = 0
        self.turn_roll_count = 0
        self.turn_roll_total = 0
        self.turn_roll_average = 0
        self.turn_roll_average_total = 0
        self.turn_roll_average_count = 0
        self.turn_roll_average_average = 0
        self.turn_roll_average_average_total = 0


class Game:
    def __init__(self):
        self.players = 0
        self.dice_rolls = 0
        self.dice_size = 0
        self.dice_sum = 0
        self.winner = 0
        self.winner_index = 0

    def roll(self):
        self.dice_rolls = int(input('How many dice would you like to roll? '))
        self.dice_size = int(input('How many sides are the dice? '))
        self.dice_sum = 0
        for i in range(0, self.dice_rolls):
            roll = random.randint(1, self.dice_size)
            self.dice_sum += roll
            if roll == 1:
                print(f'You rolled a {roll}! Critical Fail')
            elif roll == self.dice_size:
                print(f'You rolled a {roll}! Critical Success')
            else:
                print(f'You rolled a {roll}!')
        print(f'You rolled a total of {self.dice_sum}. ')


def main():
    #how many players?
    players = int(input("How many players? "))
    player = 1
    while player <= players:
        print("Player", player, "rolls a dice")
        dice = random.randint(1, 6)
        print("The dice rolled a", dice)
        player += 1

    #create a list of players
    player_list = []
    for i in range(players):
        player_list.append(Player())

    #roll the dice
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success')
        else:
            print(f'You rolled a {roll}!')
    print(f'You rolled a total of {dice_sum}. ')

    #check for a winner
    winner = 0
    for i in range(players):
        if player_list[i].score > winner:
            winner = player_list[i].score
            winner_index = i
    print(f'Player {winner_index + 1} is the winner!')


if __name__ == "__main__":
    main()
