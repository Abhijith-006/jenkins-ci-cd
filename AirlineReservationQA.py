print("AIRLINE QA TEST")
print("----------------")

available_seats = 5

if available_seats > 0:
    print("Test 1 - Seat Availability: PASS")
else:
    print("Test 1 - Seat Availability: FAIL")

passenger = "Abhi"

if passenger != "":
    print("Test 2 - Passenger: PASS")
else:
    print("Test 2 - Passenger: FAIL")

baggage = 20

if baggage > 15:
    print("Test 3 - Excess Baggage: PASS")
else:
    print("Test 3 - Excess Baggage: FAIL")

print("All basic QA tests completed.")
