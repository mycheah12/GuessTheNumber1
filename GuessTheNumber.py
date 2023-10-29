import random 

#generate a random answer within 1 and 100
answer = random.randint(1,100)

def welcome():
    logo = """
    
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                                                                 
                                                                                                                                                                         
                                                                                                                                                                         
    """
    print(logo)
    print("welcome to number guessing game.\nI am thinking a number within 1 and 100.\nTry to geuss it.")
def game_mode (option):
    chance = 0
    while option != 1 and option != 2:
        option = int(input("Choose between 1 and 2, try again:"))
    if option == 1:
        chance = 10
    else:
        chance = 5
    return chance

def guess_attempts(guess,correct_ans,chance):
    if guess > answer:
        print(f"\n{guess} is larger than answer.You have {chance} attempts(s) left.")
        correct_ans = False
        return correct_ans
    elif guess < answer:
        print(f"\n{guess} is smaller than answer.You have {chance} attempts(s) left.")
        correct_ans = False
        return correct_ans
    elif guess == answer:
        print(f"\nYou make the correct guess. The answer is {answer}.")
        correct_ans = False
        return correct_ans
    
def play(option):
    while option != 1 and option != 2:
        option = int(input("Invalid. Press 1 to play again and 2 to exit:"))
    if option != 1:
        return False
    else:
        return True

def main():
    again = True
    while again:
        welcome()
        #define mode and attempts
        mode = int(input(("Press 1 for easy mode while 2 for hard mode: ")))
        attempts = game_mode(mode)

        #user's first guess
        revealed =  False
        guess = int(input("Please give a guess: "))
        attempts -= 1
        guess_attempts(guess,revealed,attempts)
        
        
        #while attempts != 0, repeat the guess
        while attempts != 0 and not revealed:
            guess = int(input("Please give a guess: "))
            attempts -= 1
            revealed = guess_attempts(guess,revealed,attempts)
            
        
        #if user did not make the correct guess within attempts
        if attempts == 0 and not revealed:
            play_again = int(input((f"The answer is {answer}. Press 1 to try again and 2 to quit:")))
        elif revealed:
            play_again = int(input((f"Congratulations! Press 1 to try again and 2 to quit:")))
        
        play
        (play_again)




if __name__ == '__main__':
    main()