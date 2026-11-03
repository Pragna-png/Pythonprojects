print("===== ZOMATO BILL CALCULATOR =====")

# Get restaurant details
restaurant = input("Enter restaurant name: ")

# Get order details
items = int(input("Enter number of items: "))
price = float(input("Enter price per item: "))

# Get food type
food_type = input("Enter food type (Veg/Non-Veg): ").lower()

# Calculate subtotal
subtotal = items * price

# Calculate GST (18%)
gst = subtotal * 0.18

# Delivery charge
delivery = 40

# Food surcharge
if food_type == "veg":
    surcharge = 0
elif food_type == "non-veg":
    surcharge = 30
else:
    surcharge = 0
    print("Invalid food type. No surcharge added.")

# Calculate total
total = subtotal + gst + delivery + surcharge

# Print formatted receipt
print("\n====================================")
print("       ZOMATO ORDER RECEIPT")
print("====================================")

print(f"Restaurant      : {restaurant}")
print(f"Food Type       : {food_type.upper()}")
print(f"Items           : {items} x Rs {price:.2f} each")
print(f"Subtotal        : Rs {subtotal:.2f}")
print(f"GST (18%)       : Rs {gst:.2f}")
print(f"Delivery        : Rs {delivery:.2f}")
print(f"Surcharge       : Rs {surcharge:.2f}")

print("------------------------------------")
print(f"TOTAL           : Rs {total:.2f}")
print("====================================")
print("      THANK YOU! VISIT AGAIN")