import math
import re

def main():
    GRAVITY = 9.8

    weight = ask_for_float_number_on_input('Insert the maximum weight (kg):')
    speed = ask_for_float_number_on_input('Insert the maximum velocity (km/h): ')
    speed = speed / 3.6
    angle = ask_for_float_number_on_input('Insert tilt angle in degrees: ')

    ramp_height = calc_ramp_height(speed, GRAVITY)
    ramp_length = calc_ramp_length(ramp_height, angle)

    print('Track size : %.2fm' % ramp_length)


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


def has_only_numbers(input_string):
    return bool(re.search(r'-?\d+', input_string))


def calc_sin(a):
    return math.sin(math.radians(a))


def calc_ramp_length(height, angle):
    return (height / calc_sin(angle))


def calc_ramp_height(speed, gravity):
    return ((pow(speed, 2)) / (2 * gravity))


if __name__ == '__main__':
    main()
