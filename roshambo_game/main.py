import Paper_scissor_rock

player_name = input("Enter your name: ")
rounds = int(input("Enter the number of rounds you want to play: "))
game = Paper_scissor_rock.Game(player_name, rounds)
game.f_result()