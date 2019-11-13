"""

3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods. Also, write a program that creates
    three instances of the class. One instance should hold your information, and the other two
    should hold your friends’ or family members’ information.

"""
import Pii


def main():
    me = est_claobj('you')
    friend = est_claobj('a friend')
    family = est_claobj('a family member')
    print(me, friend, family)

def est_claobj(var1):
    name = input(f"Enter the following info for {var1:}. Name: ").title()
    address = input(f"Enter the following info for {name:}. Address: ")
    age = input(f"Enter the following info for {name:}. Age: ")
    phone_number = input(f"Enter the following info for {name:}. Phone Number: ")
    return Pii.Pii(name, address, age, phone_number)

 
    
main()