    #Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
seconds = int(input('Введите продолжительность времени в секундах (duration): '))
while seconds < 0:
        seconds = int(input('Введите положительное продолжительность времени в секундах (duration):'))
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
month = days // 30
years = month // 12
if seconds < 60:
    print(seconds, 'сек')
if seconds >= 60 and seconds < 60*60:
    seconds = seconds % 60
    print(minutes, 'мин', seconds, 'сек')
if seconds >= 60*60 and seconds < 60*60*24:
    minutes = minutes % 60
    seconds = seconds % 60
    print(hours,'час', minutes, 'мин', seconds, 'сек')
if seconds >= 60*60*24 and seconds < 60*60*24*7:
    hours = hours % 24
    minutes = minutes % 60
    seconds = seconds % 60
    print(days,'дн', hours,'час', minutes, 'мин', seconds, 'сек')
    # При больших значениях секунд происходит смещение (скорее всего из-за того что: в месяце 30,44 дня, а в году 365,24 дня.)
if seconds >= 60*60*24*7 and seconds < 60*60*24*7*365:
    days = days % 30
    hours = hours % 24
    minutes = minutes % 60
    seconds = seconds % 60
    print(month, 'мес', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
if seconds >= 60*60*24*7*365:
    month = month % 12
    days = days % 30
    hours = hours % 24
    minutes = minutes % 60
    seconds = seconds % 60
    print(years, 'год', month, 'мес', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
# Подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?
#
# В список можно уложить значения минут, часов, дней и т.д. Тогда код будет меньше строк на 10. Выбоку делать из списка.
