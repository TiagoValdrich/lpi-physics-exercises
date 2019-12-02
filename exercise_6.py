import re

def main():

    numb = ask_for_int_number_on_input('Insert a number of wagons')

    wags = []
    total_wd = 0

    for i in range( 0 , numb ):
        wags.insert(i , ask_for_float_number_on_input('Insert the weight of the wagon ' + str(i+1) + ':' ) )
        total_wd += wags[i]



    force =  ask_for_float_number_on_input('Insert a force for locomotive')

    acel =  calc_acel( force , total_wd )

    # Aceleration
    print('Aceleration value : ' + str(acel))

    f = force
    for i in range( 0 , numb ):
        wag = wags[i]
        t = calc_tension( wag , acel , f )
        if( t < 0 ):
            t = t * -1
        if( t == 0 ):
            t = calc_last_ten( wag , acel )

        f = t

        # Wag Tension
        print('Wagon tension ' + str(i+1) + ' : ' + str(f) )



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
        value1 = 0

        while True:
            print(message)
            value1 = input()

            if has_only_numbers(value1):
                value1 = int(value1)

            if (type(value1) is int) and (value1 > 0):
                break

        return value1
    except:
        print('Invalid value inserted. Please, insert only numbers.')
        exit()



def calc_acel( F , m ):
    return  F / m


def calc_tension( w , a , f ):
    return ( w * a ) - f


def calc_last_ten( w , a ):
    return w * a


if __name__ == '__main__':
    main()