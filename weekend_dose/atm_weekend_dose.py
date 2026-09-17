
balance = 1000
while True:
    banking_option = """

            Welcome

            1 Deposit
            2 Withdraw
            3 Check balance
            0 Thank you for banking with us

            select option: 
        """
    banking_option_list =int (input(banking_option))
    match banking_option_list:

            case 1: 
                while True:
                    print ("Deposit")
                    deposit_option = """
                        0 Back to banking option


                        select option:
                    """

                    deposit_option_list =int (input(deposit_option))
                    match deposit_option_list:

                        case 0: 
                            print ("Back to banking option")
                            break
                        case _: 
                            print ("Invalid input")

                
            case 2: 
                while True:
                    print("Withdraw")
                    Withdraw_option = """
                        1 Enter amount
                        0 Back 
                        select option:
                        
                    """
                    withdraw_option_list =int (input(Withdraw_option))
                    match withdraw_option_list:

                        case 1: 
                            amount = int(input('Enter amount: '))
                            if amount > balance:
                                print ("insufficient fund")
                            else:
                                print ("withdrawal successful")

                        case 0:
                            print ("Back to withdraw option")
                            break

                        case _: print ("Invalid input")
            case 3: 
                while True:
                    print ("Check balance")
                    check_balance_option = """

                        Account balance #{balance}


                        0 back to banking option
                    """
                    check_balance_option_list =int (input( check_balance_option))
                    match check_balance_option_list:

                        case 0: 
                            print ("Back to banking option")
                            break

                        case _: 
                            print ("Invalid input")
            case 0: 
                print ("Thank you for banking with us")
                break

            case _: 
                print ("invalid input")
            
