import numpy as np


class BMI:

    def __init__(self, height, weight, ):
        self.height = height
        self.weight = weight

    def bmi_calculation(self):
        return self.weight * self.height


Victoria = BMI(176, 69)
Pit = BMI(180, 80)

print(Pit.bmi_calculation())


class Portfolio:

    def __init__(self, tag1, tag2):
        self.tag1 = tag1
        self.tag2 = tag2

    def calculat_return(self):
        return (self.tag2 - self.tag1) / self.tag1


my_return = Portfolio(100, 110)

print(my_return.calculat_return(), '%')

number = 3

weights = np.random.random(number)
weights /= np.sum(weights)

equal_weights = np.array(number * [1 / number])
print(equal_weights)

print(weights)
