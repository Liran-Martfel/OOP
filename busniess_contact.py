from typing import override
from contact import Contact

class BusinessContact(Contact):
    def __init__(self, name, number, company, rate):
        super().__init__(name, number)
        self.company = company
        self.rate = rate

    @property
    def name(self):
        return super().name + " (Business)"

    @override
    def describe(self):
        return super().__str__() + f" | Company: {self.company} | Rate: {self.rate}"

    @override
    def __str__(self):
        return ("Business " + super().__str__() + f" | Company: {self.company} | Rate: {self.rate}")

    def cost(self, hours):
        return hours * self.rate