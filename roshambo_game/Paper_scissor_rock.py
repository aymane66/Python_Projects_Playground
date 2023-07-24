import random


class Game:

    def __init__(self, player_name, rounds):
        self.player_name = player_name
        self.rounds = int(rounds)
        self.choices = ["rock", "paper", "scissors"]

    def f_player(self):
        return self.player_name

    def f_rounds_num(self):
        return self.rounds

    def f_choices(self, choice):
        choice = choice.lower()
        if choice in self.choices:
            self.choice = choice
            self.computer = random.choice(self.choices)
            return True
        else:
            return "Error: Please choose one of the three choices."

    def f_result(self):
        ai_points = 0
        player_points = 0

        for r in range(self.rounds):
            player_choice = input("Enter your choice (rock/paper/scissors): ")

            if self.f_choices(player_choice) is True:
                if self.computer == self.choice:
                    print("Computer´s choice: ", self.computer)
                    print("Winner: Draw")
                elif self.computer == self.choices[0] and self.choice == self.choices[2]:
                    print("Computer´s choice: ", self.computer)
                    print("Winner: Computer")
                    ai_points += 1
                elif self.computer == self.choices[1] and self.choice == self.choices[0]:
                    print("Computer´s choice: ", self.computer)
                    print("Winner: Computer")
                    ai_points += 1
                elif self.computer == self.choices[2] and self.choice == self.choices[1]:
                    print("Computer´s choice: ", self.computer)
                    print("Winner: Computer")
                    ai_points += 1
                else:
                    print("Computer´s choice: ", self.computer)
                    print("Winner: ", self.player_name)
                    player_points += 1

        print()
        print("========== Scores ===========")
        print(f"{self.player_name}: {player_points}")
        print(f"Computer: {ai_points}")
        print("Winner is: ")
        if player_points > ai_points:
            print(self.player_name)
        elif ai_points > player_points:
            print("Computer")
        else:
            print("Draw")
        print("=============================")
