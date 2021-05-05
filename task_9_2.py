class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.asphalt = 25
        self.thickness = 5

    def weight_of_asphalt(self):
        return int(self._length * self._width * self.asphalt * self.thickness/1000)


findings = Road(5000, 20)
print(findings.weight_of_asphalt())
