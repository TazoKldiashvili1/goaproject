# 1) შევქმნათ სია, შემდეგ მომხმარებელს შემოვატანინოთ 10 რიცხვი, ეს 10 რიცხვი დავამატოთ სიაში, შევქმნათ მეორე სია სადაც დავამტებთ წინა სიიდან ყველა ლუწ რიცხვს, ასევე შევქმნათ მესამე სია სადაც დავამატებთ პირველი სიიდან ველა კენტ რიცხვს
user_numbers = []


print("Please enter 10 numbers:")

for i in range(10):
    number =int(input("enter a random number"))
    user_numbers.append(number)


even_numbers = []


for num in user_numbers:
    if num % 2 == 0:
        even_numbers.append(num)


third_list = user_numbers.copy()

# გამოსახე ლისტებბი
print("Originaluri OG list:", user_numbers)
print("Listi luwi ricxvebit :) :", even_numbers)
print("Third list (originaluri mara araoriginaluri):", third_list)
