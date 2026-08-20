import math

customer_id = input("Customer ID: ")
age = int(input("Age: "))
salary = float(input("Monthly Salary: "))
existing = float(input("Existing Loan Amount: "))
credit = int(input("Credit Score: "))
employment = input("Employment Type: ")
loan = float(input("Requested Loan Amount: "))
years = int(input("Loan Tenure (years): "))

dti = (existing / salary) * 100
eligible = salary * 20

if credit >= 750:
 rate = 8
elif credit >= 650:
 rate = 10
else:
 rate = 13

months = years * 12
r = rate / 1200
emi = loan * r * (1 + r) ** months / ((1 + r) ** months - 1)

approved = (21 <= age <= 60 and salary > 0 and
 credit >= 650 and dti <= 40 and loan <= eligible)

print("\n--- LOAN RESULT ---")
print("Customer ID:", customer_id)
print("Employment:", employment)
print("DTI:", round(dti, 2), "%")
print("Eligible Amount:", round(eligible, 2))
print("Interest Rate:", rate, "%")
print("EMI:", round(emi, 2))
print("Status:", "APPROVED" if approved else "REJECTED")
