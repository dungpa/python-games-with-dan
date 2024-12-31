import random

def get_secret_word():       
    words = ['metaphor', 'elephant', 'absolute', 'abstract', 'draconic', 'airplane', 'gigantic', 'grateful']
    return random.choice(words)

def get_lives():        
    difficulty = input('Choose difficulty (type 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
    difficulty = int(difficulty)

    if difficulty == 1:
        return 12
    elif difficulty == 2:
        return 9
    else:
        return 6

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

def run_game(lives, clue, guessed_word_correctly, heart_symbol, secret_word):        
    while lives > 0:
        print(clue)
        print('Lives left: ' + heart_symbol * lives)
        guess = input('Guess a letter or the whole word: ')
        
        if guess == secret_word:
            guessed_word_correctly = True
            break
            
        if guess in secret_word:
            update_clue(guess, secret_word, clue)
        else:
            print('Incorrect. You lose a life')
            lives -= 1
            
    if guessed_word_correctly:
        print('You won! The secret word was ' + secret_word)
    else:
        print('You lost! The secret word was ' + secret_word)
        
secret_word = get_secret_word()
clue = list('????????')
heart_symbol = u'\u2764'
guessed_word_correctly = False
        
lives = get_lives()
run_game(lives, clue, guessed_word_correctly, heart_symbol, secret_word)
