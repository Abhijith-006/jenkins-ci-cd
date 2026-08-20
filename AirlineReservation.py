# Airline Reservation System

passenger = "Abhi"
passenger_type = "Adult"
travel_class = "Economy"

available_seats = 5
base_fare = 5000

# Class pricing
if travel_class == "Economy":
    fare = base_fare
elif travel_class == "Business":
    fare = base_fare * 2
else:
    fare = base_fare * 3

# Passenger pricing
if passenger_type == "Child":
    fare = fare * 0.7
elif passenger_type == "Senior":
    fare = fare * 0.8

# Dynamic pricing
if available_seats <= 2:
    fare = fare * 1.20

# Baggage
baggage = 20

if baggage > 15:
    baggage_charge = (baggage - 15) * 500
else:
    baggage_charge = 0

total_fare = fare + baggage_charge

print("AIRLINE RESERVATION")
print("-------------------")
print("Passenger:", passenger)
print("Passenger Type:", passenger_type)
print("Class:", travel_class)
print("Available Seats:", available_seats)
print("Ticket Fare:", fare)
print("Baggage Charge:", baggage_charge)
print("Total Fare:", total_fare)

print("Booking: SUCCESSFUL")
