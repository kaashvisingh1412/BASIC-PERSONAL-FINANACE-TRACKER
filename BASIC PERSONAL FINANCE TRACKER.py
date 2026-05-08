# BASIC PERSONAL FINANCE TRACKER

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expenses.append([category, amount])

        print("Expense Added!")

    elif choice == "2":
        print("\n--- Expenses ---")

        for expense in expenses:
            print("Category:", expense[0], "| Amount:", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense[1]

        print("\nTotal Spending =", total)

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
