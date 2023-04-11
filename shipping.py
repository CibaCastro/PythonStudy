weight = float(input("What is the weight of your package in lbs?\n"))
#weight = 8.4

ground_price = 0.00
ground_flat = 20.00
premium_price = 125.00
drone_price = 0.00

#Ground Shipping Pricelist
if weight <= 2:
  ground_price = 1.50 * weight + ground_flat
elif weight <= 6:
  ground_price = 3.00 * weight + ground_flat
elif weight <= 10:
  ground_price = 4.00 * weight + ground_flat
else:
  ground_price = 4.75 * weight + ground_flat

print("Ground Shipping for this weight costs ", ground_price)
print("Premium Shipping for this weight costs ", premium_price)

#Drone Shipping Pricelist
if weight <= 2:
  drone_price = 4.50 * weight
elif weight <= 6:
  drone_price = 9.00 * weight
elif weight <= 10:
  drone_price = 12.00 * weight
else:
  drone_price = 14.25 * weight
  
print("Drone Shipping for this weight costs ", drone_price)

best_price = min(ground_price, premium_price, drone_price)

if best_price == ground_price:
    print ("The best option is to send via Ground Standard")
elif best_price == premium_price:
    print ("The best option is to send via Ground Premium")
elif best_price == drone_price:
    print ("The best option is to send via Drone")
else:
    print ("There was an error in the calculation")