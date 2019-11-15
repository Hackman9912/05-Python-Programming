"""
4. Chick-fil-a vs Popeye's Chicken Sandwich Quest
    Using a superclass of Person with two subclasses Student and Instructor create 
    a program that determines who is going to go where and how we'll grade the 
    sandwiches and determine a winner. Get creative with this one. Add in some 
    methods and have fun with it.I'll leave 
    this open to see what you come up with. 
	
"""
import sandwich
import random
import pprint

def main():
    instructors = []
    students = []
    participants = int(input('Enter the number of people participating in the great chicken showdown! '))
    get_part(participants, instructors, students)
    list_print(instructors)
    list_print(students)
    name_list = get_names(instructors, students)
    random.shuffle(name_list)
    if (len(name_list) % 2) ==0:
        chik = name_list[:len(name_list)//2]
        pope = name_list[len(name_list)//2:]
    else:
        chik = name_list[:(len(name_list)+1)//2]
        pope = name_list[(len(name_list)+1)//2:]
    print("Here are the folks going to Chik-Fil-A")
    pprint.pprint(chik)
    print("Here are the folks going to Popeyes")
    pprint.pprint(pope)
def get_part(count, ins_list, stu_list):
    for i in range(count):
        print(f'Person {i+1:}')
        ptype = 0
        while ptype != 1 and ptype != 2:
            ptype = int(input('If the person is a student press 1\nIf the person is an instructor press 2: '))
        if ptype == 1:
            name = input('Enter the students name: ')
            diet = input('Enter the students dietary restrictions: ')
            rank = input('Enter the rank of the student: ')
            student_obj = sandwich.Student(name, diet, rank)
            stu_list.append(student_obj)
        elif ptype == 2:
            name = input('Enter the instructors name: ')
            diet = input('Enter the instructors dietary restrictions: ')
            ins_type = input('Enter the type of instructor they are: ')
            ins_obj = sandwich.Instructor(name, diet, ins_type)
            ins_list.append(ins_obj)
def list_print(list1):  
    for i in list1:
        print(f'The name is: {i.get_name()}')
        print(f'The dietary restrictions are: {i.get_diet()}')   
def get_names(list1, list2):
    big_list = list1 + list2
    name_list = []
    for i in big_list:
        names = i.get_name()
        name_list.append(names)
    return name_list

main()