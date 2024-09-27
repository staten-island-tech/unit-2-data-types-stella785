bill_amount = float(input("Enter the total bill amount: $"))

service = input("How was the service?")

if service == "bad":
    tip_perentage = 0
elif service == "okay":
    tip_percentage = 15
elif service == "good":
    tip_percentage = 20
elif service =="great":
    tip_percentage = 25

total_amount = bill_amount + tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")