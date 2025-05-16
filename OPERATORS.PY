# Mini project : Shopping Cart Calculation

item_prices = [20,15,30,5, 10] # List of item prices
total_cost = sum(item_prices) # Arithmetic operator to calculate total cost (sum() is a inbuilt function in python)

#Applying a discount
discount = 0.1 # 10% discount
total_cost -= total_cost * discount # Applying discount using -= assignment operator 

# Free shipping threshold
free_shipping_threshold = 50

#Decision making with comparison operators

if total_cost >= free_shipping_threshold:
    print(f"Total cost after discount : ${total_cost}. you got free shipping!")
else:
    print(f"Total cost after discount: {total_cost}. You need ${free_shipping_threshold - total_cost} more for free shipping!")

# thats it lets run and see the output
