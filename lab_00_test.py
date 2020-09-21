from math import *
print("Hello I am the HAL 9000 college cost estimator")
name = input("what is yor name?")
print("good afternoon " + name + " please only input whole numbers")
needed_credits = input(name + ", how many credits do you need to take to complete your degree?")
average_credits_taken = input(name + ", how many credits do you on average take per semester?")
taken_credits = input(name + ", how many credits have you taken so far?")
cost_per_credit = input(name + ", how much does a credit cost at your college?")
credits_remaining=int(needed_credits)-int(taken_credits)
semesters_remaining =int(credits_remaining)/int(average_credits_taken)
rounded_semsesters_remaining=ceil(semesters_remaining)
total_cost =int(credits_remaining) * int(cost_per_credit)
print("you have " + str(rounded_semsesters_remaining) + " semesters remaining")
print("your " + str(credits_remaining) + " remaining credits will cost you $"+ str(total_cost) + " to complete")











