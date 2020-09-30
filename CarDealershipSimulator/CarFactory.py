from models.Ford import Escape , Explorer
from models.Toyota import Camry , Highlander
from models.Honda import Civic , Pilot

class CarFactory:
	def __init__(self):
		self.initializers = { 
	        "Highlander": Highlander, 
	        "Camry": Camry, 
	        "Civic": Civic, 
	        "Pilot": Pilot, 
	        "Explorer": Explorer, 
	        "Escape": Escape
	    }

	def manafactureCar(self, carToMake):  
	    self.intializer = self.initializers[carToMake]
	    return intializer("1995", "blue", "alloy")