import math

def add_numbers():
    total = 0
    while True:
        value = input("Enter the number or 'Stop' to exit")
        if value == "Stop":
            break
        total += int(value)

    return total

def subtract_numbers():
    x= input("Enter the 1st number")
    y= input("Enter the 2nd number")
    return int(x) - int(y)

def even_or_odd():
    while True:
        value= input("Enter the number or 'Stop' to exit")
        if value == "Stop":
            break
        elif int(value)%2 == 0:
            print("Even")
        elif int(value)%2 == 1:
            print("Odd")

def print_series(x):
    i=0
    while i<int(x):
        print(i)
        i+=1





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MAX_SIZE=100
    inputval= input("""Enter the option!
     1 For Addition
     2 for Subtraction
     3 to check Even or Odd
     4 to print series
     5 to sum the series
     6 for multiplication
     7 to reverse a string
     8 to count vowels
     9 for largest number
     10 to remove duplicates
     11 for word statistics
     12 to print odd numbers
     """)
    if inputval == "1":
        print(add_numbers())
    elif inputval == "2":
