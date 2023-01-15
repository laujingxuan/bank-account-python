from BankAccount import BankAccount

def main():
    account = BankAccount()
    print("Welcome to MyMy Bank! What would you like to do?")
    while True:
        action = input('[D]eposit\n[W]ithdraw\n[P]rint statement\n[Q]uit\n')
        if action == "d" or action == "D":
            #deposit
            amount = input("Please enter the amount to deposit: ")
            while not isDigit(amount) or not account.deposit(int(amount)):
                amount = input("Invalid amount. Please enter again: ")
            print("Thank you. $%.2f has been deposited to your account." %int(amount))
        elif action == "w" or action == "W":
            #withdraw
            if account.balance == 0:
                print("Account balance is 0. Unable to withdraw. Please select other action")
                continue
            amount = input("Please enter the amount to withdraw: ")
            while not isDigit(amount) or not account.withdraw(int(amount)):
                amount = input("Invalid amount. Please enter again: ")
            print("Thank you. $%.2f has been withdrawn." %int(amount))
        elif action == "p" or action == "P":
            #print statement
            account.printStatement()
        elif action == "q" or action == "Q":
            #quit
            break
        else:
            print("Invalid action entered. Please try again.")
            continue
        print("Is there anything else you'd like to do?")
    print("Thank you for banking with MyMy Bank.\nHave a nice day!")

def isDigit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()