
def close():
    i=0
    flag=0
    number=int(input("Enter the card number: "))
    Cvv=int(input("Enter CVV: "))
    with open("Accounts.txt","r") as f:
        with open("temp.txt","w") as ft:
            while True:
                i=i+1
                buf=f.readline()
                if buf == "":
                    break
                d=dict(subString.split(":") for subString in buf.split(","or"\n"))
                if int(d["Card number"])!=number and int(d["CVV"])!=Cvv :
                    ft.write("Card number:")
                    ft.write(str(d["Card number"]))
                    ft.write(",Name on the Card:")
                    ft.write(str(d["Name on the Card"]))
                    ft.write(",CVV:")
                    ft.write(str(d["CVV"]))
                    ft.write(",Amount:")
                    ft.write(str(d["Amount"]))
                else:
                    flag=1
    with open("temp.txt","r") as f:
        with open("Accounts.txt","w") as ft:
            while True:
                buf=f.readline()
                if buf == "":
                    break
                d=dict(subString.split(":") for subString in buf.split(","or"\n"))
                ft.write("Card number:")
                ft.write(str(d["Card number"]))
                ft.write(",Name on the Card:")
                ft.write(str(d["Name on the Card"]))
                ft.write(",CVV:")
                ft.write(str(d["CVV"]))
                ft.write(",Amount:")
                ft.write(str(d["Amount"]))
    if flag==0:
        print("Given Card number does not exist...\n")
    if flag==1:
        print("Account clossed Successfully...\n")







