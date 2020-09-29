Menu = {
    "soda": 2.00,
    "hamburger": 12.00,
    "hard taco": 3.00,
    "soft taco": 3.00,
    "bean burrito": 5.00,
    "steak burrito": 6.00,
    "chicken burrito": 6.00,
}
print("hello welcome to 404 cafe today our menu includes")
print(Menu)
Food_1 = input("what is the first thing you would like to order")
Food_2 = input("what is the second thing you would like to order")
Food_3 = input("what is the third thing you would like to order")

value_1 = (Menu.get(Food_1))
value_2 = (Menu.get(Food_2))
value_3 = (Menu.get(Food_3))
Order_Total = value_1 + value_2 + value_3
Order_Total_Plus_Tax = Order_Total * 1.06
Tax = Order_Total * .06

print("thank you here is your receipt")
print(Food_1)
print("$" + str(value_1))
print(Food_2)
print("$" + str(value_2))
print(Food_3)
print("$" + str(value_3))
print("total tax")
print("$" + str(Tax))
print("Your order total")
print("$" + str(Order_Total_Plus_Tax))



# print(value_1)



# print(Menu.get("soda"))
