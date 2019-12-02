'''
    Exercício 7 da lista
'''

import re

def main():
    pass


def has_only_numbers(input_string):
    return bool(re.search(r'-?\d+', input_string))


def ask_for_float_number_on_input(message):
    try:
        value = 0.0
        
        while True:
            print(message)
            value = input()

            if has_only_numbers(value):
                value = float(value)

            if (type(value) is float) and (value > 0):
                break

        return value
    except:
        print('Invalid value inserted. Please, insert only numbers.')
        exit()


if __name__ == '__main__':
    main()