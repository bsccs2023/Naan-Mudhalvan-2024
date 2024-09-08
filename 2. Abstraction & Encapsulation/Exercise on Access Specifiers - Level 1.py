class Ticket:
    # Static variable to keep track of the ticket counter
    counter = 0

    def __init__(self, passenger_name, source, destination):
        # Private attributes
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination
        self.__ticket_id = None  # Initialize ticket ID as None

    @staticmethod
    def validate_source_destination(source, destination):
        """
        Validate source and destination.
        Source must be 'Delhi', and destination must be one of ['Mumbai', 'Chennai', 'Pune', 'Kolkata'].
        """
        valid_sources = ["delhi"]
        valid_destinations = ["mumbai", "chennai", "pune", "kolkata"]
        
        # Normalize the case and strip any extra spaces
        source = source.strip().lower()
        destination = destination.strip().lower()
        
        is_valid = source in valid_sources and destination in valid_destinations
        
        # Debug print statements
        print(f"Validating Source: {source} (Expected: {valid_sources})")
        print(f"Validating Destination: {destination} (Expected: {valid_destinations})")
        print(f"Validation Result: {is_valid}")
        
        return is_valid

    def generate_ticket(self):
        """
        Generate a ticket if source and destination are valid.
        Ticket ID format: <first_letter_of_source><first_letter_of_destination><counter>
        """
        if Ticket.validate_source_destination(self.__source, self.__destination):
            Ticket.counter += 1  # Increment static counter
            # Generate ticket ID with leading zero for numbers less than 10
            self.__ticket_id = f"{self.__source[0].upper()}{self.__destination[0].upper()}{Ticket.counter:02d}"
        else:
            self.__ticket_id = None

    def get_ticket_id(self):
        return self.__ticket_id

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_passenger_name(self):
        return self.__passenger_name

    def display_ticket_info(self):
        """
        Display ticket information.
        """
        if self.__ticket_id:
            print(f"Ticket ID: {self.__ticket_id}")
            print(f"Passenger Name: {self.__passenger_name}")
            print(f"Source: {self.__source}")
            print(f"Destination: {self.__destination}")
        else:
            print("Error: Invalid source or destination. Ticket ID not generated.")

# Testing the Ticket class
def test_ticket_generation():
    # Test Case 1: Valid data
    ticket1 = Ticket(passenger_name="Ram", source="Delhi", destination="Mumbai")
    ticket1.generate_ticket()
    ticket1.display_ticket_info()
    
    # Test Case 2: Invalid destination
    ticket2 = Ticket(passenger_name="Ram", source="Delhi", destination="New York")
    ticket2.generate_ticket()
    ticket2.display_ticket_info()
    
    # Test Case 3: Valid data
    ticket3 = Ticket(passenger_name="Ram", source="Delhi", destination="Chennai")
    ticket3.generate_ticket()
    ticket3.display_ticket_info()

    # Test Case 4: Valid data
    ticket4 = Ticket(passenger_name="Ram", source="Delhi", destination="Pune")
    ticket4.generate_ticket()
    ticket4.display_ticket_info()

    # Test Case 5: Valid data, testing auto-increment of counter
    ticket5 = Ticket(passenger_name="Ram", source="Delhi", destination="Kolkata")
    ticket5.generate_ticket()
    ticket5.display_ticket_info()

# Run the tests
test_ticket_generation()