from Dealership import Dealership
from CarFactory import CarFactory
import random

# TO DO: maybe iterate through models instead of defining here
carClasses = ["Highlander", "Camry", "Civic", "Pilot", "Explorer", "Escape"]

if __name__ == "__main__":
	print('*******************************')
	print('    Starting simulation...')

	dealership = Dealership()
	factory = CarFactory()

	shipment = []
	for x in range(random.randint(0,9)):
		car = factory.manafactureCar(
			carClasses[random.randint(0, len(carClasses) - 1)])

		print(car)
		shipment.append(car)

	dealership.recieveShipment(shipment)
	print(dealership.getSedans())