import sys
from dataclasses import dataclass
import stack
import queue
import boardingzone

"""
CSCI-603 Lab 6: AiRIT

This is a program that implements a airport functions that performs some functions

It has multiple classes into different modules named stacks, queues, linkednode and boardingzone
It makes use of multiple data structure to line up passengers at the gate and take the
passengers in air craft and unload the passengers

author: Kapil Sharma ks4643
"""


@dataclass
class Passenger:
    """
    This is a passenger data class that stores data about the passenger
    such as name, ticket number and carry on baggage
    It also has __str__ function to display the data
    """
    name: str
    ticket_number: int
    is_cary_on: str

    def __str__(self):
        return self.name + ", ticket: " + str(self.ticket_number) + ", carry_on: " + str(self.is_cary_on)


def load_to_aircraft(main_gate, airport_capacity, boarding_zone, number_of_flight) -> int:
    """
    This function loads to aircraft and stores the data into a stack and then dequeue after adding
    everything it dequeues person from the main gate so that the loops ends when the main gate
    length is zero it gets out of the loop

    :param main_gate: queue with all the passengers
    :param airport_capacity: maximum capacity of aircraft
    :param boarding_zone: class with four zones
    :param number_of_flight: total number of flight taken
    :return: number of flights taken
    """
    air_stack = stack.Stack()
    while main_gate.length() >= 0:
        if air_stack.length() == airport_capacity or main_gate.length() == 0:
            print("Passengers are boarding the aircraft...")
            print('\t', air_stack.reverse())
            flight_simulation(air_stack, main_gate.length())
            number_of_flight += 1
            if main_gate.length() == 0:
                break
        if boarding_zone._zone4.length() > 0:
            air_stack.push(boarding_zone._zone4.peek())
            boarding_zone._zone4.dequeue()
        elif boarding_zone._zone3.length() > 0:
            air_stack.push(boarding_zone._zone3.peek())
            boarding_zone._zone3.dequeue()
        elif boarding_zone._zone2.length() > 0:
            air_stack.push(boarding_zone._zone2.peek())
            boarding_zone._zone2.dequeue()
        elif boarding_zone._zone1.length() > 0:
            air_stack.push(boarding_zone._zone1.peek())
            boarding_zone._zone1.dequeue()
        if main_gate.length() > 0:
            main_gate.dequeue()
    return number_of_flight


def run_simulation(passengers, gate_capacity, airport_capacity) -> int:
    """
    This executes the whole execution of the airport functionalities

    First it runs the loop over the length of passengers and stores the
    passengers in four queues based on zones and also maintain a
    main gate queue

    Then, based on the airport capacity the second loop runs and
    stores the data into the stack based on their boarding zone priority


    :param passengers: total passengers inside a list
    :param gate_capacity: maximum capacity of gate
    :param airport_capacity: maximum capacity of aircraft
    :return: returns integer of number of flights taken
    """
    passenger_number = 0
    number_of_flight = 0
    while passenger_number < len(passengers):
        """
        This is the main loop that runs over the length of passengers
        """
        main_gate = queue.Queue()
        length_of_gate = gate_capacity
        boarding_zone = boardingzone.BoardingZone()
        print("Passengers are lining up at the gate...")
        while length_of_gate > 0 and passenger_number < len(passengers):
            """
            This loop runs over length of gate and puts the passengers in there zones
            which is a queue
            """
            main_gate.enqueue(passengers[passenger_number])
            if str(passengers[passenger_number].ticket_number)[0] == '1':
                boarding_zone._zone1.enqueue(passengers[passenger_number])
            elif str(passengers[passenger_number].ticket_number)[0] == '2':
                boarding_zone._zone2.enqueue(passengers[passenger_number])
            elif str(passengers[passenger_number].ticket_number)[0] == '3':
                boarding_zone._zone3.enqueue(passengers[passenger_number])
            elif str(passengers[passenger_number].ticket_number)[0] == '4':
                boarding_zone._zone4.enqueue(passengers[passenger_number])
            print('\t', passengers[passenger_number])
            length_of_gate -= 1
            passenger_number += 1
        if passenger_number == len(passengers) and length_of_gate > 0:
            print("The last passenger is in line!")
        else:
            print("The gate is full; remaining passengers must wait.")

        number_of_flight = load_to_aircraft(main_gate, airport_capacity, boarding_zone, number_of_flight)
    return number_of_flight


def flight_simulation(air_stack, main_gate_length):
    """
    This function runs the flight loading and unloading functions
    It pops data from the stack if the passenger doesn't have a carry on
    and displays it
    If the passenger doesn't have a carry on then it will load the passenger
    to a queue and then after finishing the stack will dequeue it
    :param air_stack: stack with all the passengers in it
    :param main_gate_length: length of the main gate
    :return: emptied stack
    """
    if main_gate_length == 0:
        print("There are no more passengers at the gate.")
    else:
        print("The aircraft is full.")
    print("Ready for taking off ...")
    print("The aircraft has landed.")
    print("Passengers are disembarking...")
    passenger_with_carry_on = queue.Queue()
    while air_stack.length() > 0:
        passenger = air_stack.peek()
        if passenger.is_cary_on == "True":
            passenger_with_carry_on.enqueue(passenger)
            air_stack.pop()
        else:
            print('\t', air_stack.peek())
            air_stack.pop()
    while passenger_with_carry_on.length() > 0:
        print('\t', passenger_with_carry_on.peek())
        passenger_with_carry_on.dequeue()
    return air_stack


def read_files_from_file(file_name: str) -> list:
    """
    This function reads file from the text file passed from the arguments
    :param file_name: name of the text file from where the file will be read
    :return: secret keyword
    """
    open_file = open(file_name)
    file_content = open_file.readlines()
    passengers = []
    for line in file_content:
        passenger = line.strip().split(",")
        passenger_data = Passenger(passenger[0], int(passenger[1]), passenger[2])
        passengers.append(passenger_data)
    return passengers


def validation() -> int:
    """
    This functions validates user input and asks for loop to run again and again
    if it is wrong else it will accept
    :return: validated gate capacity and airport capacity
    """
    while True:
        gate_capacity = input("Gate capacity: ")
        try:
            gate_capacity = int(gate_capacity)
        except ValueError:
            print("Please enter positive integer")
            continue
        if gate_capacity > 0:
            break
        else:
            print("Please enter positive integer")
    while True:
        airport_capacity = input("Aircraft capacity: ")
        try:
            airport_capacity = int(airport_capacity)
        except ValueError:
            print("Please enter positive integer")
            continue
        if airport_capacity > 0:
            break
        else:
            print("Please enter positive integer")
    return gate_capacity, airport_capacity


def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and running the AiRIT's simulation.
    :return: None
    """
    passengers = []
    if len(sys.argv) != 2:
        print("Usage: python airit.py {filename}")
        return None
    try:
        passengers = read_files_from_file(sys.argv[1])
    except FileNotFoundError:
        print("File not found")
        return None
    gate_capacity, airport_capacity = validation()
    print("Reading passenger data from", sys.argv[1])
    print("Beginning simulation...")
    number_of_flight = run_simulation(passengers, gate_capacity, airport_capacity)
    print("Simulation complete. Statistics:", number_of_flight, "flights,", len(passengers),
          "passengers are at their destination")


if __name__ == '__main__':
    main()
