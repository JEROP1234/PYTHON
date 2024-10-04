import random

# def guessing_game(start, end):
#     number = random.randint(start, end)
#     guess = None  
    
#     while guess != number:
#         guess = int(input(f"Guess a number between {start} and {end}: \n"))
        
#         if guess < number:
#             print("Too low")
#         elif guess > number:
#             print("Too high")
#         else:
#             print("Congratulations, you won!")


# guessing_game(1, 100)


answer =random.randint(1,100)
level=input("enter hard, moderate or easy level: \n")


def check_answer(answer, guess):
    if answer>guess:
        print("the number is too high: \n")
    elif answer<guess:
        print("the number is too low: \n ")
    else:
        print("your number is correct !,you won: \n" )


def set_difficulty():
    if level=='hard':
        return 5
    elif level=='moderate':
        return 10
    elif level=='easy':
        return 15
    else:
        print('enter a valid level: ')


attempts=set_difficulty()

while attempts>0:
    print("you have {} remaining".format(attempts))
    guess=int(input('Guess a number:'))
    check_answer(guess, answer)
    attempts-=1
    if guess==answer:
        print(f"you got it the answer is {answer}")
        break
    elif attempts==0:
        print("you have run out of attempts")
    else:
        print("guess again")
    
 
    

