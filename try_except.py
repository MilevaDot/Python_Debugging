def palindrome(string):
    return string == string[::-1]


try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings.")