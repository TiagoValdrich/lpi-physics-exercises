import math
import re

def main():

    weight = ask_for_float_number_on_input('Insert the maximum weight ')

    vel = ask_for_float_number_on_input('Insert the maximum velocity ')

    inc = ask_for_float_number_on_input('Insert tilt angle in degrees')

    angle = calc_angle( 3.14159265359 , inc )
    sin = calc_sin(angle)

    calc_dist = calc_distance(weight , 9.807 , vel , sin)


    print('Track size : ' + str(calc_dist) + ' m')


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


def calc_angle( p ,ang ):
    return (p * ang) / 180


def calc_sin(a):
    return math.sin(math.radians(a))


def calc_distance(w , g , v , a):
    return ((w/g) * -(v**2))/(w * a) * -1


if __name__ == '__main__':
    main()
