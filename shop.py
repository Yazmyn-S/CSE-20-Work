# assignment: programming assignment 2
# author: Yazmyn Sims
# date: 10/16/2022
# file: shop.py implements a vending machine
# input: strings and numbers (integers)
# output: interactive messages (strings)

#set up variables
water = int(199)
OJ = int(215)
tea = int(249)
order = 1


print("Vending Machine")

#repeat prompt until quit
while (order != '4'):
    
    #Display options and get input
    order = input("Please enter what product you want to buy[1-3] or select quit[4]:\n" \
    "1. A bottle of water - $1.99 \n" \
    "2. A bottle of orange juice - $2.15\n" \
    "3. A bottle of iced tea - $2.49\n" \
    "4. Quit\n")

    #Order 1
    if (order == '1'):
        #Get deposite money  
        deposite = int(input("Please deposit money (in cents): \n"))
        #check to see if we got enough 
        while deposite < water:
            deposite = deposite + int(input("Please deposit money (in cents): \n"))
            
        #Calculate Change            
        print("You bought a bottle of water.")
        change = (deposite - water)
        if (change != 0):
            print("Your change is:")

        dollars = change // 100   
        change = change % 100     

        quarters = change // 25 
        change = change % 25

        dimes = change // 10
        change = change % 10

        nickels = change // 5
        change = change % 5

        cents = change
        
        if(quarters != 0):
            print(f"Quarters - {quarters}")
        if(dimes !=0):
            print(f"Dimes - {dimes}")
        if(nickels !=0):
            print(f"Nickels - {nickels}")
        if(cents != 0):
            print(f"Cents - {cents}")
#Order 2
    elif (order == '2'):
        #Get deposite money  
        deposite = int(input("Please deposit money (in cents): \n"))
        #check to see if we got enough 
        while deposite < OJ:
            deposite = deposite + int(input("Please deposit money (in cents): \n"))
            
        #Calculate Change            
        print("You bought a bottle of orange juice.")
        change = (deposite - OJ)
        if (change != 0):
            print("Your change is:")

        dollars = change // 100   
        change = change % 100     

        quarters = change // 25 
        change = change % 25

        dimes = change // 10
        change = change % 10

        nickels = change // 5
        change = change % 5

        cents = change
        
        if(quarters != 0):
            print(f"Quarters - {quarters}")
        if(dimes !=0):
            print(f"Dimes - {dimes}")
        if(nickels !=0):
            print(f"Nickels - {nickels}")
        if(cents != 0):
            print(f"Cents - {cents}")

#Order 3
    elif (order == '3'):
        #Get deposite money  
        deposite = int(input("Please deposit money (in cents): \n"))
        #check to see if we got enough 
        while deposite < tea:
            deposite = deposite + int(input("Please deposit money (in cents): \n"))
            
        #Calculate Change            
        print("You bought a bottle of iced tea.")
        change = (deposite - tea)
        if (change != 0):
            print("Your change is:")

        dollars = change // 100   
        change = change % 100     

        quarters = change // 25 
        change = change % 25

        dimes = change // 10
        change = change % 10

        nickels = change // 5
        change = change % 5

        cents = change
        
        if(quarters != 0):
            print(f"Quarters - {quarters}")
        if(dimes !=0):
            print(f"Dimes - {dimes}")
        if(nickels !=0):
            print(f"Nickels - {nickels}")
        if(cents != 0):
            print(f"Cents - {cents}")

    #Bad Order ERROR HERE WITH 4
    elif(order != '4'):
        print ("You made the wrong choice!")
        
print("Goodbye!")
