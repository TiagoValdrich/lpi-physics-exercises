def main():
    SLOWDOWN = -5

    print('Insert the initial speed: ')
    initial_speed = float(input())

    time = calc_slowdown_time(0, initial_speed, SLOWDOWN)
    distance = calc_distance(0, initial_speed, time, SLOWDOWN)

    print('Time spent ' + str(time))
    print('Distance ' + str(distance))


def calc_slowdown_time(final_speed, initial_speed, acceleration):
    return ((final_speed - initial_speed) / acceleration)


def calc_distance(initial_distance, initial_speed, time, acceleration):
    return round((initial_distance + (initial_speed * time) + ((acceleration * pow(time, 2)) / 2)))


if __name__ == '__main__':
    main()