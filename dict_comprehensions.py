def run():
    # dict_number = {}
    # for i in range(1,101):
    #     if i %3 != 0:
    #         dict_number[i] = i**3

    dict_number = {i: i**3 for i in range(1,101) if i %3 !=0}

    print(dict_number)


if __name__ == '__main__':
    run()