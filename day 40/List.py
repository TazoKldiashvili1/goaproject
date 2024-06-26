numbers = []
even = []
odd = []


for i in range(10):
  num = int(input(f"Enter number {i+1}: "))
  numbers.append(num)


for number in numbers:
  if number % 2 == 0:
    even.append(number)
  else:
    odd.append(number)

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")