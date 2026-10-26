def check_valid_input(value):
    """
    Checks if the given input is a valid positive number or zero.
    The threshold boundary is 0.
    """
    return value >= 0

def sub_total(quantity, price_per_item):
    """
    Calculate the subtotal for a given quantity of items at a specified price per item.

    Parameters:
    quantity (int): The number of items being purchased.
    price_per_item (float): The cost of a single item.

    Returns:
    float: The subtotal for the items.
    """
    return quantity * price_per_item

def discount_rate(subtotal, discount_threshold):
    """
    Calculate the discount amount based on the subtotal.
    
    Parameters:
    subtotal (float): The subtotal for the items.
    discount_threshold (float): The threshold for the discount.

    Returns:
    float: The discount amount.
    """
    if subtotal >= discount_threshold:
        return subtotal * 0.10  # 10% discount
    return 0.0  # No discount

def total(subtotal, discount, shipping_fee):
    """
    Calculate the final total after applying discount and adding shipping fee.

    Parameters:
    subtotal (float): The subtotal for the items.
    discount (float): The discount amount to be subtracted from the subtotal.
    shipping_fee (float): The shipping fee to be added to the total.

    Returns:
    float: The final total after applying discount and adding shipping fee.
    """
    return subtotal - discount + shipping_fee

"""
I'm taking basic informations about the goods from the user,
such as name, price, and quantity. The program will then calculate 
the total price for the goods, apply any applicable discounts, and add 
shipping fees to provide a final total cost.
Also, the program checks for valid inputs.
"""


goods_name = input("Enter your goods name: ")

goods_price = float(input("Enter your goods price: "))
while not check_valid_input(goods_price):
    print("Error: Price cannot be negative!")
    goods_price = float(input("Enter your goods price again: "))

goods_quantity = int(input("Enter your goods quantity: "))
while not check_valid_input(goods_quantity):
    print("Error: Quantity cannot be negative!")
    goods_quantity = int(input("Enter your goods quantity again: "))

discount_threshold = float(input("Enter discount threshold (enter 99999 if no discount): "))
while not check_valid_input(discount_threshold):
    print("Error: Threshold cannot be negative!")
    discount_threshold = float(input("Enter discount threshold again: "))

shipping_fee = float(input("Enter your shipping fee: "))
while not check_valid_input(shipping_fee):
    print("Error: Shipping fee cannot be negative!")
    shipping_fee = float(input("Enter your shipping fee again: "))


# Calculate the subtotal, discount, and final total
current_subtotal = sub_total(goods_quantity, goods_price)
current_discount = discount_rate(current_subtotal, discount_threshold)
final_cost = total(current_subtotal, current_discount, shipping_fee)

# Print the final results
print(f"\nProduct: {goods_name}")
print(f"Total Price: ${final_cost}")