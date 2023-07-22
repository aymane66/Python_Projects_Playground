import random


class Game:

    def __init__(self, player_name, rounds, choice, computer, choices, winner):
        self.player_name = ""
        self.rounds = int(rounds)
        self.choice = choice
        self.computer = computer
        self.choices = []
        self.winner = None

    def f_player(self, player_name):
        return self.player_name

    def f_rounds_num(self):
        return self.rounds

    def f_choices(self):
        choices = ["rock", "paper", "scissors"]
        self.computer = random.choice(choices)

        for i in choices:
            if i == self.choice.lower:
                return True
            else:
                return "Error: Please choose one of the three choices."

    def f_result(self):
        ai_points = 0
        player_points = 0

        while self.f_choices() is True:
            for r in range(self.rounds):
                if self.computer == self.choices[0] and self.choice == self.choices[2]:
                    print("Winner: ", self.computer)
                    ai_points += 1
                elif self.computer == self.choices[1] and self.choice == self.choices[0]:
                    print("Winner: ", self.computer)
                    ai_points += 1
                elif self.computer == self.choices[2] and self.choice == self.choices[1]:
                    print("Winner: ", self.computer)
                    ai_points += 1
                elif self.computer == self.choice:
                    print("Draw")
                else:
                    print("Winner: ", self.player_name)
                    player_points += 1

            print("Scores: ")
            print(f"{self.player_name}: {player_points}")
            print(f"{self.computer}: {ai_points}")
            print("Winner is: ")
            if player_points > ai_points:
                print(player_points)
            elif ai_points > player_points:
                print(ai_points)
            else:
                print("Draw")
