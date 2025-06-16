#Multiplying the numbers on a list and finding if they are Odd or Even.

numbers = [7, 3, 5]
product = numbers[0] * numbers[1] * numbers[2]

if product % 2 == 0:
    product_status = "even"
else: 
    product_status = "odd"

print(numbers)
msg = f"The product of the numbers is {product}, which is an {product_status} number."
print(msg)