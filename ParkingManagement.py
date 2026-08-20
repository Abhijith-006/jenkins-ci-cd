# Smart Parking Management

vehicle_number = "KL01AB1234"
vehicle_type = "Car"

available_slots = 5
hours = 3
peak_hour = True
vip = False

# Slot allocation
if available_slots > 0:
    slot = 1
    print("Parking Slot:", slot)
else:
    print("Parking Full")
    exit()

# Parking rates
if vehicle_type == "Bike":
    rate = 20
elif vehicle_type == "Car":
    rate = 40
elif vehicle_type == "SUV":
    rate = 60
elif vehicle_type == "Truck":
    rate = 80
elif vehicle_type == "EV":
    rate = 50
else:
    rate = 0

fee = rate * hours

# Peak hour pricing
if peak_hour:
    fee = fee * 1.5

# VIP discount
if vip:
    fee = fee * 0.5

# EV charging
if vehicle_type == "EV":
    fee = fee + 50

print("SMART PARKING")
print("-------------")
print("Vehicle:", vehicle_number)
print("Vehicle Type:", vehicle_type)
print("Hours:", hours)
print("Peak Hour:", peak_hour)
print("VIP:", vip)
print("Parking Fee:", fee)
print("Vehicle Exit: SUCCESSFUL")
