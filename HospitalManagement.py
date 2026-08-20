# Hospital Appointment and Billing

patient_name = "Rahul"
age = 65
appointment_type = "Normal"

consultation_fee = 500
lab_charge = 1000
medicine_charge = 500

# Senior citizen discount
if age >= 60:
    consultation_fee = consultation_fee * 0.80

# Follow-up discount
if appointment_type == "Follow-up":
    consultation_fee = consultation_fee * 0.50

insurance = True

total = consultation_fee + lab_charge + medicine_charge

if insurance:
    insurance_coverage = total * 0.70
else:
    insurance_coverage = 0

payable = total - insurance_coverage

print("HOSPITAL BILL")
print("-------------")
print("Patient:", patient_name)
print("Age:", age)
print("Appointment:", appointment_type)
print("Consultation Fee:", consultation_fee)
print("Lab Charges:", lab_charge)
print("Medicine Charges:", medicine_charge)
print("Insurance:", insurance_coverage)
print("Patient Payable:", payable)
