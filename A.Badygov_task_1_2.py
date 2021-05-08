arr = []
sum_numbers = 0
for numbers in range(1, 1000,2):
    arr.append(numbers ** 3)
for numbers in arr:
    sum_number = 0
    numbers_copy = numbers
    while numbers_copy > 0:
        number = numbers_copy % 10
        sum_number += number
        numbers_copy = numbers_copy // 10
    if sum_number % 7 == 0:
        sum_numbers += numbers
print(sum_numbers)
sum_numbers = 0
for numbers in arr:
    sum_number = 0
    numbers_copy = numbers + 17
    while numbers_copy > 0:
        number = numbers_copy % 10
        sum_number += number
        numbers_copy = numbers_copy // 10
    if sum_number % 7 == 0:
        sum_numbers = sum_numbers + (numbers + 17)
print(sum_numbers)

