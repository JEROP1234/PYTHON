#import random number from computer
import random
#ganaerate a random interger from btwn 1-100
target_number = random.randint(1,100)
#rule games 
print ("welcome to my game guess a number")
user_guess= 0 
while user_guess!= target_number:
    user_guess= int (input("user_guess":))
    if user_guess> target_number:
        print("fail")
    if user_guess<target_number:
        print("less")
else:
    print("congrats")

