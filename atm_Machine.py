# Banking program

def show_balance(balance):
    print()
    print(f"Your balance is ${balance:.2f}")
    print()


def deposit():
    print()
    amount = float(input("Enter an amount to deposit: "))
    print()
    if amount <= 0:
        print("Enter an amount greater than 0.")
        print()
        return 0
    else:
        return f"{amount}\n "


def withdraw(balance):
    print()
    amount = float(input("Enter an amount to withdraw: "))
    print()
    if amount > balance:
        print("Insufficient funds.")
        print()
        return 0
    elif amount <= 0:
        print("Enter an amount greater than 0.")
        print()
        return 0
    else:
        return f"{amount}\n"


def main():

    balance = 0
    is_running = True

    while is_running:
        print("-----------------")
        print(" Banking Program ")
        print("-----------------")
        print()

        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        print()
        choice = input("What would you like to do? (1-4): ")
        print()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Thanks for your patronage. Goodbye.")
            print()
        else:
            print("Please choose a valid option")
            print()


if __name__ == '__main__':
    main()
