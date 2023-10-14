import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempt_left = 0
guessed = False
correct_answer = random.randint(1, 101)
difficulty = input("Choose a difficulty, type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt_left = 10
else:
    attempt_left = 5

def check_user_guess():
    global attempt_left
    global guessed
    if user_guess > correct_answer:
        attempt_left -= 1
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempt_left} attempts remaining to guess the number.")
        return
    elif user_guess < correct_answer:
        attempt_left -= 1
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempt_left} attempts remaining to guess the number.")
        return
    else:
        guessed = True
        print(f"You got it! The answer was {correct_answer}")
    
    

while attempt_left > 0 and guessed == False:
    user_guess = int(input("Make a guess: "))
    check_user_guess()
    
if attempt_left == 0:
    print("You run out of guess, you lose.")

