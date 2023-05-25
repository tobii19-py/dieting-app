class Calorie:
    """Represent the amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature"""

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        pass