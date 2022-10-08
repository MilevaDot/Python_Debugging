"""
    Dos formas de escribir un código, con funciones lambda
    y sin funciones lambda.
"""
### Primera Forma, sin Lambda:

# def palindrome(string):
#     return string == string[::-1]


# def run():
#     palindrome('anitalavalatina')


### Segunda forma, con Lambda
palindrome = lambda string: string ==string[::-1]


def run():
    print(palindrome('anitalavalatina'))


# Esto siempre va--
if __name__ == '__main__':
    run()