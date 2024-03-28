secret = 7
guess = 5
if guess < secret:
    print ("Too Low")
elif guess > secret:
    print("Too High")
else:
    print ("Just Right")


small = True
green = False

if small and green:
    print("Pea")
elif small and not green:
    print("Cherry")
elif not small and green:
    print("Watermelon")
else:
    print("Pumpkin")


list = [3, 2, 1, 0]
for item in list:
    print(item)

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('Too Low')
    elif number == guess_me:
        print('Found It!')
        break
    else:
        print('Oops')
        break
    number += 1

guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break