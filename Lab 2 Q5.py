#student ID: 1201201564
#student Name: Goh Jia Chen

pliter = 0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")

amount = float(input("Enter amount of litres : "))

total = pliter * amount

print("Price per liter  = RM {:.2f}".format(pliter))
print("Number of liters = {}".format(amount))
print("Total = RM {:.2f}".format(total))