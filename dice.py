import random 
print("This game to guess a number from the dice and then the dice is thrown. If you guess the same number as outcome on the dice you Won. If not you Lose")
b=1
while b==1:
    a=int(input("Enter any number between 1 to 6--->"))
    x=random.randint(1,6)
    if 1<=a<=6:
        if a==x:
            print("Congrats! You Won .")
        else:
            print("BETTER LUCK NEXT TIME! Computer generated is-",x)
    else:
        print("Enter a number between 1 and 6")
    b=int(input("Want to play more enter 1 and for exit enter 0:-->"))