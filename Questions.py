

Question1 = str(input("Are you risk avers? "))

if Question1 == 'yes':
    t = 1
else: ValueError
print('Plase')

while True:
    try:
        money = int(input("How much money do you want to invest ? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if money >= 1000:
    s = 1
else:
    s = 0

while True:
    try:
        time = int(input("For how long do you want to invest your money? (Please enter number in years) "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if time >= 2:
    f = 1
else:
    f = 0

while True:
    try:
        loss = str(input("Would a temporarily 10 % loss of your money make you nervous ? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if loss == 'yes':
    t = 1
else:
    t = 0

final_score = t + s + f

print("Your estimated score is", final_score)


if final_score >= 2:
    print("You are risk avers!")



