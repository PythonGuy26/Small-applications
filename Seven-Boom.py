"""
The Seven Boom game against the computer
"""
def seven_check(number):   # punctuation that check if the number divide by 7 or contain 7
    if number % 7 == 0 or "7" in str(number):
        return True
    return False


running_number = 0         # the current running number of the game
attempts = 0               # how many attempts the user succeeded
try:                       # validation check to enter only integer
    turn_changer = int(input("Who starts the game?\n 0 - The computer stars\n 1 - You start\nType here:"))
except ValueError:
    turn_changer = 0
if turn_changer == 0:      # open line
    print("The computer starts")
else:
    print("Your honor, you may begin")

while True:                # the game begin
    if turn_changer == 0:  # computer turn
        turn_changer += 1
        running_number += 1
        if seven_check(running_number):
            print("BOOM")
        else:
            print(running_number)
    else:                  # user turn
        turn_changer = 0
        running_number += 1
        attempts += 1
        user_try = input()
        if seven_check(running_number):
            if user_try.lower() != "boom":
                break
        elif user_try != str(running_number):
            break
print("You survived", attempts, "attempts, well down!!")
exit = input("press Exit:")

