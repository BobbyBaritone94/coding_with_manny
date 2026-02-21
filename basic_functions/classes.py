class Square():
    def __init__(self,side_length):
        self.side_length = side_length
    def get_area(self):
        return self.side_length*self.side_length
    def get_perimeter(self):
        return 4 * self.side_length
    def print_stats(self):
        print(f'AREA: {self.get_area()}')
        print(f'PERIMETER: {self.get_perimeter()}')

for x in range (10):
    print(f'Square stats: {x}')
    Square(x).print_stats()

