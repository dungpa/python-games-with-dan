import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'fluffy', 'proud', 'brave', 'sleek', 'intimidating', 'scary', 'cool', 'flying', 'spiky']

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'black', 'white']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'shark', 'kaiju', 'fish', 'pokemon', 'lion', 'lizard', 'snake']

print('Welcome to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    colour = random.choice(colours)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + colour + noun + str(number) + special_char
    print('Your new password is: %s' % password)
    
    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break
        
print('Very well.')

