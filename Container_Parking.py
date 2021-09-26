#!/usr/bin/env python3

import sys
from Methods import (ParkingLot, create_parking_lot, park, leave_slot,reg_number_by_age, slot_by_car_number, slot_num__by_age)

def executearg(parkingLot, arg):
    CREATE_PARKING_LOT = 'Create_parking_lot'
    PARK = 'Park'    #'^.*r*.[a-zA-Z]+*.[a-zA-Z]+.*$'
    LEAVE_SLOT = 'Leave'
    SLOT_FOR_REG_NUMBER = 'Slot_number_for_car_with_number'
    REG_NUMBER_BY_AGE = 'Vehicle_registration_number_for_driver_of_age'
    SLOT_NUMBER_BY_AGE = 'Slot_numbers_for_driver_of_age'
    
    if arg[0] == CREATE_PARKING_LOT:
        return create_parking_lot(arg[1])
    elif arg[0] == PARK:
        print (park(parkingLot, arg[1], arg[2],arg[3]))
    elif arg[0] == LEAVE_SLOT:
        print(leave_slot(parkingLot, arg[1]))
    elif arg[0] == SLOT_FOR_REG_NUMBER:
        print(slot_by_car_number(parkingLot, arg[1]).rstrip(', '))
    elif arg[0] == REG_NUMBER_BY_AGE:
        print(reg_number_by_age(parkingLot, arg[1]).rstrip(', '))
    elif arg[0] == SLOT_NUMBER_BY_AGE:
        print(slot_num__by_age(parkingLot, arg[1]).rstrip(', '))
    else:
        print('Invalid arg ')
    return parkingLot

def Parse_file(parkingLot, fileName):
    try:
        with open(fileName) as file:
            args = file.readlines()
            for arg in args:
                parkingLot = executearg(
                    parkingLot, arg.replace('\n', '').split())
    except Exception as e:
        print(e)
def interactive_Mode(parkingLot):
    try:
        arg = input().split()
        while arg[0] != EXIT:
            parkingLot = executearg(parkingLot, arg)
            arg = input().split()
    except Exception as e:
        print(e)


def main():
    parkingLot = None
    if len(sys.argv) > 1:
        Parse_file(parkingLot, sys.argv[1])
    else:
        interactive_Mode(parkingLot)
        


if __name__ == '__main__':
    main()
