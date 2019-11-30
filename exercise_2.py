def main():
    print('Insert an acceleration: ')
    acceleration = float(input())
    print('Insert the final speed before the slowdown: ')
    speed_before_slowdown = float(input())
    print('Insert the slowdown: ')
    slowdown = float(input()) * -1

    time_to_get_speed = calc_time_to_get_speed(speed_before_slowdown, 0, acceleration)
    distance_to_get_speed = calc_distance(0, 0, time_to_get_speed, acceleration)
    time_to_slowdown = calc_time_to_get_speed(0, speed_before_slowdown, slowdown)
    distance_until_stop = calc_distance(distance_to_get_speed, speed_before_slowdown, time_to_slowdown, slowdown)

    print('Time between departure and stop: ' + str(time_to_get_speed + time_to_slowdown))
    print('Distance traveled: ' + str(distance_to_get_speed + distance_until_stop))


def calc_time_to_get_speed(final_speed, initial_speed, acceleration):
    return ((final_speed - initial_speed) / acceleration)


def calc_distance(initial_distance, initial_speed, time, acceleration):
    return round((initial_distance + (initial_speed * time) + ((acceleration * pow(time, 2)) / 2)))


if __name__ == '__main__':
    main()