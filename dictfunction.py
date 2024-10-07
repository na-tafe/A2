"""
Created on Wed Sep 25 23:08:22 2024
version 1
@author: Nadifa Aziza
Student ID: 20027521


•	A dictionary that stores at least 12 of your favourite actors/actresses’ names and birthdays.
•	A list that stores at least 12 of your favourite movies and release year.
•	A list that stores at least 12 of your favourite games and release year.
1.	Write a Python program that provides the ability to: 
1.1.	Create a dictionary from the scenario above
1.2.	Add a value to the dictionary
1.3.	Delete a value from the dictionary
1.4.	Sort all the data in the dictionary in the ascending order. Sort all the data in the dictionary in the descending order. 
1.5.	Search for the value in the dictionary asking user for input.

"""

# Define functions for dictionary operations
def add_dict(category_dict, name, date):
        category_dict[name] = date
#        print(f"Added: {name} with date: {date}.") #adds the entry to the dictionary
        return category_dict

def delete_dict(category_dict, name):
    if name in category_dict:
        del category_dict[name]
#        print(f"Deleted: {name}.") #if the name found in the dictionary, then can delete
        return category_dict
    else:
        print(f"{name} not found in the dictionary.") # if not, action can't be done
        return category_dict

def sort_dict(category_dict): #no input value needed
    sorted_items = sorted(category_dict.items()) #sort the items in the dict
#    for name, date in sorted_items:
#        print(f"{name}: {date}") #print name and date after being sorted
    return sorted_items

def search_dict(category_dict, name): #input name to search
    if name in category_dict:
        print(name, " is found")
        return category_dict
        

#        print(f"{name}: {category_dict[name]}") #if inputted value is found on the list, print the associated info
    else:
        print(name, "not found in the dictionary.") #else, tell user entered value is not in the dictionary
        return category_dict
    


# Create empty dictionaries
actor_dict = {    
    "Leonardo DiCaprio": 1974,
    "Meryl Streep": 1949,
    "Tom Hanks": 1956,
    "Natalie Portman": 1981,
    "Denzel Washington": 1954,
    "Scarlett Johansson": 1984,
    "Morgan Freeman": 1937,
    "Jennifer Lawrence": 1990,
    "Brad Pitt": 1963,
    "Halle Berry": 1966,
    "Robert Downey Jr.": 1965,
    "Viola Davis": 1965}
movie_dict = {"The Shawshank Redemption": 1994,
    "The Godfather": 1972,
    "Pulp Fiction": 1994,
    "Forrest Gump": 1994,
    "Inception": 2010,
    "The Dark Knight": 2008,
    "Fight Club": 1999,
    "The Matrix": 1999,
    "Interstellar": 2014,
    "Gladiator": 2000,
    "Titanic": 1997,
    "Avatar": 2009}
game_dict = {
    "The Legend of Zelda: Breath of the Wild": 2017,
    "The Witcher 3: Wild Hunt": 2015,
    "Minecraft": 2011,
    "Dark Souls": 2011,
    "Red Dead Redemption 2": 2018,
    "Overwatch": 2016,
    "Fortnite": 2017,
    "God of War": 2018,
    "Hollow Knight": 2017,
    "DOOM (2016)": 2016,
    "Celeste": 2018,
    "Final Fantasy VII": 1997}

# Main loop
while True: 
    #prompt for input for category type
    category_type = input("Please enter category type e.g., A(ctor), M(ovie), G(ames), E(nd) => ").strip().upper()
    
    if category_type == 'E':
        print("Thank you. You are exiting the program.") #exiting message
        break #to exit the loop
    else:
        if category_type == 'A':
            dict_type = actor_dict # input 'A' will assign to actor_dict
        elif category_type == 'M':
            dict_type = movie_dict  # input 'M' will assign to movie_dict
        elif category_type == 'G':
            dict_type = game_dict  # input 'G' will assign to game_dict
        else:
            print("Unknown input:", category_type) #otherwise, display invalid message
            continue #prompt input again
            
      #nested looop      
        while True:
            #after choosing category type, choose instructions that needs to be done (function defined at the top)
            instruction_type = input("Please enter instruction type e.g., A(dd), D(elete), S(orting), sea(R)ch, P(revious menu) => ").strip().upper()
            if instruction_type == 'P':
                break #exit this loop
            elif instruction_type == 'A':
                name = input("Enter a name: ") #first entry needed is the name
                date = int(input("Enter the date (yyyy): ")) #second entry needed is the date
                dict_type = add_dict(dict_type, name, date) #function adds name and date to the dictionary
            elif instruction_type == 'D':
                name = input("Enter a name to delete: ") #enter the name that wants to be deleted
                dict_type = delete_dict(dict_type, name) #run the functionusing the input (delete if entry is found, error message if not found)
            elif instruction_type == 'S':
                dict_type = sort_dict(dict_type)  # Sort in dictionary in order
            elif instruction_type == 'R':
                name = input("Enter a name to search: ") #enter the name that wants to be searched
                dict_type = search_dict(dict_type, name) #using the input, run the search function
            else:
                print("Invalid instruction. Please try again.") #other than stated in the instruction, display invalid message
            
            
            print(dict_type)
            # Display the current state of the dictionary after each instruction
#            display_dict(dict_type) #display the current dictionary after instruction being done

