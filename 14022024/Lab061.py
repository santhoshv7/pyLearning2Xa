def make_pizza(*toppings,base):
    print(toppings,base)
    for topping in toppings:
        print (topping)
        return toppings,base

make_pizza("onion", "Chicken", "capsi", base ="pure wheat")