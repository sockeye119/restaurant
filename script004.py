def act4():

    from food import Food
    from drink import Drink

    food1 = Food('Bibimpa', 600, 600)
    food2 = Food('Shin Ramen Noodles Set Menu', 600, 700)
    food3 = Food('Cold Noodles ', 800, 500)
    food4 = Food('Spicy Tofu Soup', 800, 520)
    food5 = Food('Bulgogi Set Menu', 1000, 890)
    food6 = Food('Skip', 0, 0)
             
    foods = [food1, food2, food3, food4, food5, food6]

    drink1 = Drink('Mineral Water', 200, 0)
    drink2 = Drink('Oolong Tea', 200, 0)
    drink3 = Drink('Skip',0 ,0) 

    drinks= [drink1, drink2, drink3]
    
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

    print('--------------------')

# if choose invalid numbers 

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

        if drink_order == '0' or drink_order == '1' or drink_order == '2' or drink_order == '3':
            selected_drink = drinks[int(drink_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break
     

    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))

    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

    #print total
    
    print()
    print('----------------------------------------------------------')
    print('Here is your total order:')
    print()
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_drink.name) + ' ¥' + str(selected_drink.price) + ' x ' + str(count))
    
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
