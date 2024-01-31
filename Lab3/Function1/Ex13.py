import random
def guess():
    print("Hello! What is your name?")
    name=str(input())
    cnt=0
    print("Well,",name,", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    number=random.randint(1, 20)
    a=int(input())
    while number!=a:
        if a>number:
            print("Your guess is too high.")
            print("Take a guess.")
        else:
            print("Your guess is too low.")
            print("Take a guess.")
        a=int(input())
        cnt+=1
    print("Good job,",name,"! You guessed my number in",cnt+1,"guesses!")
guess()