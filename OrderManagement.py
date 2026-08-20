# E-Commerce Order Processing

product = "Laptop"
quantity = 2
price = 50000

coupon = "SAVE10"
tax_rate = 18

subtotal = quantity * price

# Product discount
discount = subtotal * 0.10

# Coupon discount
if coupon == "SAVE10":
    coupon_discount = subtotal * 0.10
else:
    coupon_discount = 0

amount = subtotal - discount - coupon_discount

# GST
gst = amount * tax_rate / 100

# Free shipping above 50000
if amount >= 50000:
    shipping = 0
else:
    shipping = 100

final_amount = amount + gst + shipping

print("E-COMMERCE ORDER")
print("----------------")
print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Coupon Discount:", coupon_discount)
print("GST:", gst)
print("Shipping:", shipping)
print("Final Amount:", final_amount)
