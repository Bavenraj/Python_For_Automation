import pyinputplus as pyip

print("\nEXAMPLE 1")
result = pyip.inputInt("Enter the number of shopping bags you will need for your items:", min=0)
print("\nYou will use", result, "store bags.")

print("\nEXAMPLE 2")
result = pyip.inputMenu(["red", "blue", "green"], lettered=True, numbered=False)
print("\nYou have chosen a", result, "marker.")

