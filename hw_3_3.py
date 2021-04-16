def sum_2_max_object (a, b, c):
    max_numbers = [a,b,c]
    min_number = min(a,b,c)
    max_numbers.pop(max_numbers.index(min_number))
    return max_numbers

print(sum_2_max_object(5,-30,10))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.