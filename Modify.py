
def modify():
    i=0
    p=0
    number=int(input("Enter the card number: "))
    Cvv=int(input("Enter CVV: "))
    with open("Accounts.txt","r") as f:
        flag=0
        while True:
            i=i+1
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))

            if int(d["Card number"])==number and int(d["CVV"])==Cvv:
                
                flag=1
                print(d)
                break
            else:
                p=f.tell()

    if flag==1:
        with open("Accounts.txt","r+") as f:
            f.seek(p)
            f.write("Card number:")
            f.write(str(d["Card number"]))
            f.write(",Name on the Card:")
            name=input("Enter name : ")
            f.write(name)
            f.write(",CVV:")
            f.write(str(d["CVV"]))
            f.write(",Amount:")
            f.write(str(d["Amount"]))
            
    else:
        print("Given card number or CVV does not Exist...\n")







