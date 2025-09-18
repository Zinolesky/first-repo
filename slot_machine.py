import random


def spin_row():
    symbols = ['🍒', '🍉', '🔔', '💣', '💯']
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "💣":
            return bet * 10
        elif row[0] == "💯":
            return bet * 20
    return 0


def main():
    profit = 0
    wins = 0
    balance = 1000
    print("************************")
    print("      Slot Machine      ")
    print("************************")
    print()
    print("------------------------")
    print("Symbols: 🍒 🍉 🔔 💣 💯")
    print("------------------------")
    print()
    print("Disclaimer: We don't accept bets in kobo.")
    print()

    while balance > 0:

        print(f"Balance: ₦{balance}")
        print()

        bet = input("Place bet: ")
        print()

        if not bet.isdigit():
            print("Please enter a valid amount.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be above 0.")
            continue

        if bet > balance:
            print("Insufficient funds.")
            continue

        balance -= bet

        row = spin_row()

        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ₦{payout} 🤑!\n")
            balance += payout
            wins += 1
            profit += payout
        else:
            print("Sorry. You lost this round. 🥲\n")

        if input("Play again? (Y/N): ").upper() != "Y":
            break

    print("--------------------")
    print(f"Number of wins: {wins}")
    print(f"Earnings: ₦{profit}")
    print(f"Balance: ₦{balance}")
    print("--------------------")


if __name__ == '__main__':
    main()