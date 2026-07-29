from readfile import TextAnalyzer

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
    static_call()
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
    for i in x.split(','):
        if i!="" and int(i)%2 == 1:
            final_list.append(i)
    return final_list

def static_call():
    TextAnalyzer.random_no_gen()

def sort_list(x):
    return sorted(x, reverse=True)


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
     10 WC using class
     11 check cool in string
     12 sort list
     """)
    if inputval == "1":
        print(add_numbers())
    elif inputval == "2":
        print(subtract_numbers())
    elif inputval == "3":
        even_or_odd()
    elif inputval == "4":
        print_series(input("Enter the max number"))
    elif inputval == "5":
        print(string_reverse(input("Enter the string")))
    elif inputval == "6":
        print(largest_number([5,6,7,5,8,55,52,5,63,99]))
    elif inputval == "7":
        print(remove_duplicates(input("Enter the string")))
    elif inputval == "8":
        word_statistics(input("Enter the string"))
    elif inputval == "9":
        print(print_odd_numbers(input("Enter the string")))
    elif inputval == "10":
        obj = TextAnalyzer(input("Enter the string"))
        print(obj.word_count())
    elif inputval == "11":
        obj = TextAnalyzer(input("Enter the string"))
        print(obj.check_string_in_stmt())
    elif inputval == "12":
        print(sort_list([4,6,7,7,8,8,5,4,3]))
    else:
        print("Invalid input")


