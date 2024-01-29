# import calendar
# y = 2024
# m = 1
# print(calendar.month(y,m))

# a = 'salom dustim'
# print(a)

    
# ruyxat = []
# regitratsiya = input('jobingizni yozing')
# ruyxat.append(regitratsiya)
# print(ruyxat)

class Room:
    def __str__(self,number,status):
        self.number = number
        self.status = status
class Hotel(Room):
    def __str__(self):
        self.rooms = []
    
    def add_room(self,room):
        self.room = room
        self.rooms.append(room)
    
    def find_room(self,number):
        for room in self.rooms:
            if room.number == number:
                return room
            return None
    
    def check_in(self,number):
        room = self.find_room(number)
        if room is not None:
            room.status = 'occupied'
            print(f"room {room.number} has been checked in")

        else:
            print('invalid room number')

    def check_out(self,number):
            room = self.find_room(number)
            if room is not None:
                    room.status = "vacant"
                    print(f"room {room.number} has been checked out")
            else:
                 print('invalid room number')
                 
    def display_rooms(self):
        print('izlangan xona holati')
        for room in self.rooms:
            print(f"room {room.number},{room.status}")
hotel = Hotel()
