def check_guess(max_attempt, guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < max_attempt:
        if guess.lower() == answer.lower():
            print ('Correct answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < max_attempt - 1:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
           
    if attempt == max_attempt:
        print('The correct answer is ' + answer)

score = 0
max_attempt = 3
print('Guess the animal!')

guess1 = input('Which bear lives at the North Pole?')
check_guess(max_attempt, guess1, 'polar bear')
guess2 = input('Which is the fastest land animal?')
check_guess(max_attempt, guess2, 'cheetah')
guess3 = input('Which is the largest animal?')
check_guess(max_attempt, guess3, 'blue whale')

print('Your score is ' + str(score))


        
