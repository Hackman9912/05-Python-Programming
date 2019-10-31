# 1. Bug Collector
# A bug collector collects bugs every day for seven days. Write a program that keeps a running total of the number of bugs collected during the seven days. 
# The loop should ask forthe number of bugs collected for each day, and when the loop is finished, the programshould display the total number of bugs collected.
def main():

    counter = 1
    total = 0

    while counter <= 7:
        bugs = int(input("Enter the number of bugs you caught today: "))
        total += bugs
        counter += 1
    print(f"You caught {total:} bugs in the past 7 days")

main()