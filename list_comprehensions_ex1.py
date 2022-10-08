def run():
    number_list = [
            number for number in range(1, 100000) if number%36 == 0
        ]
    print(number_list)


if __name__ == '__main__':
    run()
