class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage.
    """

    def __init__(self, city, country):
        self.country = country
        self.city = city

    def get(self):
        pass