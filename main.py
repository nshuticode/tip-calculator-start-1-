print("Welcome to the tip calculator! \n")

total_bill = input("What was the total bill? $")
tip = input("How much tip would like to give? 10, 12, or 15 ?  $")
people_to_split_the_bill = input("How many people to split the bill? ")
total_bill_as_float = float(total_bill)
tip_as_int = int(tip)
people_to_split_the_bill_as_int = int(people_to_split_the_bill)
tip_percentage = (tip_as_int * total_bill_as_float) / 100
general_total_bill = total_bill_as_float + tip_percentage 
splited_bill = general_total_bill / people_to_split_the_bill_as_int
bill_per_person = round(splited_bill, 2)
bill_per_person = "{:.2f}".format(splited_bill)
print(f"Each person should pay:$ {bill_per_person} ")
