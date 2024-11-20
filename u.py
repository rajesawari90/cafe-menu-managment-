import pandas as pd
from sqlalchemy import create_engine
#creating menu
menu = {
    "Espresso": 150,
    "Cappuccino": 180,
    "Latte": 200,
    "Iced Coffee": 220,
    "Green Tea": 120,
    "Smoothie": 250,
    "Veg Sandwich": 100,
    "Chicken Sandwich": 150,
    "French Fries": 80,
    "Nachos": 130,
    "Garlic Bread": 90,
    "Paneer Tikka": 180,
    "Chocolate Cake": 150,
    "Cheesecake": 200,
    "Brownie": 120,
    "Ice Cream Sundae": 180,
    "Fruit Salad": 100,
    "Veg Biryani": 250,
    "Chicken Biryani": 300,
    "Pasta Alfredo": 220,
    "Grilled Chicken": 350,
    "Paneer Butter Masala": 200
}
data = {'items' :['new order']}
#create an  dataframe
df = pd.DataFrame(data)

print("Welcome to Python cafe")
print("Espresso: 150\n")
print("Cappuccino: 180 Rs\nLatte: 200 Rs\nIced Coffee: 220\n Green Tea: 120\n Smoothie: 250\nVeg Sandwich: 100\nChicken Sandwich: 150\nFrench Fries: 80\n")
print("Nachos: 130\nGarlic Bread: 90\nPaneer Tikka: 180\nChocolate Cake: 150\nCheesecake: 200\nBrownie: 120\nice Cream Sundae: 180")

order_total = 0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
        # Adding a new row
        df.loc[len(df)] = [item]
        print(df)
    else:
        print("Sorry, we don't have that item on the menu")
    
    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print (f"The total amount to pay is {order_total}")
# Create a connection to the MySQL database
engine = create_engine('mysql+mysqlconnector://new_user:password123@localhost/mydatabase')

# Write the DataFrame to a SQL table
df.to_sql('my_table', con=engine, if_exists='append', index=False)
