# serializing objects
# is the process of converting the object to a stream of bytes that can be saved to a file for later retrieval. in Python , object serialization is called pickling.

# Sytax is below
# output_file = open('mydata.dat', 'wb')
# pickle.dump(object, file)

# This program demonstrates object pickling

import pickle

# call main funciton
def main():
    # control loop repetition
    again = 'y'

    # Open a file for binary writing
    output_file = open('information.dat', 'wb')

    # get data until the user wants to stop
    while again.lower() =='y':
        # get data about a person and save it
        save_data(output_file)


        # Does the user want to enter more data?
        again = input("Enter more data? (y/n): ")

    # close the file
    output_file.close()
# The save data function gets data about a person, stores it in a dictionary and then pickles the dictionary to the specified file
def save_data(file):
    # create an empty dictionary
    person = {}

    # Get the data for a person and store it in a dictionary
    # person['name'] = input('Name: ')
    # person['age'] = input('age: ')
    # person['weight'] = float(input("weight: "))

    person.update({'name' : input('Name: '), 'age' : input('age: '), 'weight' : float(input("weight: "))})
    # Pickle the dictionary
    pickle.dump(person, file)

# call main
main()