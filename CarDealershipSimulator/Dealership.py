from models import Sedan , Suv 
from models.Ford import Escape , Explorer
from models.Toyota import Camry , Highlander
from models.Honda import Civic , Pilot

class Dealership: 
	def __init__(self):
		self.inventory = {}

	def getSedans(self):
		return { k: v for k, v in self.inventory if isSubclass(type(v), Sedan) }

	def getSuvs(self):
		return { k: v for k, v in self.inventory if isSubclass(type(v), Suv) }

	def makeSale(self, vehicleId):
		del self.inventory[vehicleId]
		print('Sold: ' + self.inventory[vehicleId])

	def addToInventory(self, carToAdd):
		self.inventory[carToAdd.vehicleId] = carToAdd

	def recieveShipment(self, shipment):
		for x in shipment:
			addToInventory(x)