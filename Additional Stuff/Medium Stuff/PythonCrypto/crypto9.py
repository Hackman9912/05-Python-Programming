alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter a string: ")

input_length = len(string_input)

string_output = ""

for i in range(input_length):
    character = string_input[i]
    location_of_character = alphabets.find(character)
    new_location = location_of_character + 3;
    string_output = string_output + alphabets[new_location]

print("Encrypted text: ", string_output)







# print(string_input)

# print(input_length)
