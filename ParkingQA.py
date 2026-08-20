print("PARKING QA TEST")
print("----------------")

available_slots = 5

if available_slots > 0:
    print("Test 1 - Slot Availability: PASS")
else:
    print("Test 1 - Slot Availability: FAIL")

vehicle_type = "Car"

if vehicle_type in ["Bike", "Car", "SUV", "Truck", "EV"]:
    print("Test 2 - Vehicle Type: PASS")
else:
    print("Test 2 - Vehicle Type: FAIL")

peak_hour = True

if peak_hour:
    print("Test 3 - Peak Hour Pricing: PASS")
else:
    print("Test 3 - Peak Hour Pricing: FAIL")

print("All basic QA tests completed.")
