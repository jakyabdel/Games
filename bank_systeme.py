
print("=====================================")

customerNames = ['John Smith']
customerPins = ['123']
customerBalances = [0]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 1
i = 0


while True:
   
    print("=====================================")
    print(" ----Welcome to Banking System----   ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")
   
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        
        NOC = eval(input("Number of Customers : "))
 
        i = i + NOC
        # The if condition will restrict the number of new account to 5.
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - NOC
        else:
            # The while loop will run according to the no:of customers.
            while counter_1 <= i:
                # These few lines will take information from customer and then append them to the list.
                name = input("Input Fullname : ")
                customerNames.append(name)
                pin = str(input("Please input a pin of your choice : "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Please input a value to deposit to start an account : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("$")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
                
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
       
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("$\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Input value to Withdraw : "))
                        if withdrawal > balance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("$\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("$\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("$\n\n")
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("$")
                        balance = (customerBalances[k])
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("$\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("$")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
