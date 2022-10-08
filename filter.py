### Filter es una función de order superior
# Vamos a resolver un problema de dos maneras distintas.
# Queremos obtener los valores impares de muy_list.
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

# Primero con list comprehensions.
# odd_lc = [i for i in my_list if i%2 != 0]
# print(odd_lc)

# Ahora lo resolvemos con filter.
odd_filter = list(filter(lambda x: x%2 != 0, my_list))
print(odd_filter)
