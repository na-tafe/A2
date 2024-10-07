"""
Created on 26 September 2024
version1
Nadifa Aziza
20027521

In the first part of this assessment, you must design, code, and test a program that uses a Python list data structure. 
Use the following scenario: 
•	A list that stores at least 12 of your favourite actors/actresses’ names.
•	A list that stores at least 12 of your favourite movies.
•	A list that stores at least 12 of your favourite games.
1.	Write a Python program that provides the ability to: 
1.1.	Create a list from scenario above
1.2.	Add a value to the list 
1.3.	Delete a value from the list 
1.4.	Sort all the data in the list in the ascending order. Sort all the data in the list in the descending order. 
1.5.	Search for the value in the list asking user for input.
2.	Debug and test your program. You must write unit tests to test the functionality specified above. Screenshot your test results. 
3.	Comment your programs and upload your evidence in compressed format into the Blackboard assessment area.

"""


# coding

# function definitions (3)

def add_value(list_name,value) :

    list_name.append(value)

    return list_name

def sort_value(list_name) :
    list_name.sort()
    return list_name

def delete_value(list_name, value):
    if value in list_name:
        list_name.remove(value)
    else:
        print(value, " is not FOUND") 
    return list_name 

def search_value(list_name, value):
    if value in list_name:
        print(value, "is found in the list")
        return list_name
    else:
        print(value, "is not found in the list")
        return list_name
        
movie_stars = [    
    "Leonardo DiCaprio",
    "Meryl Streep",
    "Tom Hanks",
    "Scarlett Johansson",
    "Denzel Washington",
    "Natalie Portman",
    "Brad Pitt",
    "Halle Berry",
    "Robert Downey Jr.",
    "Viola Davis",
    "Morgan Freeman",
    "Jennifer Lawrence"] # movie_stars = list()
movies = [    
    "The Shawshank Redemption",
    "The Godfather",
    "Pulp Fiction",
    "Forrest Gump",
    "Inception",
    "The Dark Knight",
    "Fight Club",
    "The Matrix",
    "Interstellar",
    "Gladiator",
    "Titanic",
    "Avatar"] # movie = list()
games = [    
    "The Legend of Zelda: Breath of the Wild",
    "The Witcher 3: Wild Hunt",
    "Minecraft",
    "Dark Souls",
    "Red Dead Redemption 2",
    "Overwatch",
    "Fortnite",
    "God of War",
    "Hollow Knight",
    "DOOM (2016)",
    "Celeste",
    "Final Fantasy VII"]  # games = list()

while True: 

    category_type = input("Please Enter category type e.g., S(tars), M(ovie), G(ames), E(nd) => ")

    if category_type == 'E':
        print("Thank you. You are now exiting the program ")
        break 
    else:
        if category_type == 'S':
            list_type = movie_stars
        else:
            if category_type == 'M':
                list_type = movies
            else:
                if category_type == 'G':
                    list_type = games
                else:
                    print("Unknown input", category_type)
                    continue
                
        while True:      
            instruction_type = input("Please enter instruction type e.g., A(dd), D(elete), S(orting), sea(R)ch, P(revious menu) => ").strip().upper()
            if instruction_type == "P":
                break
            else:
                if instruction_type == "A":
                    value = input("Please Enter Value :")
                    list_type = add_value(list_type, value )
                else:
                    if instruction_type == "D":
                        value = input("Please Enter Value :")
                        list_type = delete_value(list_type, value)
                    else:
                        if instruction_type == "S":
                            value = input("Please Enter Value :")
                            list_type = sort_value(list_type)
                        else:
                            if instruction_type == "R":
                                value = input("Please enter value to search: ")
                                list_type = search_value(list_type)
                            else:
                                print("invalid instruction")
                                continue


            print(list_type) 


# testing 
