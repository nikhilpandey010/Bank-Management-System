def User():
    number1=int(input("Enter the card number: "))
    Cvv1=int(input("Enter Cvv: "))
    Name1=input("Enter the name on the card: ")
    with open("Accounts.txt","r") as f:
        flag=0
        while True:
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))

            if int(d["Card number"])==number1 and int(d["CVV"])==Cvv1 and d["Name on the Card"]==Name1:
                flag=1
                break
        while flag==1:
                print("======Enter======")
                print("   1.    Enquiry")    
                print("   2.    Transact")
                print("   3.    Exit")
                ch=int(input(" : "))
                if ch==1:
                    print(d)
                elif ch==2:
                    import Reciever
                    d2=dict()
                    d2=Reciever.check()
                    if d2!=None:
                        amt=float(input("Enter amount to be transacted: "))
                        if float(d["Amount"])<amt:
                            print("Insufficient Balance...\n")
                        else:
                            d["Amount"]=float(d["Amount"])-amt
                            Reciever.transact(d,amt)
                            Reciever.send(d2,amt)
                            print("YOUR TRANSACTION IS SUCCESSFUL...")
                    else:
                        print("Given card number does not exist!!!\n")
                elif ch==3:
                    exit(0)
                else:
                    print("Enter a valid input!!!!....")
        if flag==0:
            print("Given card number does not exist!!!\n")



