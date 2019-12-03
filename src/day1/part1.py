import math
import sys


def calculate_required_fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Specify the name of the input file.')
        sys.exit(1)

    spacecraft_fuel_requirements = []
    with open(file_name) as file:
        for line in file:
            spacecraft_fuel_requirements.append(
                calculate_required_fuel(int(line))
            )

    print(sum(spacecraft_fuel_requirements))
