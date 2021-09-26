class ParkingLot:
    #Parking Class to define the size of the parking lot and count for the number of parked vehicles
    def __init__(self, size):
        self.parkedVehicles = 0                                                 #counter for parked cars
        self.slots = dict.fromkeys([i for i in range(1,int(size)+1)])          # declaring a dictionary of slots size given by 

    
    def cnt_parked_vehicles(self):
        return self.parkedVehicles                                              #get count of cars parked in the parking lot

    def get_slots(self):
        return self.slots                                                       #set number of cars parked in the lot (assign slots)

    def set_slots(self, slot, value):
        self.slots[slot] = value                                                # retrieve slots


class Vehicle:
#class Vehicle to initialize the vehicle details (registration_number,driver_age)
    def __init__(self, registrationNumber, random, age):
        self.carRegistrationNumber = registrationNumber             #initialising reg_no
        self.random = random                                        # to handle dummy string driver_age
        self.driv_age = age                                         #initialising age
        self.carSlot = None
        
    def get_age(self):
        return self.driv_age                                        # returns driver_age

    def get_registration_number(self):
        return self.carRegistrationNumber                           # returns car's registration number
    
    def set_slot(self, slot):    
        self.carSlot = slot                                         #setting the slot for parked cars

    def get_slot(self):                                             #returns slots of the cars
        return self.carSlot               

def create_parking_lot(size):                                       # create parking lot of the given size
    lot = ParkingLot(int(size))
    print('Created parking of {} slots '.format(size) )             # initiates ParkingLot class constructor to create a dictionary of the given size
    return lot


# function to park a car
def park(lot, registrationNumber,random, age):
    
    result = ''
    if lot:
        if len(lot.get_slots()) <= lot.cnt_parked_vehicles():
            result = 'Cannot park a car since parking lot is full'
            
        else:
            parkingSlot = lot.get_slots()                               # creating an instance of the dictionary     
            for slot in parkingSlot.keys():                             #iterating through the keys of dict
                if parkingSlot[slot] is None:                           # if particular slot is available
                    car = Vehicle(registrationNumber,random, age)       # creating an instance of the class car by initializing the command(KB_1234,driver_age,21)
                    lot.set_slots(slot, car)                            # ASSIGNING THE SLOTS                
                    car.set_slot(slot)               
                    lot.parkedVehicles += 1                             # incrementing parked vehicles
                    result = 'Vehicle with vehicle registration number {} has been parked at slot number {} ' .format(registrationNumber,str(slot))
                    break
    else:
        result = 'Parking lot has not been allocated a particular size'
    return result


#function to leave a particular slot
def leave_slot(lot, inputSlot):

    result = ''
    res=''
    age=''

    parkingSlot = lot.get_slots()  
    for parkedCar in parkingSlot.values():
        if parkedCar is not None:
            if parkedCar.get_slot()==int(inputSlot):
                res+=parkedCar.get_registration_number()+', '
                age+=parkedCar.get_age()
                      
    if lot:
        if not lot.cnt_parked_vehicles():                                                   #if no parked vehicles available lot is empty
            result = 'No car is available at the particular slot since parking lot is empty'
        elif int(inputSlot) >= 1 and int(inputSlot) <= len(lot.get_slots()):                             
            parkingSlot = lot.get_slots()                                 # creating an instance of the dictionary 
            value = parkingSlot.get(int(inputSlot), None)                  # to fetch the slot inputted by the user
            if value is not None:                                                 
                lot.set_slots(int(inputSlot), None)                                         # set the slot i.e. key 's value in dictionary to None
                lot.parkedVehicles -= 1                                                     # decrementing parked vehicles counter
                result = 'Slot number {} vacated the car with vehicle registration number {} left the space, the driver of the car was of age {}' .format(inputSlot,res,age) 
            else:
                result = 'No available car at Slot number ' + inputSlot
        else:
            result = 'Cannot exit slot number: ' + inputSlot + ' since it\'s not available!'
    else:
        result = 'Parking lot has not been allocated a particular size'
    return result



# function to retrieve car registration number from diver_age
def reg_number_by_age(lot, inputAge):          
    res = ''
    if lot:
        if not lot.cnt_parked_vehicles():
            res = 'No car is available at the particular slot since parking lot is empty'
        else:
            ptr = False
            parkingSlot = lot.get_slots()                                                       # creating an instance of the dictionary 
            for parkedVehicle in parkingSlot.values():                                          # iterating through the (values) of the dict
                if parkedVehicle is not None:
                                                                                                #print(parkedVehicle.get_age(),parkedVehicle.get_registration_number(),"parkedVehicle")
                    if parkedVehicle.get_age() == inputAge:                                     # invoking method get_age from vehicle class to check any such existing age 
                        ptr = True
                        res += parkedVehicle.get_registration_number() + ', '
            if not ptr:
                res = ' '
    else:
        res = 'Parking lot has not been allocated a particular size'
    return res


 # function to retrieve slot number from car's registration number
def slot_by_car_number(parkingLot, number):
    result = ''
    if parkingLot:
        if not parkingLot.cnt_parked_vehicles():
            result = 'No car is available at the particular slot since parking lot is empty'
        else:
            flag = False
            parkingSlot = parkingLot.get_slots()                                                # creating an instance of the dictionary 
            for parkedCar in parkingSlot.values():                                              # iterating through the (values) of the dict
                if parkedCar is not None:
                    if parkedCar.get_registration_number() == number:                           # invoking method get_registration_number from vehicle class to check any such existing value

                        flag = True
                        result += str(parkedCar.get_slot()) + ', '
                        # assuming that for the cars, there is one and only one registration number exits
                        break
            if not flag:
                result = 'no such car parked with registration number {}' .format(number)
    else:
        result = 'Parking lot has not been allocated a particular size'
    return result



 # function to retrieve  slot number from driver_age
def slot_num__by_age(lot, inputage):                                                           
    result = ''
    if lot:
        if not lot.cnt_parked_vehicles():
            result = 'No car is available at the particular slot since parking lot is empty '
        else:
            ptr = False
            parkingSlot = lot.get_slots()                                                       # creating an instance of the dictionary 
            for parkedVehicle in parkingSlot.values():                                          # iterating through the (values) of the dict
                if parkedVehicle is not None:
                    if parkedVehicle.get_age() == inputage:                                     # invoking method get_age from vehicle class to check any such existing value
                        ptr = True
                        result += str(parkedVehicle.get_slot()) + ',  ' 
            if not ptr:
                result = 'No such car parked with driver\'s age {}'.format(inputage)
    else:
        result = 'Parking lot has not been allocated a particular size'
    return result


