import random

name = input("Hello!! What is your name: ")
print(f"Hey! {name}, Lets Play A Game! \n So Guess a Number which i am thinking right now!!!!!")
k = int(random.randint(0,100))
print('You have only 10 chances')
b = 9
s = 1
# print(f"Choose number between {k - 1230 } to {k + 1409}")
if k == 10:
    while(b >= 0):
        g = int(input("your number "))
        if g == k:
            print(f"CONGRATULATIONS {name} YOU GUSSED RIGHT IN {s} chances")
            break

        elif g < k:
            print(f"NO BIGGER THAN {g} chances left = {b}")
            b = b - 1
            s = s + 1
            continue

        elif g > k: 
            print(f'NO SMALLER THAN {g} chances left {b}')
            b = b-1
            s = s + 1
            continue
            

print("correct answer is ", k)