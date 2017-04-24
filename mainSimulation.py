# !/usr/bin/python
import random
import sys
from planePosition import PlanePosition
import time

mu = 0
sigma = 1

class Simulation:
    def simulate(self):
        planePosition = PlanePosition()
        print(30 * '-')
        print("   M A I N - M E N U")
        print(30 * '-')
        print("1. Start program")
        print("2. Quit")
        print(30 * '-')

        is_valid = 0
        while not is_valid:
            try:
                choice = int(input('Enter your choice [1-2] : '))
                is_valid = 1  ## set it to 1 to validate input and to terminate the while..not loop
            except ValueError as e:
                print("'%s' is not a valid integer." % e.args[0].split(": ")[1])

            ### Take action as per selected menu-option ###
            if choice == 1:
                print("Starting simulator...")
                while True:
                    tilt_corr = random.gauss(mu, sigma)

                    planePosition.tilt_correction(tilt_corr)

                    planePosition.correction_flight()
                    planePosition.show_current_position()
                    to_stop = input("Do you want to brake? y-true \n\n")
                    if to_stop == "y":
                        sys.exit(0)
                    time.sleep(1)

            elif choice == 2:
                print("Bye bye...")
                sys.exit(0)
            else:
                print("Invalid number. Byebye...")


if __name__ == "__main__":
    simulation = Simulation()
    simulation.simulate()
