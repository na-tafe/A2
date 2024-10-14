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
    print(f"Added: {name} with date: {date}.")
    return category_dict

def delete_dict(category_dict, name):
    if name in category_dict:
        del category_dict[name]
        print(f"Deleted: {name}.")
    else:
        print(f"{name} not found in the dictionary.")
    return category_dict

def sort_dict(category_dict, descending=False):
    sorted_items = sorted(category_dict.items(), key=lambda x: x[0], reverse=descending)
    return sorted_items

def search_dict(category_dict, name):
    if name in category_dict:
        print(f"{name} is found: {category_dict[name]}")
    else:
        print(f"{name} not found in the dictionary.")
    return category_dict

# Create dictionaries
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
    "Viola Davis": 1965
}

movie_dict = {
    "The Shawshank Redemption": 1994,
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
    "Avatar": 2009
}

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
    "Final Fantasy VII": 1997
}

# Main loop
def main():
    while True:
        category_type = input("Please enter category type e.g., A(ctor), M(ovie), G(ames), E(nd) => ").strip().upper()
        
        if category_type == 'E':
            print("Thank you. You are exiting the program.")
            break
        
        if category_type == 'A':
            dict_type = actor_dict
        elif category_type == 'M':
            dict_type = movie_dict
        elif category_type == 'G':
            dict_type = game_dict
        else:
            print("Unknown input:", category_type)
            continue
            
        while True:
            instruction_type = input("Please enter instruction type e.g., A(dd), D(elete), S(orting), sea(R)ch, P(revious menu) => ").strip().upper()
            if instruction_type == 'P':
                break
            elif instruction_type == 'A':
                name = input("Enter a name: ")
                date = int(input("Enter the year (yyyy): "))
                dict_type = add_dict(dict_type, name, date)
            elif instruction_type == 'D':
                name = input("Enter a name to delete: ")
                dict_type = delete_dict(dict_type, name)
            elif instruction_type == 'S':
                order = input("Sort in ascending or descending order? (A/D): ").strip().upper()
                descending = order == 'D'
                sorted_items = sort_dict(dict_type, descending)
                for name, year in sorted_items:
                    print(f"{name}: {year}")
            elif instruction_type == 'R':
                name = input("Enter a name to search: ")
                dict_type = search_dict(dict_type, name)
            else:
                print("Invalid instruction. Please try again.")
            
            print()  # For better readability between operations

if __name__ == '__main__':
    main()
