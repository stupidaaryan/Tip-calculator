print("Welcome to Tip Calculator!")
total_bill = float(input("What is the Total Bill? $"))
tip = int(input("What percentage of tip You would like to give? 12, 10 or 15? \n"))
people = int(input("how many people to split the bill?"))
real_tip = total_bill * (tip/ 100)

splited_bill = ((total_bill + real_tip)/ people)

print(f"Each person should pay {splited_bill}")
