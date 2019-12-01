'''
    Exercício 3 da lista
'''

import re

def main():
    GRAVITY = 9.8

    distance = ask_for_float_number_on_input('Insert the initial distance that is beeing dropped the object (m): ')
    initial_speed = ask_for_float_number_on_input('Insert the initial launch speed (m/s): ')

    final_speed = calc_final_speed_before_reach_the_ground(initial_speed, GRAVITY, distance)
    time = calc_time_to_reach_the_ground(initial_speed, final_speed, GRAVITY)

    print('\nThe object hits the ground in %.2f seconds' % time)
    print('The object speed before reach the ground is %.2f m/s' % final_speed)


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


def calc_final_speed_before_reach_the_ground(initial_speed, acceleration, distance):
    return (pow(initial_speed, 2) + 2 * acceleration * distance) ** (1/2)


def calc_time_to_reach_the_ground(initial_speed, final_speed, acceleration):
    return ((final_speed - initial_speed) / acceleration)


if __name__ == '__main__':
    main()