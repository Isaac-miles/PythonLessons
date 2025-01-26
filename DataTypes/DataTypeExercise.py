print("Welcome to the tip calculator")
bill = float(input("What was the total Bill ?"))
tip = int(input("What % tip would you like to give ? 10 12 15 "))
people = int(input("How many people to split the bill ? "))
bill_with_tip = tip/100 * bill + bill
print(f"Bill with tip = {bill_with_tip}")