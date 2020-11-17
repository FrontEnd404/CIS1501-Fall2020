import math

def payment_amount(p, r, t):

    r = r/(12*100)

    t = t*12
    payment_amount = (p*r*pow(1+r,t))/(pow(1+r,t)-1)
    return payment_amount

def number_of_payments(rate, payment_amount, present_value ):
    number_of_payments = (-math.log(1 - rate * present_value/ payment_amount))/ math.log(1 + rate)
    return number_of_payments

print("would you like to calculate payment or number of payments?")
which_function = input("if you would like to calculate payment type 1 if you would like to calculate number of payments type 2 ")

if which_function == "1":
    keep_going = "yes"
    while keep_going == "yes":
        try:
            principal = float(input("what is the total amount of the loan you took out?"))
        except:
              print("sorry you must enter a number")
              continue
        try:
            rate = float(input("what is the annual interest rate percentage? "))
        except:
            print("sorry you must enter a number")
            continue
        if rate > 100 or rate < 0:
            print("sorry the interest rate must be between 1 and 100")
        try:
            time = float(input("how will it take to pay off this loan?"))
        except:
            print("sorry you must enter a number")
            continue
        payment_amount = payment_amount(principal, rate, time)
        print("payment amount is $", payment_amount)
        keep_going = "no"
if which_function == "2":
    keep_going = "yes"
    while keep_going == "yes":
        try:
            present_value = float(input("what is the total amount of the loan you took out?"))
        except:
            print("sorry you must enter a number")
            continue
        try:
            rate = float(input("what is the annual interest rate percentage? "))/100
        except:
            print("sorry you must enter a number")
            continue
        if rate > 100 or rate < 0:
            print("sorry the interest rate must be between 1 and 100")
        try:
            payment_amount = float(input("how much do you pay each period?"))
        except:
            print("sorry you must enter a number")
            continue
        number_of_payments = number_of_payments(rate,payment_amount, present_value )
        print("the number of payments is", number_of_payments)
        keep_going = "no"

