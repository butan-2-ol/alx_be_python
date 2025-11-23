from datetime import datetime, timedelta


def display_current_datetime():
    # Part 1
    current_date = datetime.now()  # save inside current_date
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
    return current_date   # return it so the next function can use it


def calculate_future_date(current_date, days_to_add):
    # Part 2
    future_date = current_date + timedelta(days=days_to_add)  # save inside future_date
    formatted = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted)
    return future_date


def main():
    # Display current date/time
    current_date = display_current_datetime()

    # Ask user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Calculate and print future date
    calculate_future_date(current_date, days)


if __name__ == "__main__":
    main()
