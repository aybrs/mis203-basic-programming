NUM_DAYS = 7


def main():
    print("=== Weekly Sales Monitor ===")

    # Get a valid daily sales target
    while True:
        try:
            target = float(input("Enter daily sales target: $"))
            if target < 0:
                print("Target cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    # Initialize tracking variables
    total_sales = 0.0
    days_meeting_target = 0
    highest_sale = -1.0
    highest_day = 0

    day = 1
    while day <= NUM_DAYS:
        try:
            val_input = input(f"Enter sales for Day {day}: $")
            sale = float(val_input)

            # Re-prompt when a sale is negative
            if sale < 0:
                print("Sales cannot be negative. Please enter a valid amount.")
                continue

            # Accumulate totals
            total_sales += sale

            # Check if target is met (includes days equal to target)
            if sale >= target:
                days_meeting_target += 1

            # Stretch task: track highest sale without lists
            if sale > highest_sale:
                highest_sale = sale
                highest_day = day

            # Advance to next day only after a valid entry
            day += 1

        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    # Calculate average
    average_sales = total_sales / NUM_DAYS

    # Display results
    print("\n--- Weekly Summary ---")
    print(f"Weekly Total Sales:      ${total_sales:,.2f}")
    print(f"Average Daily Sales:      ${average_sales:,.2f}")
    print(
        f"Days Target Met:          {days_meeting_target} / {NUM_DAYS} days"
    )
    if highest_day > 0:
        print(f"Highest Sale:             ${highest_sale:,.2f} (Day {highest_day})")


if __name__ == "__main__":
    main()