# Grocery Store Billing System using Python

## 📌 Case Study Title
Grocery Store Billing System

## 👩‍🎓 Student Details
Name: Aarzu Bhatt 
Roll No.: 202501100700001
Branch: ECE 
Section: A  

---

## 📖 Problem Statement
A grocery store wants to calculate the total cost of items purchased by a customer.

Requirements:
- Calculate the total cost of 3 different items.
- Add a 10% discount if the total exceeds $50.
- Display the original total, discount (if applicable), and final payable amount.

---

## 💡 Approach
1. Accept price input for 3 items using `float()` function.
2. Calculate total cost by adding all three prices.
3. Check if total > 50:
   - If true, apply 10% discount.
4. Subtract discount from total.
5. Display:
   - Original Total
   - Discount Applied
   - Final Payable Amount

---

## 🧮 Python Code

```python
# Grocery Store Billing System

item1 = float(input("Enter price of item 1: $"))
item2 = float(input("Enter price of item 2: $"))
item3 = float(input("Enter price of item 3: $"))

total = item1 + item2 + item3
discount = 0

if total > 50:
    discount = total * 0.10

final_amount = total - discount

print("\n--- BILL SUMMARY ---")
print("Original Total: $", round(total, 2))
print("Discount Applied: $", round(discount, 2))
print("Final Payable Amount: $", round(final_amount, 2))
