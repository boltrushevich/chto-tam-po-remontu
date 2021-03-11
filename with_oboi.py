class WinDoor:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'


class Room:

    def __init__(self, x, y, z, room_name):
        self.x = x
        self.y = y
        self.z = z
        self.room_name = room_name
        self.wd = []
        self.locations = {}

    def rooms(self):
        self.locations[self.room_name] = (self.x, self.y, self.z)
        return f'{self.room_name}: {self.x}x{self.y}x{self.z}'

    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))

    def full_square(self, room_name):
        room_name = self.room_name
        #self.square = 2 * self.locations[self.room_name[2]] * (self.locations[self.room_name[0]] + self.locations[self.room_name[1]])
        self.square = 2 * self.z * (self.x + self.y)
        return self.square

    def workSurface(self):
        self.new_square = self.square
        for i in self.wd:
            self.new_square -= i.square
        return self.new_square

    def oboi(self, width, length):
        self.width = float(input('Enter width: '))
        self. length = float(input('Enter length: '))
        self.num_of_rulons = (self.new_square)//(self.length * self.width) + 1

    def __repr__(self):
        return f'Оклеиваемая площадь составляет {self.new_square}. Для этого потребуется {self.num_of_rulons} рулонов.'

