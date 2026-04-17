capacity = 350
remaining_seats = capacity

total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while True:
    tickets = int(input("Enter number of tickets (and 0 to exit): "))

    if tickets == 0:
        break

    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED (1-15 only)")
        rejected_bookings += 1
        continue

    if tickets > remaining_seats:
        print("BOOKING REJECTED Not enough seats available")
        rejected_bookings += 1
        continue

    valid_booking = True
    for i in range(tickets):
        age = int(input(f"Enter age for person {i+1}: "))
        if age < 12:
            valid_booking = False
            break

    if valid_booking:
        print(f"BOOKING CONFIRMED {tickets} tickets")
        total_bookings += 1
        tickets_sold += tickets
        remaining_seats -= tickets
    else:
        print("BOOKING REJECTED Age restriction")
        rejected_bookings += 1

    if remaining_seats == 0:
        print("Theatre is now FULL. No more bookings.")
        break

print("\n FINAL REPORT ")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {remaining_seats}")