odd_list = []
even_list = []

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    
    if user_input == 'q':
        break
    
    number = int(user_input)
    
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print("Odd numbers:", odd_list)
print("Even numbers:", even_list)
