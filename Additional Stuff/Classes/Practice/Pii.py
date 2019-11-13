"""
3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods. Also, write a program that creates
    three instances of the class. One instance should hold your information, and the other two
    should hold your friends’ or family members’ information.

"""
class Pii:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self, name):
        return self.__name
    
    def get_address(self, address):
        return self.__address

    def get_age(self, age):
        return self.__age

    def get_phone_number(self, phone_number):
        return self.__phone_number
    
    def __str__(self):
        return f'\nName: {self.__name:} \nAddress: {self.__address:} \nAge: {self.__age:} \nPhone Number: {self.__phone_number:}\n '