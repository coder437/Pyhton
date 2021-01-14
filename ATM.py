class ATM:
    def __init__(self):
        def check_balance(self):
            print(balance)

        def withdraw_balance():
            withdrawl_amount = int(input("please enter the cash you want to withdraw"))
            if withdrawl_amount <= balance:
                print("cash left is",balance)
            else:
                print("please enter a valid amount or add some cash to account")
        
        def add_balance():
            added_amount = int(input("lease enter the cash you want to add"))
            if added_amount==0:
                print("please add a amount")
            else:
                print("your added"+added_amount)

        def exit():
            print("thanks for submision")

def main():
    balance = 0
    cardNumber = 12345
    card_number = input("please enter card number")
    pin_number = input("please enter pin")
    if card_number == 12345:
        print("please select an activity")
        print("1. check balance")
        print("2. withdraw amount")
        print("3. add amount")
        print("4. exit")
        activity = int(input("please enter activity number"))
        if activity == 1:
            check_balance()
        elif activity == 2:
            withdraw_balance()
        elif activity == 3:
            add_balance()
        elif activity == 4:
            exit()
        else:
            print("please enter a valid number")
    else:
        print("card number incorrect")

main()     
