import math
import re

def main():
    height = ask_for_float_number_on_input('Insert the height which the plane is (m/s): ')

    angle = ask_for_float_number_on_input('Insert airplane diving angle: ')

    time = ask_for_float_number_on_input('Insert the time for projectile impact (seconds): ')

    calc_plane_angle = calc_sen(90 - angle)
    plane_velocity = calc_plane_velocity(0, height, 9.8, time, calc_plane_angle)

    if plane_velocity < 0:
        plane_velocity = plane_velocity * -1

    horiz_angle = calc_cos(90 - angle)
    horiz_dist = calc_horiz_dist(plane_velocity , horiz_angle , time)

    if horiz_dist < 0:
        horiz_dist = horiz_dist * -1

    # PRINTs
    print('The plane velocity is %.2f m/s' % plane_velocity)
    print('The plane horizontal distance is %.2f meters' % horiz_dist)


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


def calc_plane_velocity(iniciatl_height, height, g, time, angle):
    return ((iniciatl_height - height ) + ( 1 / 2 * g * time ** 2 )) / (angle * time)


def calc_sen(angle):
    return math.sin(math.radians( angle ) )


def calc_cos(angle):
    return math.cos(math.radians(angle))


def calc_horiz_dist(velocity , angle , time):
    return (velocity * angle * time)


if __name__ == '__main__':
    main()