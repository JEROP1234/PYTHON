player_name = input("Input gamer name: ")
place = "The player is in a runway looking for treasure along the path."
print(f"{player_name} is in a runway looking for treasure.")

path = ['treasure', 'monster', 'puzzle']

for encounter in path:
    print(f"\n{player_name} encounters a {encounter}")
    
    
    encounter= int(input("Enter a number: "))

    
    if encounter >= 100:
        print("You found a treasure! Congratulations")

    
    elif encounter< 90 and encounter > 0:
        print("You found a monster.")
    
    elif encounter==int("puzzle"):
        # print("You found a puzzle!")

      
        answer = input("What is the fastest animal? ").lower()
        
        
        if answer == 'cheetah':
            print(f"Correct {player_name} solved the puzzle and continues the journey.")
        else:
            print(f"Wrong  {player_name} failed the puzzle.")

   
    else:
         print("try again")
