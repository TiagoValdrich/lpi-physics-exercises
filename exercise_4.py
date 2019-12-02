import math


def main():
    print('Insert a height')
    height = float(input())

    print('Insert an angle')
    angle = float(input())

    print('Insert the for projectile impact')
    time = float(input())

    calc_plane_angle = calc_sen( 90 - angle )
    plane_velocity = calc_plane_velocity( 0, height, 9.8, time, calc_plane_angle )
    horiz_angle = calc_cos( 90 - angle )
    horiz_dist = calc_horiz_dist( plane_velocity , horiz_angle , time )



    # PRINTs
    print('The plane velocity is :' + str( -plane_velocity ) )

    print('The plane horizontal distance is :' + str( -horiz_dist ) )


def calc_plane_velocity(iniciatl_height, height, g, time, angle):
    return ( ( iniciatl_height - height ) + ( 1 / 2 * g * time ** 2 ) ) / ( angle * time )


def calc_sen( angle ):
    return math.sin( math.radians( angle ) )


def calc_cos( angle ):
    return math.cos( math.radians( angle ) )


def calc_horiz_dist( velocity , angle , time ):
    return ( velocity * angle * time )


if __name__ == '__main__':
    main()