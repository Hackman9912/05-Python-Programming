# 7. Book Club Points
# Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:
# • If a customer purchases 0 books, he or she earns 0 points.
# • If a customer purchases 1 book, he or she earns 5 points.
# • If a customer purchases 2 books, he or she earns 15 points.
# • If a customer purchases 3 books, he or she earns 30 points.
# • If a customer purchases 4 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she has purchased this month and displays the number of points awarded.

def main():
    books = int(input("Enter the number of books purchased this month: "))

    if books >= 4:
        print("Good job you earned 60 points!")
    elif books == 3:
        print("Good job you earned 30 points!")
    elif books == 2:
        print("Okay job, you eanred 15 points.")
    elif books == 1:
        print("Meh, you only bought one book. 5 points.")
    else:
        print("You suck. Buy some damned books")

main()