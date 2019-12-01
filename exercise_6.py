def main():
    print('Insert a force for locomotive')
    force = float(input())

    print('Insert a number of wagons')
    wag = int(input())

    print('Insert their weights')
    wd = 0
    weights = []
    for ii in range(0, wag):
        w =  float(input())
        weights.insert(ii , w)
        wd += weights[ii]


    acel = calc_acel( force , wd )
    print('Aceleration is : ' + str( acel ) )

    # First wagon
    wag1_ten = calc_wag1( weights[0] , acel , force )


    # Last wagon
    length = len(weights)
    last_elem_wd = weights[ length - 1 ]

    las_wag_ten = calc_las_wag( last_elem_wd , acel )


    # Wag
    random_wag_ten = calc_random_wag_ten()


    # PRINTs
    print('wag1 tension ' + str(-wag1_ten))

    print('last wag tension ' + str(las_wag_ten))



def calc_acel( F , m ):
    return  F / m


def calc_wag1( m , ac , F ):
    return ( m * ac ) - F


def calc_las_wag( m , ac ):
    return m * ac


def calc_random_wag_ten():
    return

if __name__ == '__main__':
    main()
