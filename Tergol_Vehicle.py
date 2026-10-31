class Vehicle:
    total_units: int = 0

    def __init__(self, model: str, plate: str, paint: str = 'Gray'):
        self._model = model
        self._plate = plate
        self.paint = paint
        Vehicle.total_units += 1
        self._serial = Vehicle.total_units
        self._odometer: float = 0.0  # תיקון לשם עקבי עם drive

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model: str):
        self._model = model

    @property
    def plate(self):
        return self._plate

    @plate.setter
    def plate(self, plate: str):
        self._plate = plate

    @property
    def odometer(self):
        return self._odometer

    def drive(self, km: float):
        if km >= 0:
            self._odometer += km
        else:
            raise ValueError('KM must be positive')  # תיקון ה-raise

    def summary(self, verbose: bool = False):
        if verbose:
            return f'model: {self._model}\nplate: {self._plate}\nodometer: {self._odometer}'
        else:
            return f'model: {self._model}\nplate: {self._plate}\n{self._serial}'

    def repaint(self, new_paint: str):
        self.paint = new_paint

    @classmethod
    def parse(cls, line: str, sep: str = ','):
        model, plate = line.split(sep)
        return cls(model.strip(), plate.strip())

    def __str__(self):
        return f'Vehicle: {self._serial}, {self.model}, {self.plate}'

honda = Vehicle(model='honda', plate='123-45-678')
print('Honda:',honda)
print(honda.summary(verbose=True))