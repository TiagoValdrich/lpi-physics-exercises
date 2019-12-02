'''
    Exercício 7 da lista
'''

import re

def main():
    ELETROSTATIC_CONSTANT = 8.99 * pow(10, 9)

    static_charge_Q = ask_for_float_number_on_input('Insert the value of Q in uC: ')
    static_charge_Q = static_charge_Q * pow(10, -6)
    distance_1 = ask_for_float_number_on_input('Insert the first distance (A) in meters: ')
    distance_2 = ask_for_float_number_on_input('Insert the second distance (B) in meters: ')
    charge_q = ask_for_float_number_on_input('Insert the value of q in uC: ')

    eletric_field_A = calc_eletric_field(ELETROSTATIC_CONSTANT, static_charge_Q, distance_1)
    eletric_field_B = calc_eletric_field(ELETROSTATIC_CONSTANT, static_charge_Q, distance_2)

    work_done = calc_work_done(charge_q, eletric_field_A, eletric_field_B)
    print('\n Work done to move charge q from A to B: %.2f Joules' % work_done)


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


def calc_eletric_field(constant, charge, distance):
    return ((constant * charge) / distance)


def calc_work_done(charge, initial_eletric_field, final_eletric_field):
    return (charge * (initial_eletric_field - final_eletric_field))


if __name__ == '__main__':
    main()