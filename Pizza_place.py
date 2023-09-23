print ("welcome to python pizza deliveries!")
areYouSure = 0
while areYouSure != "N":
    size = input("what pizza size do you want? S, M, or L: ").upper()
    if size == "S":
        print(f"That's $15")
    elif size == "M":
        print(f"That's $20")
    elif size == "L":
        print(f"That's $25")
    addPepperoni = input("Do you want pepperoni? Y or N: ").upper()
    if size == "S" and addPepperoni == "Y":
        print(f"That's an extra $2")
    elif size == "M" or size == "L" and addPepperoni == "Y":
        print(f"That's an extra $3")
    else:
        print (f"No pepperoni for you then")
    extraCheese = input("Do you want extra cheese? Y or N: ").upper()
    if extraCheese == "Y":
        print("That's an extra $1")
    else:
        print (f"No extra cheese for you then")
    areYouSure = input("Do you want to make any changes to your choices? Y or N: ").upper()
    if areYouSure == "Y":
        print("Okay let's do this again")

if size == "S" and addPepperoni == "Y" and extraCheese == "N":
    print(f"your final bill is $17")
elif size == "M" and  addPepperoni == "Y" and extraCheese == "N":
    print(f"your final bill is $23")
elif size == "L" and addPepperoni == "Y" and extraCheese == "N":
    print(f"your final bill is $28")
elif size == "S" and addPepperoni == "Y" and extraCheese == "Y":
    print(f"your final bill is $18")
elif size == "M" and  addPepperoni == "Y" and extraCheese == "Y":
    print(f"your final bill is $24")
elif size == "L" and addPepperoni == "Y" and extraCheese == "Y":
    print(f"your final bill is $29")
elif size == "S" and addPepperoni == "N" and extraCheese == "Y":
    print(f"your final bill is $16")
elif size == "M" and  addPepperoni == "N" and extraCheese == "Y":
    print(f"your final bill is $21")
elif size == "L" and addPepperoni == "N" and extraCheese == "Y":
    print(f"your final bill is $26")
