print("====== ZOMATO ORDER RECEIPT ======")

restaurant = input("Enter Restaurant Name: ")
items = int(input("Enter Number of Items: "))
price = float(input("Enter Price Per Item: "))

food_type = input("Enter Food Type (Veg/Non-Veg): ")

# Calculate subtotal
subtotal = items * price

# Calculate GST
gst = subtotal * 18 / 100

# Delivery charge
delivery = 40

# Food surcharge
if food_type.lower() == "non-veg":
    surcharge = 20
else:
    surcharge = 0

# Calculate total
total = subtotal + gst + delivery + surcharge

# Print receipt
print("\n================================")
print("       ZOMATO ORDER RECEIPT")
print("================================")
print("Restaurant :", restaurant)
print("Food Type  :", food_type)
print("Items      :", items, "* Rs", price)
print("Subtotal   : Rs", subtotal)
print("GST (18%)  : Rs", gst)
print("Delivery   : Rs", delivery)
print("Surcharge  : Rs", surcharge)
print("--------------------------------")
print("TOTAL      : Rs", total)
print("================================")
print("      THANK YOU! VISIT AGAIN")
print("Updated Zomato Bill Calculator")

