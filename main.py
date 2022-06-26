import random

def game():

    game = ['rock', 'paper', 'scissor']
    maxscore = 10
    pscore = 0
    sscore = 0

    while pscore < maxscore and sscore < maxscore:
        player = input("rock/paper/scissor?: ").lower()
        system = random.choice(game)

        if player == system:
            print("It's A Tie!")
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

        # PLAYER WINS

        elif player == "rock" and system == "scissor":
            print("You Got A Point!")
            pscore += 1
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

        elif player == "paper" and system == "rock":
            print("You Got A Point!")
            pscore += 1
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

        elif player == "scissor" and system == "paper":
            print("You Got A Point!")
            pscore += 1
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

        # SYSTEM WINS

        elif system == "rock" and player == "scissor":
            print("System Got A Point!")
            sscore += 1
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

        elif system == "paper" and player == "rock":
            print("System Got A Point!")
            sscore += 1
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

        elif system == "scissor" and player == "paper":
            print("System Got A Point!")
            sscore += 1
            print("Your Score: {}".format(pscore))
            print("System Score: {}".format(sscore))

    if sscore == maxscore:
        print("System Wins!")

    elif pscore == maxscore:
        print("You Win!")

    else:
        pass


game()

opinion = input("Play Again?(y/n): ").lower()

while opinion == "y":
    game()
    opinion = input("Play Again?(y/n): ").lower()

if opinion != "y" or opinion != "n":
    opinion = input("Play Again?(y/n): ").lower()


#A Code By Sree Teja Dusi
#Website: https://sreetejadusi.me
#Facebook: https://facebook.com/sreetejadusi
#Twitter: https://twitter.com/sreetejadusi
#LinkedIn: https://linkedin.com/in/sreetejadusi
#Instagram: https://instagram.com/sreeteja_dusi
#GitHub: https://github.com/sreetejadusi
