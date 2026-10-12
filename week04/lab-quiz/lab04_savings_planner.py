def main():
    while True:
        balance = float(input("Enter starting balance: "))
        if balance >= 0:
            break
        print("Error: Starting balance cannot be negative. Please try again.")

    while True:
        deposit = float(input("Enter monthly deposit: "))
        if deposit > 0:
            break
        print("Error: Monthly deposit must be positive. Please try again.")

    while True:
        rate = float(input("Enter monthly interest rate (%): "))
        if rate >= 0:
            break
        print("Error: Interest rate cannot be negative. Please try again.")

    while True:
        goal = float(input("Enter savings goal: "))
        if goal > 0:
            break
        print("Error: Savings goal must be positive. Please try again.")

    if balance >= goal:
        print("\nYour starting balance already meets the goal!")
        return  # End program early, no table printed
    print(f"\n{'Month':<5} | {'Interest':<12} | {'New Balance'}")
    print("-" * 35)

    total_interest = 0.0
    months = 0
    goal_reached = False

    for month in range(1, 61):  # Maximum 60 months loop
        monthly_interest = balance * (rate / 100)
        balance += monthly_interest
        balance += deposit
        
        total_interest += monthly_interest
        months += 1
        
        print(f"{month:<5} | {monthly_interest:<12.2f} | {balance:.2f}")
        
        if balance >= goal:
            goal_reached = True
            break  # Stop the loop early

    print("-" * 35)
    if goal_reached:
        print(f"Goal reached in {months} months.")
    else:
        print("Goal not reached (stopped after 60 months).")
        
    print(f"Final Balance: {balance:.2f}")
    print(f"Total Interest Earned: {total_interest:.2f}")

if __name__ == "__main__":
    main()