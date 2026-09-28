# Taking information
print("\n" + "-" * 50)
product_1 = input("Enter your first product: ")
quantity_1 = int(input("Enter product quantity: "))
price_1 = float(input("Enter product unit price: "))

print("\n" + "-" * 50)
product_2 = input("Enter your second product: ")
quantity_2 = int(input("Enter product quantity: "))
price_2 = float(input("Enter product unit price: "))

print("\n" + "-" * 50)
print(f"{'Additional Charges':^50}")
print("-" * 50)

delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage: "))

# Calculations
line_total_1 = quantity_1 * price_1
line_total_2 = quantity_2 * price_2
subtotal = line_total_1 + line_total_2  # <-- Eklenen satır

# Tax
tax_amount = subtotal * (tax_percentage / 100)

# Final total
final_total = subtotal + tax_amount + delivery_fee

# Outputs
print("\n" + "-" * 50)
print(f"{'ORDER SUMMARY':^50}")
print("-" * 50)
print(f"{product_1:<20} {quantity_1:>3} x {price_1:>7.2f} = {line_total_1:>10.2f}")  # <-- Tırnak kapatıldı
print(f"{product_2:<20} {quantity_2:>3} x {price_2:>7.2f} = {line_total_2:>10.2f}")  # <-- Tırnak kapatıldı
print("-" * 50)
print(f"{'Subtotal:':<29} {subtotal:>10.2f}")
print(f"{f'Tax ({tax_percentage:.0f}%):':<29} {tax_amount:>10.2f}")
print(f"{'Delivery Fee:':<29} {delivery_fee:>10.2f}")
print("-" * 50)
print(f"{'FINAL TOTAL:':<29} {final_total:>10.2f}")
print("-" * 50)
