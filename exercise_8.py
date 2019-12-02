'''
    Exercício 8 da lista
'''

import re


def main():
    ELETROSTATIC_CONSTANT = 8.99 * pow(10, 9)

    resultant_eletrical_potencial = 0.0

    number_of_charges = ask_for_int_number_on_input('Insert the number of charges that you want to calculate the resultant eletric field: ')

    for num in range(number_of_charges):
        print('\nCharge {}: '.format(num + 1))
        charge_value = ask_for_float_number_on_input('Insert the charge value in uC: ', True)
        distance = ask_for_float_number_on_input('Insert the charge distance from point P in meters: ')
        eletrical_potencial = calc_eletric_field(ELETROSTATIC_CONSTANT, charge_value, distance)
        resultant_eletrical_potencial = resultant_eletrical_potencial + eletrical_potencial

    print('The resultant eletrical potencial is %.2f V/M' % resultant_eletrical_potencial)


def has_only_numbers(input_string):
    return bool(re.search(r'-?\d+', input_string))


def ask_for_int_number_on_input(message):
    try:
        value = 0

        while True:
            print(message)
            value = input()

            if has_only_numbers(value):
                value = int(value)

            if (type(value) is int) and (value > 0):
                break

        return value
    except:
        print('Invalid value inserted. Please, insert only numbers.')
        exit()


def ask_for_float_number_on_input(message, accept_negative=False):
    try:
        value = 0.0

        while True:
            print(message)
            value = input()

            if has_only_numbers(value):
                value = float(value)

            if (type(value) is float) and (value > 0 or accept_negative):
                break

        return value
    except:
        print('Invalid value inserted. Please, insert only numbers.')
        exit()


def calc_eletric_field(constant, charge, distance):
    return ((constant * charge) / distance)


if __name__ == '__main__':
    main()
