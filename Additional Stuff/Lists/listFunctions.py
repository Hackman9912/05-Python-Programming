# Built in functionality for lists

# Append

def main():
    name_list = []

    # Create a variable to control our loop
    again = "y"

    # Add some names to the list
    while again == "y":
        # Get a name from the user
        name = input("Enter a name: ")

        name_list.append(name)

        print("Do you want to add another name? ")
        again = input("y = yea, anything else = no: ")

        print()

    print("Here are the names you entered: ")
    for name in name_list:
        print(name)


# Index function

# This program shows how to get the index of an item in a list and then replace that item with a new item

def main():

    food = ["pizza", "burgers", "chips"]

    print("Here are the items in the food list: ")
    print(food)
    item = input("Which item should I change? ")

    try:
        # Get the item index in the list
        item_index = food.index(item)

        # Get the value to replace it with
        new_item = input("Enter a new value: ")

        # Replace the old item with the new item
        food[item_index] = new_item

        print("Here is the revised list: ")
        print(food)

    except:
        # User entered the wrong thing
        print("That item was not found in the list.")

main()



# This program demonstrates the insert method

def main():

    names = ["James", "Kathy", "Bill"]

    # Display the list
    print("This list before insert: ")

    print(names)

    names.insert(0, "Joe")

    print("This list after the insert: ")

    print(names)


main()


# Sort method on lists

my_list = [9, 5, 7, 3, 2, 1, 0]

print("Original order: ", my_list)
my_list.sort()
print("Sorted order: ", my_list)

# Sorted - not permanent and list.sort is faster

my_list2 = [9, 5, 7, 3, 2, 1, 0]
print("Before sort", my_list2)
print(sorted(my_list2))
print("After sort", my_list2)


# This program shows how to use the romove method from a list

def main():

    food = ['pizza', 'burgers', 'chips']

    print("Here are the foods ", food)

    item  = input("Which item would I remove: ")

    try:

        food.remove(item)

        print('Here is the revised list ', food)

    except ValueError:
        print(' That item was not found: ')

main()


# The reverse method

my_list = [1, 2, 3, 4, 5, 6]
print('Original order: ', my_list)

my_list.reverse()

print('Reversed', my_list)

# The delete statement: for specific elements

my_list = [1, 2, 3, 4, 5]

print('Here is the list: ', my_list)

del my_list[2]
print('After deletion: ', my_list)


# min and max funciton

my_list = [5, 4, 7, 8, 3, 2, 0, 9, 1]
print("The lowest value is: ", min(my_list))

print('The highest value is: ', max(my_list))