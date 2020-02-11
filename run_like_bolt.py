from People_class import People
from Customer_class import Customer
from Food_class import Food
from Order_class import Orders

# As I an resturant owner i can create customers

customer1 = Customer('John', '21 downtown abbey, London')
customer2 = Customer('Anabella', '45 filler road, Hackney')

# AS a resturant owner i can create new food items

# 3 mains
main1 = Food('Sea Bass', 17.5, ['sea bass fish'])
main2 = Food('Omelete du Formage Avec champignon', 9, ['Egg', 'Cheese', 'Mushroom'])
main3 = Food('Fiorentina', 5.5, ['Tomato sauce', 'Egg', 'Mozzarella', 'Fresh Spinach'])

# 3 sides
side1 = Food('Garlic Bread', 4, ['bread', 'garlic'])
side1 = Food('Garlic Bread cheese', 4, ['bread', 'garlic', 'cheese'])

# 3 drinks
drink1 = Food('water', 2, ['water'])
drink2 = Food('CokeCola', ['others'])
drink3 = Food('Smoothies', 4, ['orange', 'carrots', 'kiwi'])

# 3 combos

# as a resturanter owner i can create new orders and add food items for a customer

#Opening a tab
order1 = Orders(customer1)

order1.add_items_order(main3)
order1.add_items_order(drink3)

print(order1.customer.name)
print(order1.tab[0].items)


for item in order1.tab:
     print(item.items, f'${item.price}')

# we want to a game to keep running

# following options:
#   As a user I can create a customer
#   As a user I can create Food items
#   As a user I can list food items
#   As a user I can create Orders
#   As a user I can add items to order (requires a specific order and selective of food items)
#   As a user I can see the total of an order (requires calculating the total of all the food items)

# Create a simple switch board

while True:
    pass
    # print option
    print('where would you like to go?\n 1 - create a customer')
    user_input = input('>>>>')
    # get user input
    if user_input == '1' or user_input == 'create customer' in user_input:
        print('I am going to create a customer')
        # Get user input for x or y
        # use it to create a customer
        # 
    elif user_input == '2' or 'create food' in user_input:
        print('I am going to create some fooooooooooooooo.....oood')

    # Evaluate and go to each option
        # inside each option, do logic and create what ever you need to create
