# Работа с ошибками

#try:
#    x = int(input())
#    x += 5
#    print(x)
#except ValueError:
#    print('Введите число пожалуйста!')

# Work_2

#x = 0

#while x == 0:
#    try:
#        x = int(input('Введите число: '))
#        x += 5
#        print(x)
#    except ValueError:
#        print('Введите лучше число!')

# Work_3

#try:
#    x = 5 / 0
#    x = int(input())
#except ZeroDivisionError:
#    print('Число не делится на ноль!')
#except ValueError:
#    print('Что-то пошло не так')
#else:
#    print('Else')
#finally:
#    print('Finally')