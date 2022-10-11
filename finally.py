# finally sirve para cerrar un archivo dentro de python, cerrar una conexión a una base de datos o liberar recursos externos. Generalmente finally no se usa, pero existe y debemos conocerlo.

try:
    f = open('archivo.txt')
finally:
    f.close()

# finally hace algo ya sea que hay o no un error.