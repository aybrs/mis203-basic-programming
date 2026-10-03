total_customers = 0
total_revenue = 0.0
free_tickets = 0

while True:
    print("-" * 24 + "Welcome!!!" + "-" * 24)
    name = input("Enter your name please:(q to quit.) ").strip()
    if name.lower() == 'q':
        break

    #taking age input and control the input

    age_input = input("Enter your age please:(q to quit.) ").strip()
    if age_input.lower() == 'q':
        break

    try:
        age = int(age_input)
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age. Please enter a valid age.")
        continue

    #taking ticket day 
    day = input("Day (weekend or weekday): ").strip().lower()
    if day not in ["weekend" , "weekday"]:
        print("Invalid input. Please enter 'weekend' or 'weekday'.")
        continue

    #stdudent control
    student = input("Are you a student? Please enter yes or no: ").strip().lower()
    if student not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

    #prices
    base_price = 200.0 if day == "weekday" else 250.0

    #discounts
    if age < 6:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        category = "Child"
    elif student == "yes" and age <= 25:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.00
        category = "Standard"

    #final price calculation
    final_price = base_price * (1.0 - discount)

    #print the result
    print("\n" + "-" * 48)
    print("\n")
    print(f"{name}: {final_price:.2f} TRY ({category})")

    #update total customers and revenue
    total_customers += 1
    total_revenue += final_price
    if category == "Free":
        free_tickets += 1

#Summary screen
if total_customers == 0:
    print("No tickets sold.")
else:
    average_price = total_revenue / total_customers
    print("\n" + "=" * 48)
    print("Summary")
    print("=" * 48 + "\n")
    print(f"Total customers: {total_customers}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")