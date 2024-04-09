# assignment: programming assignment 3
# author: Yazmyn Sims
# date: 11/5/2022
# file: convert.py is a program that gets unser input for temperature (in Fahrenheit), weight (Pounds), or distance(Miles) and converts it into a different unit of measurement (Celsius, km, and kg)
# input: user will choose between Fahrenehit, Pounds, and Miles, then the user will enter a number to convert the amount into a different unit
# output: the program will output the result of the conversion and ask if the user would like to repeat the process or end the program

#defined variable
order = 'F'
again = 'y'

# defined functions
def format(num, precision = 2): 
    num = round(num, precision)

    num = str(num)
    if num [-1] == '0':
        num = num[:-2]
    return(num)

def isfloat(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
    
def fahrenheit_Celsius():
        Ftemp = input("Please enter a temperature in Fahrenheit:\n")
        if isfloat(Ftemp):
            Ftemp = float(Ftemp)
            Ctemp = (Ftemp - 32) * 5 / 9
            format(Ctemp, 2)
            print(f"{format(Ftemp)} Fahrenheit corresponds to {format(Ctemp)} Celsius.")
        else:
            while isfloat (Ftemp) == False:
                print("You did not enter a number.")
                Ftemp = input("Please enter a temperature in Fahrenheit:\n")
                if isfloat(Ftemp):
                    Ftemp = float(Ftemp)
                    Ctemp = (Ftemp - 32) * 5 / 9
                    format(Ctemp, 2)
                    print(f"{format(Ftemp)} Fahrenheit corresponds to {format(Ctemp)} Celsius.")
            
def miles_km():
    miles = input("Please enter miles:\n")
    if isfloat(miles):
        miles = float(miles)
        km = miles * 1.609344
        format(km, 2)
        print(f"{format(miles)} miles corresponds to {format(km)} km.")
    else:
        while isfloat(miles) == False:
            print("You did not enter a number.")
            miles = input("Please enter miles:\n")
            if isfloat(miles):
                miles = float(miles)
                km = miles * 1.609344
                format(km, 2)
                print(f"{format(miles)} miles corresponds to {format(km)} km.")

def pounds_kg():
    pounds = input("Please enter pounds:\n")
    if isfloat(pounds):
        pounds = float(pounds)
        kg = pounds * 0.45359237
        format(kg,2)
        print(f"{format(pounds)} pounds corresponds to {format(kg)} kg.")
    else:
        while isfloat(pounds) == False:
            print("You did not enter a number.")
            pounds = input("Please enter pounds:\n")
            if isfloat(pounds):
                pounds = float(pounds)
                kg = pounds * 0.45359237
                format(kg,2)
                print(f"{format(pounds)} pounds corresponds to {format(kg)} kg.")
        
#Title    
print("Welcome to the SI Unit Converter!")



# Repeat until input is valid
while (order != 'F' or order != 'f' or order != 'M' or order != 'm' or order != 'P' or order != 'p'):
    
    #Options
    order = input("Please choose one of the following conversions:\n" \
        "Fahrenheit to Celsius - F\n" \
        "Pounds to kg - P\n" \
        "Miles to km - M\n")

    #Option F
    if (order == 'F' or order == 'f'):
        fahrenheit_Celsius()
    
        #Continue 
        again = input("Do you want to continue? [Y/N]:\n")
        if (again == 'Y' or again == 'y'):
            continue
        else:
            print("Goodbye!")
            break

    #Option P
    elif (order == 'P' or order == 'p'):
        pounds_kg()
    
        #Continue
        again = input("Do you want to continue? [Y/N]:\n")
        if (again == 'Y' or again == 'y'):
            continue
        else:
            print("Goodbye!")
            break

    #Option M
    elif (order == 'M' or order == 'm'):
        miles_km()
    
        #Continue 
        again = input("Do you want to continue? [Y/N]:\n")
        if (again == 'Y' or again == 'y'):
            continue
        else:
            print("Goodbye!")
            break
    #bad input
    elif(order != 'F' or order != 'f' or order != 'M' or order != 'm' or order != 'P' or order != 'p'):
        print ("You did not choose correctly.")
