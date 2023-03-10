def check():
    number2=int(input("Enter the reciever Card number: "))
    Name2=input("Enter name on the card: ")
    with open("Accounts.txt","r") as f:
        flag=0
        while True:
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))

            if int(d["Card number"])==number2 and d["Name on the Card"]==Name2:
                return(d)

    
def send(d2,amt):
    p=0
    with open("Accounts.txt","r") as f:
        flag=0
        while True:
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))

            if int(d["Card number"])==int(d2["Card number"]) and int(d["CVV"])==int(d2["CVV"]):
                flag=1
                d["Amount"]=float(d["Amount"])+amt
                print("Name on card: ",d["Name on the Card"])
                print("Amount         : ",d["Amount"])
                break
            else:
                p=f.tell()
    f.close()
    if flag==1:
        with open("Accounts.txt","r+") as f:
            f.seek(p)
        
            f.write("Card number:")
            f.write(str(d["Card number"]))
            f.write(",Name on the Card:")
            f.write(str(d["Name on the Card"]))
            f.write(",CVV:")
            f.write(str(d["CVV"]))
            f.write(",Amount:")
            f.write(str(d["Amount"]))
def transact(d2,amt):
    p=0
    with open("Accounts.txt","r") as f:
        flag=0
        while True:
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))

            if int(d["Card number"])==int(d2["Card number"]) and int(d["CVV"])==int(d2["CVV"]):
                flag=1
                d["Amount"]=float(d["Amount"])-amt
                print("Name on card: ",d["Name on the Card"])
                print("Amount         : ",d["Amount"])
            else:
                p=f.tell()
                    
    if flag==1:
        with open("Accounts.txt","r+") as f:
            f.seek(p)
            
            f.write("Card number:")
            f.write(str(d["Card number"]))
            f.write(",Name on the Card:")
            f.write(str(d["Name on the Card"]))
            f.write(",CVV:")
            f.write(str(d["CVV"]))
            f.write(",Amount:")
            f.write(str(d["Amount"]))
            f.write("\n")

