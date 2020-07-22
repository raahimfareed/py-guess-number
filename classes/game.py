import random


class Game:
    def __init__(self):
        self.limit = (0, 100)
        self.retries = 10

    def start(self):
        init = True
        running = False
        guessed = False
        number_generated = 0
        tries = 10

        while init:
            start_menu = str(input("Would you like to play Guess The Number? (y/n): "))
            if start_menu == "y" or start_menu == "n":
                if start_menu == "y":
                    running = True
                    init = False
                else:
                    init = False
            else:
                print("Please choose a valid option!")

        if running:
            number_generated = random.randint(self.limit[0], self.limit[1])

        while running:
            print("You will have to guess a random number from 0 - 100.\n"
                  "You will have " + str(self.retries) + " tries.\nGood luck!")

            while not guessed:
                if self.retries > 0:
                    user_guess = input("Guess: ")
                    if int(user_guess) != int(number_generated):
                        # print(user_guess, number_generated)
                        self.retries -= 1
                        print("Wrong guess!")
                        print(f"Hint: {self.hints(number_generated)}")
                    else:
                        guessed = True
                        running = False
                        break
                else:
                    print("Oops! You're out of tries. Better luck next time")
                    running = False
                    break

        if guessed:
            print("Yay! You won")

    def hints(self, generated_num):
        hints = [
            f"(x * 2) - 11 = {str((generated_num * 2) - 11)}",
            f"(x / 2) * 4 + 1 = {str((generated_num / 2) * 4 + 1)}",
            f"x(3 + 8) = {generated_num * (3 + 8)}",
            f"(x + 3)/6 = {(generated_num + 3) / 6}",
            f"3x + 9 = {(generated_num * 3) + 9}",
            f"(x + 3) * 3 = {(generated_num + 3) / 6}",
            f"3x + 9 - 9 = {(generated_num * 3) + 9 - 9}",
            f"x/x = 1",
            # f"(x + 3)/6 = {(generated_num + 3) / 6}",
            # f"(x + 3)/6 = {(generated_num + 3) / 6}",
        ]

        return_var = random.randint(0, len(hints))

        return hints[return_var]
