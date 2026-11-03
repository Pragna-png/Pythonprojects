print("======================================")
print("      ZOMATO ORDER RECEIPT")
print("======================================")
#Get restaurant details
restaurant = input ("Enter the Restaurant Name: ")
#Get number of items
 n = int(input("Enter the Number of Items: "))
 subtotal = 0
#Get item details
for i in range(1,n+1):
    print("\nItem",i)
    item_name = input("enter Item Name: ")
    price = float(input("Enter the Item Price:"))
    subtotal = subtotal + price
#Veg or Non-veg
food_type = input("\nOrder Type (Veg/Non-Veg): ").lower()
if food_type == "veg":
    surcharge = 0
elif food_type == "non-veg":
    surcharge = 30
else:
    surcharge = 0
    print("Invalid food type. No surcharge added.")
#Bill calculations
gst = subtotal * 18 / 100
delivery_charge = 40
total = subtotal + gst + delivery_charge + surcharge
#Print receipt
print("\n======================================")
print("      ZOMATO ORDER RECEIPT")
print("========================================")
print("Restaurant Name : ", restaurant)
print("Number of Items : ", n)
print("Food Type       : ", food_type)

print("----------------------------------------")
print("Subtotal        : Rs.",round(sub))
