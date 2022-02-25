#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on February 2022
# This is the Perimeter and Area for a circle with radius = 15 mm

import math


def main():
    # this function calculates the area and perimeter of a circle with radius = 15 mm
    print("If a Circle has a radius of 15 mm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 15**2))
    print("")
    print("Perimeter is {} mm.".format(2 * math.pi * 15))


if __name__ == "__main__":
    main()
