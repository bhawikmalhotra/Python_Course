# 4. Simple Guessing Game
# This uses a different type of loop (while) based on a condition.
# The Task: Create a simple "guess the number" game.
# Store a "secret number" in a variable (e.g., secret_number = 7).
# Use a while loop to continuously ask the user to guess the number.
# Inside the loop, use conditions to check their guess:
# If the guess is less than the secret number, print "Too low! Try again."
# If the guess is greater than the secret number, print "Too high! Try again."
# If the guess is equal to the secret number, print "Correct!" and break out of the loop.

secret = 7 


while True:
    num = int(input("guess an number : "))
    if num > secret:
        print("Too high! Try again.")
    elif num < secret:
        print("Too Low! Try again.")
    else:
        print("Right Guess")
        break
    