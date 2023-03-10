
from random import randint

#function to generate a random number taking in number of digits for said number as argument
def digit_random(n):     
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#Function for creating a bank account, consisting of Name,card number,cvv and initial deposit   
def create():
    with open("Accounts.txt","a")as file:        
        Cardnumber=digit_random(10)
        CVV=digit_random(3)
        Name_on_the_Card=input("Enter customer name: ")              
        print("Card Number is ",Cardnumber)
        print("CVV is ",CVV)
        while True:
            Amount=float(input("Enter amount: "))
            if Amount<5000:
                print("Please Deposit an Amount not less than 5000!!!")
            else:
                print("Initial Deposit of INR",Amount," has been made in your account.")
                break
            
#Writing of card details to file designated for the storage of all accounts   
        file.write("Card number:")
        file.write(str(Cardnumber))
        file.write(",Name on the Card:")
        file.write(Name_on_the_Card)
        file.write(",CVV:")
        file.write(str(CVV))
        file.write(",Amount:")
        file.write(str(Amount))
        file.write("\n")
        print("Your Account Has Been Created Successfully\n")
            

