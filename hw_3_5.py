def sum_numbers(a = input('Введите числа: ')):
    user_input = a.split(' ')
    b = len(user_input)
    while b != 0:
        c = user_input.pop(0)
        c = int(c)
        c += c
        b -= 1
    return c

print (sum_numbers())
# Долго мучился, не разобрался

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
