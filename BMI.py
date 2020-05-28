class BMI:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_BMI(self):
        return self.weight / (self.height*self.height)


Pit = BMI(80,180)

print(Pit.calculate_BMI())