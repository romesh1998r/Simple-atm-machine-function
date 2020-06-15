count=0
store_pin=int(1998)
s=""
shutdown = False
Balance=float(100000.00)
while s != store_pin :
    
    s=int(input("Enter the atm pin:"))


    if s != store_pin:

        print("Invalid login in atm.")
        count=count+1
        

    if count == 3:

        print("Too many attempts. The atm machine blocked by your card. ")
        quit
        shutdown=True
        break
       


while(shutdown == False):

    print("Welcome to atm machine.\n")

    w=input("Select the option: 1.View Balance\n 2.Withdraw Money\n 3.Deposit Money\n 4.Quit\n :choose(1,2,3,4,5):")


    if w == "1":
        print("Balance:",Balance)
        break

    if w == "2":
        j=float(input("Enter the withdrawal money:"))

        Balance=Balance-j
        print("New balance:",Balance)
        break

    elif w == "3":

        h=float(input("Enter the deposit money:"))

        Balance=Balance+h
        print("New balance:",Balance)

        break


    elif w == "4":

        print("Thank for banking with us.")
        quit
        shutdown = True
        break

    

           


        
