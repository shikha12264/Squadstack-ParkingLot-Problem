# Squadstack_Problem
# Repl link to the project : https://replit.com/@shikha12264/Squadstack-ParkingLot-Problem-2#.replit
# Problem Statement :
We own a parking lot that can hold up to ‘n’ cars at any given point in time. 

Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

Due to government regulation, the system should provide us with the ability to find out:-
#### Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
#### Slot number in which a car with a given vehicle registration plate is parked. 
#### Slot numbers of all slots where cars of drivers of a particular age are parked.

We get the input by reading input.txt directly (you’ll have to create it in your environment) .The file will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.
 
# OUTPUT
## File Mode: 
In order to run the file : 
#### run save_output.py file 

This would create an output.txt file with all the commands executed from the input file
![image](https://user-images.githubusercontent.com/64529469/134845473-293cc233-7c33-4f7a-b423-57bae198d26a.png)

## Interactive Mode: 
#### Run Command: py ./Container_Parking.py input.txt

This would print all the executed commands from the input file.
![image](https://user-images.githubusercontent.com/64529469/134845653-05069584-8477-46e2-a707-20621b04949b.png)

## Command Mode

#### Run Command: py ./Container_Parking.py
This would prompt the user to enter the commands & executes accordingly
![image](https://user-images.githubusercontent.com/64529469/134845925-f195e18d-6664-4638-aadf-02129a986d88.png)
