from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print formatted current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Get current date
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    # Print formatted future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1
    display_current_datetime()

    # Part 2
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
