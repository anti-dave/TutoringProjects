import uuid 
from abc import ABC

class Car(ABC):
	def __init__(self, year):
		self.vin = uuid.uuid1()
		# self.year = year
		self.make = ''
		self.model = ''