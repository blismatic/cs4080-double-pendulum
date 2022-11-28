import argparse
from datetime import datetime


def generate_file_name():
    # Helper function used when saving the simulation to a file
    x = datetime.now()
    return x.strftime('%b %d %Y %H-%M-%S')


def main():
    DEFAULT_LENGTH = 14
    DEFAULT_MASS = 20
    DEFAULT_ANGLE = 0

    # Argument parsing... allows user to specify the length, mass, and angle
    # of each pendulum
    parser = argparse.ArgumentParser(
        description='Visualize a double pendulum simulation.'
    )

    parser.add_argument('-p1_l', '--p1_length', type=int,
                        default=DEFAULT_LENGTH,
                        help='length of pendulum 1')
    parser.add_argument('-p1_m', '--p1_mass', type=int,
                        default=DEFAULT_MASS,
                        help='mass of pendulum 1')
    parser.add_argument('-p1_a', '--p1_angle', type=int,
                        default=DEFAULT_ANGLE,
                        help='starting angle of pendulum 1 (degrees)')
    parser.add_argument('-p2_l', '--p2_length', type=int,
                        default=DEFAULT_LENGTH,
                        help='length of pendulum 2')
    parser.add_argument('-p2_m', '--p2_mass', type=int,
                        default=DEFAULT_MASS,
                        help='mass of pendulum 2')
    parser.add_argument('-p2_a', '--p2_angle', type=int,
                        default=DEFAULT_ANGLE,
                        help='starting angle of pendulum 2 (degrees)')

    parser.add_argument('-o', '--output_file',
                        default=generate_file_name(),
                        help='name of file to be saved')

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
