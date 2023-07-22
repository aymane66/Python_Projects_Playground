import Paper_scissor_rock

game = Paper_scissor_rock.Game

name = input("Your name: ")
game.f_player(name)

rounds = int(input("Rounds: "))
game.f_rounds_num(rounds)

choice = input("Your choice (rock, paper, scissors): ")
game.f_choices(choice)


game.f_result()


