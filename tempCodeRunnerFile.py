
item1 = float(input("Enter price of Item 1: $"))
item2 = float(input("Enter price of Item 2: $"))
item3 = float(input("Enter price of Item 3: $"))

# Calculate  cost
total = item1 + item2 + item3

discount = 0


if total > 50:
    discount = total * 0.10   # 10% discount

# Calculate final payable amount
final_amount = total - discount

# Display results
print("\n----- Billing Summary -----")
print(f"Original Total: ${total:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Payable Amount: ${final_amount:.2f}")
