import math


def main():
    print('Insert the maximum weight ')
    weight = float(input())

    print('Insert the maximum velocity ')
    vel = float(input())

    print('Insert the inclination ')
    inc = float(input())

    kin_energy = calc_kin_ener(weight, vel)

    h = calc_sen(inc)
    pot_energy = calc_pot_ener(weight, 9.8, h)

    ramp_weight = calc_ramp_weight()


def calc_ramp_weight():
    return


def calc_sen(angle):
    return math.sin(math.radians(angle))


def calc_kin_ener(wd, vel):
    return (wd * (vel ** 2)) / 2


def calc_pot_ener(wd, g, h):
    return (wd * g * h)


if __name__ == '__main__':
    main()
