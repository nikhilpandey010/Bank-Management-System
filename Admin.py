def admin():
    login=input("Enter username:  ")
    pasw=input("Enter Password: ")
    if login=="Bankmanagement" and pasw=="group10":
    
        while True:
            try:
                print("======Enter======")
                print("   1.    Create")    
                print("   2.    Deposit")
                print("   3.    Withdraw")
                print("   4.    Balance Enquiry")
                print("   5.    All Account List")
                print("   6.    Close An Account")
                print("   7.    Modify An Account")
                print("   8.    Exit\n")
                ch=int(input(":    "))
                if ch==1:
                    import Create
                    Create.create()
                elif ch==2:
                    import Deposit
                    Deposit.deposit()
                elif ch==3:
                    import Withdraw
                    Withdraw.withdraw()
                elif ch==4:
                    import Balance_enq
                    Balance_enq.balance_enq()
                elif ch==5:
                    import Accounts_list
                    Accounts_list.All_account_holder_list()
                elif ch==6:
                    import Close
                    Close.close()
                elif ch==7:
                    import Modify
                    Modify.modify()
                elif ch==8:
                    exit()
                else:
                    print("Enter a valid input!!!!....")
            except ValueError:
                print("!!!Invalid entry...\n Enter only numbers for your choice....\n")
    else:
        print("Incorrect login details..!!\n")


