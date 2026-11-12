from datetime import datetime, date

print("=" * 45)
print("       INDIAN RAILWAY TICKET BOOKING")
print("=" * 45)

# Available routes and seats
availability = {
    "Mumbai-Delhi": 3,
    "Delhi-Bangalore": 12
}

# Base ticket prices
prices = {
    "Mumbai-Delhi": 1200,
    "Delhi-Bangalore": 1500
}

# Get passenger details
source = input("Enter source city: ").strip().title()
destination = input("Enter destination city: ").strip().title()

travel_date = input("Enter travel date (YYYY-MM-DD): ")

age = int(input("Enter passenger age: "))

# Create route name
route = source + "-" + destination

print("\nChecking ticket availability...")

# Check route availability
if route in availability:

    seats = availability[route]
    base_price = prices[route]

    print("Route available!")

    # Calculate age discount
    discount = 0

    if age >= 60:
        discount = base_price * 0.40
        passenger_type = "Senior citizen"

    elif age < 12:
        discount = base_price * 0.50
        passenger_type = "Child"

    else:
        passenger_type = "Adult"

    # Calculate weekend surcharge
    date_object = datetime.strptime(
        travel_date, "%Y-%m-%d"
    ).date()

    weekend_charge = 0

    if date_object.weekday() == 5 or date_object.weekday() == 6:
        weekend_charge = (base_price - discount) * 0.10

    # Calculate Tatkal charge
    today = date.today()
    days_left = (date_object - today).days

    tatkal_charge = 0

    if days_left >= 0 and days_left <= 2:
        tatkal_charge = base_price * 0.30

    # Calculate total price
    total = (
        base_price
        - discount
        + weekend_charge
        + tatkal_charge
    )

    # Seat availability warning
    print("\nChecking seats...")

    if seats < 5:
        print("Only", seats, "seats left! Book fast!")

    else:
        print(seats, "seats available.")

    # Display ticket details
    print("\n" + "=" * 45)
    print("             JOURNEY DETAILS")
    print("=" * 45)

    print("Journey       :", source, "->", destination)
    print("Date          :", date_object.strftime("%A"))
    print("Passenger     :", passenger_type)
    print("Base price    : Rs", int(base_price))
    print("Age discount  :-Rs", int(discount))
    print("Weekend       : +Rs", int(weekend_charge))
    print("Tatkal charge : +Rs", int(tatkal_charge))
    print("-" * 45)
    print("TOTAL         : Rs", int(total))
    print("Seats left    :", seats)

    # Payment simulation
    print("\n" + "=" * 45)
    print("              PAYMENT")
    print("=" * 45)

    payment = int(input("Enter payment amount: Rs "))

    if payment == total:
        print("Payment successful!")
        print("Your ticket is booked.")

    elif payment > total:
        balance = payment - total
        print("Payment successful!")
        print("Extra amount: Rs", int(balance))
        print("Your ticket is booked.")

    else:
        balance = total - payment
        print("Insufficient payment!")
        print("Please pay Rs", int(balance), "more.")

else:
    print("Sorry! This route is not available.")

print("\nThank you for booking with Indian Railways!")