import re

def main():

    numb = ask_for_int_number_on_input('Insert a number of wagons (except the locomotive): ')

    wags = []
    total_wd = 0

    for i in range(numb):
        wags.insert(i, ask_for_float_number_on_input('Insert the weight of the wagon {} (kg):'.format(i + 1)))
        total_wd += wags[i]


    locomotive_force = ask_for_float_number_on_input('Insert a force for the first locomotive (N): ')
    acel = calc_acel(locomotive_force, total_wd)

    # Aceleration
    print('Aceleration value %.2f m/s²' % acel)

    last_tension = 0

    for i in range(numb):
        tension = 0
        # Check if is the first wagon
        if i == 0:
            last_tension = tension = calc_tension(wags[i], acel, 0)
        # Check if wagon is on the middle
        elif wags[i - 1] and i != (numb - 1) and wags[i + 1]:
            tension = calc_tension(wags[i], acel, last_tension)
            last_tension = tension
        # If there is not a wagon on the next position, only on before, we are on the locomotive
        # which we already have it's force
        else:
            tension = locomotive_force
        # Wag Tension
        print('Wagon {a} have tension: {b:5.2f}N'.format(a=(i+1), b=tension))


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


def ask_for_int_number_on_input(message):
    try:
        value = 0

        while True:
            print(message)
            value = input()

            if has_only_numbers(value):
                value = int(value)

            if (type(value) is int) and (value > 0):
                break

        return value
    except:
        print('Invalid value inserted. Please, insert only numbers.')
        exit()



def calc_acel(F, m):
    return  F / m


def calc_tension(w, a, f):
    return (w * a) + f


def calc_last_ten(w, a):
    return w * a


if __name__ == '__main__':
    main()