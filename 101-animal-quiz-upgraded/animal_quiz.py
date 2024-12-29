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

questions = ['What is the least intelligent shark?', 'What jawless animal has four eyes?', 'Which is the second largest land animal?', 'What is the lizard that lives in the sea?', 'What animal is the graphics of this programming language named after?']
answers = ['basking shark', 'lamprey', 'asian elephant', 'marine iguana', 'turtle']

for index in range(0, 5):
    guess = input(questions[index])
    check_guess(max_attempt, guess, answers[index])

print('Your score is ' + str(score))


        
