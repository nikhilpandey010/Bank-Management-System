
def balance_enq():
    number=int(input("Enter the card number: "))
    Cvv=int(input("Enter CVV: "))
    with open("Accounts.txt","r") as f:
        flag=0
        while True:
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))
            
            if int(d["Card number"])==number and int(d["CVV"])==Cvv:
                flag=1
                for i,j in d.items():
                    print(i,"       :",j)
                ch=input("Do you need to save (y/n):")
                if(ch=='y'):
                    filename=input("Save as: ")
                    with open(filename,"w")as fs:
                        fs.write(str(d))
                    print("Saved successfully")
    if flag==0:
        print("Given Card number or cvv does not exist....\n")
