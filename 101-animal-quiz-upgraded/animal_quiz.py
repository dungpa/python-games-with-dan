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

questions = ['Which bear lives at the North Pole?', 'Which is the fastest land animal?', 'Which is the largest animal?']
answers = ['polar bear', 'cheetah', 'blue whale']

for index in range(0, 3):
    guess = input(questions[index])
    check_guess(max_attempt, guess, answers[index])

print('Your score is ' + str(score))


        
