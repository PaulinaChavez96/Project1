#Find the maximum number in a list.

numbers = [50000000, 7, 109, 3, 23989823982]
#max_number = max(numbers)

#print(numbers)
#msg = f"The maximum number in the list is {max_number}."
#print(msg)

if len(numbers) > 0:
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    msg = f"The maximum number in the list is {max_number}."

print(numbers)
print(msg)