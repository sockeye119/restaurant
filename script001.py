def act1():

    from food import Food
    from drink import Drink
    from dressing import Dressing

    food1 = Food('High Five Power Salad', 1580, 476)
    food2 = Food('Smoked Duck & Honey Nut Salad', 1080, 220)
    food3 = Food("Grilled Chicken & Egg Salad", 980, 262)
    food4 = Food('Prosciutto & Mimolette Cheese Salad', 980, 139)
    food5 = Food('Garlic Shrimp Salad', 1280, 113)
    food6 = Food('Skip', 0, 0)

    foods = [food1, food2, food3, food4, food5, food6]
    
    dressing1 = Dressing('Classic Caesar',0,73)
    dressing2 = Dressing('Onion Soy',0,107)
    dressing3 = Dressing('Creamy Seasame',0,67)
    dressing4 = Dressing('Honey Mustard',0,127)
    dressing5 = Dressing('Balsamic Vinaigrette',0,127)
    dressing6 = Dressing('Skip',0,0)

    dressings = [dressing1, dressing2, dressing3, dressing4, dressing5, dressing6]
    
    drink1 = Drink('Green Smoothie', 360, 126)
    drink2 = Drink('Homemade Soup', 360, 234)
    drink3 = Drink('Iced Coffee', 100, 15)
    drink4 = Drink('Seasonal Smoothie', 500, 245)
    drink5 = Drink('Skip',0, 0) 

    drinks = [drink1, drink2, drink3, drink4, drink5]
    
    print()
    print('***** FOOD MENU *****')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print()    
    print('***** DRESSING MENU *****')
    index = 0
    for dressing in dressings:
        print(str(index) + '. ' + dressing.info())
        index += 1

    print()
    print('***** DRINK MENU *****')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

    print('--------------------')

    food_order = int(input('Please select a number from the food menu: '))
    selected_food = foods[food_order]
    
    dressing_order = int(input('Please select a number from the dressing menu: '))
    selected_dressing = dressings[dressing_order]

    drink_order = int(input('Please select a number from the drink menu: '))
    selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print()
    print('----------------------------------------------------------')
    print('Here is your total order:')
    print()
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_dressing.name) + ' ¥' + str(selected_dressing.price) + ' x ' + str(count))
    print(str(selected_drink.name) + ' ¥' + str(selected_drink.price) + ' x ' + str(count))
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



