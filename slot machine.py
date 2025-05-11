# py slot machine
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols)for _ in range(3)]




def print_row():
    print("********************************")
    print(" | ".join(row))
    print("********************************")


def get_payout(row,bet):
    if row[0]== row[1] == row[2]:
        if row[0]=='🍒':
            return bet*10
        elif row[0]=='🍉':
            return bet*1.7
        elif row[0]=='🍋':
            return bet*2.5
        elif row[0]=='🔔':
            return bet*13
        elif row[0]=='⭐':
            return bet*100
    return 0
    


def main():
    balance = 100

    print("--------------------------------")
    print("Welcome to the slot machine")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("--------------------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
         

        row= spin_row()
        print("Spinning...\n")
        print(row)


        payout=get_payout(row,bet)
        if payout>0:
            print(f"You won ${payout}")
        else:
            print("You didn't win anything sorry...")
        
        balance += payout



if __name__ == "__main__":
    main()
# this multiples the total amount in balance not the bet idk why future me i trust you will slove this ps 22:32 2025/02/21