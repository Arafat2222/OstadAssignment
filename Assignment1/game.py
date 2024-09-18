# Import Library
import random

def game():
    rand = random.randint(1, 100) 
    cnt = 0  

    while True:
        guess = input("Enter your guess: ")
        guess = guess.strip()  
        cnt += 1 
        
        try:
            guess = int(guess)  
            if guess == rand:
                print(f"Congratulations! You've guessed the number in {cnt} attempts.")
                break  
            
            elif rand > guess:
                print("Too Low!")
            elif rand < guess:
                print("Too High!")
        except ValueError:
            print("Please enter a valid integer.") 

# Start the game
if __name__ == "__main__":
    game()
