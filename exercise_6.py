def main():
    print('Insert a number of wagons')
    numb = int(input())

    wags = []
    total_wd = 0

    for i in range( 0 , numb ):
        print('Insert the weight of the wagon ' + str(i+1) + ':' )
        wags.insert(i , float(input()))
        total_wd += wags[i]


    print('Insert a force for locomotive')
    force = float(input())

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


def calc_acel( F , m ):
    return  F / m


def calc_tension( w , a , f ):
    return ( w * a ) - f


def calc_last_ten( w , a ):
    return w * a


if __name__ == '__main__':
    main()