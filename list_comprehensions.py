"""
    Dos formas de escribir un mismo código,
    primero escribirlo de manera normal en
    cuatro lineas, mientras que con la com-
    prehension de lista se puede escribir
    en una sola linea. Nótese que tiene la
    forma:
    [element for element in iterable if condition]
"""
def run():
    # squares = []
    # for i in range(1, 101):
    #     if i%3 !=0:
    #         squares.append(i**2)
    
    squares = [i**2 for i in range(1,101) if i%3 != 0]

    print(squares)


if __name__ == '__main__':
    run()