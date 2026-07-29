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

def string_reverse(x):
    return x[::-1]

def largest_number(x):
    largest = int(x[0])
    for i in x:
        if int(i) > largest:
            largest = int(x[i])
    return largest

def remove_duplicates(x):
    final_list = []
    for i in x:
        if i not in final_list:
            final_list.append(i)
    return final_list

def word_statistics(x):
    vowels = 0
    consonants = 0
    words= 0
    for i in x:
        if i in "aeiou":
            vowels += 1
        if i not in "aeiou":
            consonants += 1
    print(f'Vowels {vowels}')
    print(f'Consonants {consonants}')
    print(f'Words {len(x.split())}')

def print_odd_numbers(x):
    final_list = []
    for i in x:
        if int(i)%2 == 1:
            final_list.append(i)
    return final_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MAX_SIZE=100
    inputval= input("""Enter the option!
     1 For Addition
     2 for Subtraction
     3 to check Even or Odd
     4 to print series
     5 to reverse a string
     6 for largest number
     7 to remove duplicates
     8 for word statistics
     9 to print odd numbers
     """)
    if inputval == "1":
        print(add_numbers())
    #elif inputval == "2":
