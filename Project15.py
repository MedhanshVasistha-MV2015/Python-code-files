def calculate_change(bill, paid):
    return paid - bill
bill = int(input("Enter the total bill amount: "))
paid = int(input("Enter the amount paid: "))
change = calculate_change(bill, paid)
print("The shopkeeper should give: ", change)