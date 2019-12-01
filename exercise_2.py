'''
    Exercício 2 da lista
'''

import re

def main():
    acceleration = ask_for_float_number_from_input('Insert the car initial acceleration (m/s²): ')
    speed_before_slowdown = ask_for_float_number_from_input('Insert the final speed before the slowdown (m/s): ')
    slowdown = ask_for_float_number_from_input('Insert the car slowdown (m/s²): ')

    if (slowdown > 0):
        slowdown = slowdown * -1

    time_to_get_speed = calc_time_to_get_speed(speed_before_slowdown, 0, acceleration)
    distance_to_get_speed = calc_distance(0, 0, time_to_get_speed, acceleration)
    time_to_slowdown = calc_time_to_get_speed(0, speed_before_slowdown, slowdown)
    distance_until_stop = calc_distance(distance_to_get_speed, speed_before_slowdown, time_to_slowdown, slowdown)

    print('Time between departure and stop: ' + str(time_to_get_speed + time_to_slowdown))
    print('Distance traveled: ' + str(distance_to_get_speed + distance_until_stop))

def has_only_numbers(input_string):
    return bool(re.search(r'-?\d+', input_string))


def ask_for_float_number_from_input(message):
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


def calc_time_to_get_speed(final_speed, initial_speed, acceleration):
    return ((final_speed - initial_speed) / acceleration)


def calc_distance(initial_distance, initial_speed, time, acceleration):
    return round((initial_distance + (initial_speed * time) + ((acceleration * pow(time, 2)) / 2)))


if __name__ == '__main__':
    main()