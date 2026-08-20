# Banking Loan Approval System

customer_id = "C101"
age = 30
salary = 50000
existing_loan = 10000
credit_score = 750
employment = "Government"
requested_loan = 300000
tenure = 5

# Debt-to-income ratio
dti = (existing_loan / salary) * 100

# Eligible loan
eligible_loan = salary * 10

# Interest rate
if credit_score >= 750:
    interest_rate = 8
elif credit_score >= 650:
    interest_rate = 10
else:
    interest_rate = 14

# EMI
monthly_rate = interest_rate / (12 * 100)
months = tenure * 12

emi = (requested_loan * monthly_rate *
       (1 + monthly_rate) ** months) / \
      ((1 + monthly_rate) ** months - 1)

# Approval
if credit_score >= 650 and dti <= 40 and requested_loan <= eligible_loan:
    status = "APPROVED"
else:
    status = "REJECTED"

print("BANKING LOAN APPROVAL")
print("----------------------")
print("Customer ID:", customer_id)
print("Age:", age)
print("Salary:", salary)
print("Existing Loan:", existing_loan)
print("Credit Score:", credit_score)
print("Employment:", employment)
print("Requested Loan:", requested_loan)
print("DTI:", round(dti, 2), "%")
print("Eligible Loan:", eligible_loan)
print("Interest Rate:", interest_rate, "%")
print("EMI:", round(emi, 2))
print("Status:", status)
