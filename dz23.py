class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, number_of_wheels):
        if number_of_wheels == 2:
            return f"Это мотоцикл марки {self.name}"
        if number_of_wheels == 3:
            return f"Это трицикл марки {self.name}"
        if number_of_wheels == 4:
            return f"Это автомобиль марки {self.name}"
        if number_of_wheels > 4:
            return f"Я не знаю такого ТС"

    def get_vehicle_advice(self):

        if self.mileage < 50000:
            return f"Неплохо {self.name} можно брать."
        elif self.mileage < 100000:
            return f"{self.name} надо внимательно проверить."
        elif self.mileage < 150000:
            return f"{self.name} надо провести полную диагностику."
        elif self.mileage > 150000:
            return f"{self.name} лучше не покупать."


Vehicle_1 = Vehicle("SKODA", 33333)
Vehicle_2 = Vehicle("VOLVO", 66666)
Vehicle_3 = Vehicle("BMW", 123123)
Vehicle_4 = Vehicle("TOYOTA", 150234)

print(Vehicle_1.get_vehicle_advice())
print(Vehicle_2.get_vehicle_advice())
print(Vehicle_3.get_vehicle_advice())
print(Vehicle_4.get_vehicle_advice())

print(Vehicle_1.get_vehicle_type(2))
print(Vehicle_2.get_vehicle_type(3))
print(Vehicle_3.get_vehicle_type(4))
print(Vehicle_4.get_vehicle_type(5))


#########################################################################################

class Printer:
    def __init__(self, model, type, value, year_of_issue):
        self._model = model
        self._type = type
        self._value = value
        self._year_of_issue = year_of_issue
        # self._image_drum = image_drum
        print(f"Это {type} принтер, модели {model}, {year_of_issue} года выпуска, стоимостью {value}")

    def Cartridge(self):
        return (f"Картридж модели {self._model}")

    def Paper(self, format, amount):
        return f"В картридж добавленно {amount} листов формата {format}"

    def Image_drum(self, image_drum):
        return f"Ресурс фотобарабана = {image_drum}"


Printer_1 = Printer("M6500", "Матричный", "7999", "2004")
print(Printer_1.Cartridge())
print(Printer_1.Paper("A4", 33))
print(Printer_1.Image_drum(5000))

Printer_2 = Printer("Mf310", "Лазерный", "5999", "2006")
print(Printer_2.Cartridge())
print(Printer_2.Paper("A4", 66))
print(Printer_2.Image_drum(5500))
