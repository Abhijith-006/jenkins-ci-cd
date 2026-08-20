print("HOSPITAL QA TEST")
print("----------------")

age = 65

if age >= 60:
    print("Test 1 - Senior Citizen: PASS")
else:
    print("Test 1 - Senior Citizen: FAIL")

insurance = True

if insurance:
    print("Test 2 - Insurance: PASS")
else:
    print("Test 2 - Insurance: FAIL")

appointment = "Normal"

if appointment in ["Normal", "Emergency", "Follow-up"]:
    print("Test 3 - Appointment Type: PASS")
else:
    print("Test 3 - Appointment Type: FAIL")

print("All basic QA tests completed.")
