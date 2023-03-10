def All_account_holder_list():
    with open("Accounts.txt","r") as f:
        while True:
            buf=f.readline()
            if buf == "":
                break
            d=dict(subString.split(":") for subString in buf.split(","or"\n"))
            for i,j in d.items():
                print(i,"    ",j)
            print("\n")








