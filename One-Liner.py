# 1.1.2 הכפלת אותיות במילה
def x(letter):
    return letter + letter

def double_letter(my_str):
    return "".join(list(map(x, my_str)))

def double_letter(my_str):
    return ''.join([char*2 for char in my_str])

print(double_letter("python"))
print(double_letter("we are the champions!"))


# 1.1.3 פונקציה שמחזירה את כל המספרים שמתחלקים ב 4
def divide_by_four(number):
    return number % 7 == 0

def four_dividers(number):
     return list(filter(divide_by_four, range(1, number)))

print(four_dividers(9))
print(four_dividers(30))

# 1.1.4 סכום הספרות של מספר
import functools
def sum(x, y):
    return x + y

def int_to_list(num):
    return list(map(int, str(num)))

def sum_of_digits(number):
    return functools.reduce(sum, int_to_list(number))

print(sum_of_digits(108679875784))
