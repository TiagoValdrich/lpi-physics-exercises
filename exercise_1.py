'''
    Exercício 1 da lista.
'''

import re

def main():
    SLOWDOWN = -5

    try:
        while True:
            print('Insert the initial speed: ')
            initial_speed = input()

            if has_only_numbers(initial_speed):
                initial_speed = float(initial_speed)

            if (type(initial_speed) is float) and (initial_speed > 0):
                break
    except:
        print('Invalid value inserted. Please, insert only numbers.')
        exit()

    time = calc_slowdown_time(0, initial_speed, SLOWDOWN)
    distance = calc_distance(0, initial_speed, time, SLOWDOWN)

    print('\nTime spent to stop the car: %.2f seconds' % time)
    print('Travelled distance: %.2f meters' % distance)

def has_only_numbers(input_string):
    return bool(re.search(r'-?\d+', input_string))


def calc_slowdown_time(final_speed, initial_speed, acceleration):
    return ((final_speed - initial_speed) / acceleration)


def calc_distance(initial_distance, initial_speed, time, acceleration):
    return ((initial_distance + (initial_speed * time) + ((acceleration * pow(time, 2)) / 2)))


if __name__ == '__main__':
    main()