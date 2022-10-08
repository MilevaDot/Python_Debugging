def run():
    my_dict = {number: round(number**(1/2), 3) for number in range(1, 1001)}
    print(my_dict)


if __name__ == '__main__':
    run()