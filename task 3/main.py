class Room:
    # Represents a single room in the hotel
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_available = True  # Room is free by default
        self.guest = None         # No guest assigned yet
    
   # Formats the room details for printing
    def __str__(self):
        
        # 1. Figure out if the room is free or taken
        if self.is_available:
            status = "Available"
        else:
            status = f"Occupied by {self.guest.name}"
            
        # 2. Return the full sentence using that status
        return f"Room {self.room_number} | Price: ${self.price} | Status: {status}"

class Guest:
    # Storing basic details about the guest
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Hotel:
    # Manages rooms, bookings, and check-outs
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = {}  # Dictionary to store rooms (Key: room_number, Value: Room object)

    def add_room(self, room_number, price):
        # Adds a new room if it doesn't already exist
        if room_number in self.rooms:
            print(f"\nError: Room {room_number} already exists.")
        else:
            self.rooms[room_number] = Room(room_number, price)
            print(f"Success: Room {room_number} added successfully.")

    def show_available_rooms(self):
        # Filters and displays only unoccupied rooms
        available = [r for r in self.rooms.values() if r.is_available]
        
        if not available:
            print("\nNotice : No rooms are currently available for booking.")
            return False
        
        print("\n List of Available Rooms ")
        for room in available:
            print(room)
        return True

    def book_room(self, room_number, name, phone):
        # Assigns a guest to a room and marks it as occupied
        room = self.rooms.get(room_number)
        if room and room.is_available:
            room.guest = Guest(name, phone)
            room.is_available = False 
            print(f"\nBooking Confirmed: Room {room_number} assigned to {name}.")
        else:
            print("\nError: Invalid Room Number or Room is already occupied.")

    def check_out(self, room_number, nights):
        # Calculates the total bill and frees up the room
        room = self.rooms.get(room_number)
        if room and not room.is_available:
            bill = room.price * nights
            print("\n---------- BILLS ----------")
            print(f"Guest Name:   {room.guest.name}")
            print(f"Room Number:  {room_number}")
            print(f"Total Bill:   ${bill}")
            print("-----------------------------")
            room.is_available = True  # Free the room
            room.guest = None         # Remove the guest data
            print(f"Success: Room {room_number} is now free.")
        else:
            print("\nError: This room is either empty or does not exist.")


def main():
    # Initializing the hotel
    hotel = Hotel("The Bolan Residency")
    
    # Starting the main menu loop
    while True:
        print(f"\n=== {hotel.hotel_name} Management System ===")
        print("1. Add New Room")
        print("2. Show Available Rooms")
        print("3. Book a Room")
        print("4. Check-out & Generate Bill")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        # OPTION 1: Adding a room
        if choice == '1':
            try:
                num = input("Enter Room Number: ")
                prc = float(input("Enter Price: "))
                hotel.add_room(num, prc)
            except ValueError:
                print("Error: Please enter a valid number for price.")

        # OPTION 2: List of available rooms
        elif choice == '2':
            if not hotel.rooms:
                print(" No rooms exist. Please add a room first (Option 1).")
            else:
                hotel.show_available_rooms()

        # OPTION 3: Book a room
        elif choice == '3':
            if not hotel.rooms:
                print("System Alert: Cannot book. No rooms have been created yet.")
            elif hotel.show_available_rooms():
                num = input("\nEnter Room Number to book: ")

                #  Fetching the room first
                room = hotel.rooms.get(num)

                #  Checking immediately if the room exists
                if not room:
                    print(f"\nError: Room {num} does not exist in The Bolan Residency.")
                
                #  Checking immediately if the room is already taken
                elif not room.is_available:
                    print(f"\nError: Room {num} is currently occupied.")
                
                #  If everything is good, now we ask for guest details
                else:
                    name = input("Enter Guest Name: ")
                    ph = input("Enter Guest Phone: ")
                    hotel.book_room(num, name, ph)

        # OPTION 4: Checking out a guest
        elif choice == '4':
            occupied_rooms = [r for r in hotel.rooms.values() if not r.is_available]
            
            if not hotel.rooms:
                print("System Alert: No rooms exist in the system.")
            elif not occupied_rooms:
                print("System Alert: No guests are currently checked in.")
            else:
                print("\n--- Occupied Rooms ---")
                for r in occupied_rooms:
                    print(f"Room {r.room_number} (Guest: {r.guest.name})")
                
                num = input("\nEnter Room Number for check-out: ")

                #  Fetch the room first
                room = hotel.rooms.get(num)

                #  Check immediately if the room exists
                if not room:
                    print(f"\nError: Room {num} does not exist in The Bolan Residency.")
                
                #  Check immediately if the room is already empty
                elif room.is_available:
                    print(f"\nError: Room {num} is already empty. No guest to check out.")
                
                #  If everything is correct, ask for nights and generate the bill
                else:
                    try:
                        # Notice how it now uses the guest's name to be more polite!
                        days = int(input(f"Enter number of nights {room.guest.name} stayed: "))
                        hotel.check_out(num, days)
                    except ValueError:
                        print("Error: Nights must be a whole number.")
        # OPTION 5: Exiting the program
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid Choice! Please select 1-5.")

# Run the program
if __name__ == "__main__":
    main()