odd_list = []
even_list = []

while True:
    user_input = input("Enter a number (or press Enter to stop): ")
    
    if user_input == "":
        break
    
    if user_input.isdigit():
        number = int(user_input)
        
        if number % 2 != 0:
            odd_list.append(number)
        else:
            even_list.append(number)
    else:
        print("Please enter a valid integer.")

# Print the results
print("Odd numbers:", odd_list)
print("Even numbers:", even_list)

print("Even numbers:", even_list)
49