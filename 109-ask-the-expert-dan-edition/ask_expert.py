from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('ai_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
            
def write_to_file(animal_name, animaltype):
    with open('ai_data.txt', 'a') as file:
        file.write('\n' + animal_name + '/' + animaltype)

print('Ask the Expert - Type of Different Prehistoric Animals')
root = Tk()
root.withdraw()
the_world = {}

read_from_file()

while True:
    query_country = simpledialog.askstring('Animal', 'Type the name of a prehistoric animal (mosasaur, pliosaur, etc):')
    
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The type of animal of ' + query_country + ' is ' + result + '!')
    else:
        new_type = simpledialog.askstring('Teach me', 'I don\'t know! ' + 'What type of animal is ' + query_country + '?')
        the_world[query_country] = new_type
        write_to_file(query_country, new_type)
        
root.mainloop()
       