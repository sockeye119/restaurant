def act6():

    from food import Food
    from drink import Drink
    from dessert import Dessert

    food1 = Food('Asian Curry Plate (soup and mini desert set)', 1200, 590)
    food2 = Food(' Rice Bowl with Vegetables (soup and mini desert set)', 1200, 370)
    food3 = Food('Pizza Toast (soup and mini desert set)', 1000, 310)
    food4 = Food('Vegan Plate (soup and mini dessert set)', 1200, 310)
    food5 = Food('Herb Fragrant Salt Pork Bowl (soup and mini dessert set)', 1000, 680)
    food6 = Food('Skip',0,0)

    foods = [food1, food2, food3, food4, food5, food6]

    drink1 = Drink('Decaf Coffee', 450, 0)
    drink2 = Drink('Organic Black Tea', 450, 0)
    drink3 = Drink('Morinaga Tea', 500, 0)
    drink4 = Drink('Citrus Unshiu Juice', 450, 35) 
    drink5 = Drink('Perrier', 350, 0)
    drink6 = Drink('Skip',0,0)
               
    drinks = [drink1, drink2, drink3, drink4, drink5, drink6]

    dessert1 = Dessert('Pancake with Vegan Butter and Fruits', 880, 105)
    dessert2 = Dessert('Waffles with Soy Milk Whipped Cream and Fruits', 880, 180)
    dessert3 = Dessert('Brownie Soy Milk Whipped', 650, 200)
    dessert4 = Dessert('Clafoutis with Shanti Sauce', 700, 250)
    dessert5 = Dessert('Coconut Kudzu Pudding', 650, 140)
    dessert6 = Dessert('Skip',0,0)

    desserts = [dessert1, dessert2, dessert3, dessert4, dessert5, dessert6]
    
    print()
    print('***** FOOD MENU *****')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print()
    print('***** DRINK MENU *****')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

    print()
    print('***** DESSERT MENU *****')
    index = 0
    for dessert in desserts:
        print(str(index) + '. ' + dessert.info())
        index += 1
    
#if choose invalid number

    print('--------------------')

    while True:
        food_order = input('Please select a number from the food menu: ')

        if food_order == '0' or food_order == '1' or food_order == '2' or food_order == '3' or food_order == '4' or food_order == '5' or food_order == '6':
            selected_food = foods[int(food_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break

    while True:
        drink_order = input('Please select a number from the drink menu: ')

        if drink_order == '0' or drink_order == '1' or drink_order == '2' or drink_order == '3' or drink_order == '4' or drink_order == '5' or drink_order == '6':
            selected_drink = drinks[int(drink_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break
     
    while True:
        dessert_order = input('Please select a number from the dessert menu: ')

        if dessert_order == '0' or dessert_order == '1' or dessert_order == '2' or dessert_order == '3' or dessert_order == '4' or dessert_order == '5' or dessert_order == '6':
            selected_dessert = desserts[int(dessert_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break

    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))

    result =selected_food.get_total_price(count) + selected_drink.get_total_price(count) + selected_dessert.get_total_price(count)

    #print total

    print()
    print('----------------------------------------------------------')
    print('Here is your total order:')
    print()
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_drink.name) + ' ¥' + str(selected_drink.price) + ' x ' + str(count))
    print(str(selected_dessert.name) + ' ¥' + str(selected_dessert.price) + ' x ' + str(count))
    
    if count>=3:
        print ('10% discount')

    else:
        print('    ')

    print('----------------------------------------------------------')
    print('Your total is ' + str(result) + ' Yen')
    print()
    print('Thank you for using W-Delivers! We hope to serve you again soon!')
    print('----------------------------------------------------------')
    print()
    print('Your order is on its way')

    import time

    for i in range(100):
        print('.', end='')
        time.sleep(1)
