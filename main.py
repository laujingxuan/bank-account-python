from BankAccount import BankAccount

def main():
    account = BankAccount()
    print("Welcome to MyMy Bank! What would you like to do?")
    while True:
        action = input('[D]eposit\n[W]ithdraw\n[P]rint statement\n[Q]uit')
        if action == "d" or action == "D":
            amount = input("Please enter the amount to deposit: ")
            #Deposit()
        elif action == "w" or action == "W":
            #Withdraw()
        elif action == "p" or action == "P":
            #PrintStatement()
        elif action == "q" or action == "Q":
            isExit = True
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