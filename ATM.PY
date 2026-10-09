
pin = 1432
balance = 4000
transaction = 0
failed = 0
attempts = 3
depositedamnt = 0
withdrawalamnt = 0

while attempts > 0:
    enteredpin = int(input("Enter the pin:"))

    if pin == enteredpin:
        print("1.check balance\n2.deposit\n3.withdraw\n4.ministatement\n5.exit")
        echoice = int(input("Enter the choice"))

        if echoice == 5:
            print("Thank you")
            break

        elif echoice == 1:  # check balance
            print("Account balance:", balance)

        elif echoice == 2:  # deposit
            damnt = int(input("Enter the amount you want to deposit:"))

            if damnt > 0:
                balance = balance + damnt
                transaction += 1
                print("Account bal:", balance)
                print(f"transaction succesful {transaction} times")
                depositedamnt += damnt
            else:
                failed += 1
                print(f"Transaction failed {failed} times")

        elif echoice == 3:  # withdrawal
            wamnt = int(input("Enter the amount:"))

            if wamnt <= balance and wamnt > 0:
                balance = balance - wamnt
                print("Account bal:", balance)
                transaction += 1
                print("Transaction success", transaction)
                withdrawalamnt += wamnt
            else:
                print("Enter valid amount")
                failed += 1
                print(f"Transaction failed {failed} times")

        elif echoice == 4:  # mini statement
            print("*******MINI STATEMENT*******")
            print("Account Balance:", balance)
            print("Deposited amount:", depositedamnt)
            print("Withdrawal amount:", withdrawalamnt)
            print("Successful transactions:", transaction)
            print("Failed Transactions:", failed)
            print("        *********            ")

        else:
            print("Invalid choice")
            failed += 1

    else:
        print("Invalid PIN")
        failed += 1
        attempts -= 1

if attempts == 0:
    print("Account temporarily locked")