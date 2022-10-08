### Map es una función de order superior
# Vamos a resolver un problema de dos maneras distintas.
# Queremos obtener los cuadrados de los elementos de my_list.
my_list = [1, 2, 3, 4, 5]

# Primero con list_comprehensions.
# squares_lc = [i**2 for i in my_list]
# print(squares_lc)

# Ahora con map.
squares_map = list(map(lambda x: x**2, my_list))
print(squares_map)