# Может я не понял задания и надо было сделать не просто через if. Или если чисел было не 20, а 2000, но там добавляется только цикл.
# Можно добавить проверку ввода цисел от 0 до 20
number = int(input('Введите число процентов для склонения от 0 до 20: '))
if number <= 1:
    print(number, 'процент')
if number > 1 and number <= 4:
    print(number, 'процента')
if number >= 5:
    print(number, 'процентов')

