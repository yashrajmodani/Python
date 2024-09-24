account_balance = 50000

remaining_bal = 0
i = 1

while i >= 1:
    withdraw_amt = int(input("Enter the amount you want to withdraw = "))

    if withdraw_amt <= account_balance:
        if withdraw_amt % 10 == 0:
            account_balance = account_balance - withdraw_amt
            remaining_bal = account_balance
            print(remaining_bal)
            i = i + 1
        else:
            print("Amount must be a multiple of 10")
    else:
        print("Insufficient Balance")
