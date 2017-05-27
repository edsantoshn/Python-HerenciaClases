class Animales(object):
	"""Algunos de los procesos que comparten los animales entre ellos, sin importar su raza o clase"""
	def __init__(self,cantidadanimales,reproduccionanimales):
		self.CantidadAnimales = cantidadanimales
		self.Reproduccion = reproduccionanimales
		self.ReservaAlimenticia = 0
	def Nacimientos(self,hembrasprenadas):
		if(self.CantidadAnimales>hembrasprenadas):
			nacidos = (self.Reproduccion*hembrasprenadas)
			self.CantidadAnimales+=nacidos
			print("Tiene {0} nuevos animales, ahora posee {1}".format(nacidos,self.CantidadAnimales))
		else:
			print("La cantidad de hembras prenadas no puede ser superior a la cantidad de animales en la granja")

	def Repoducir(self,cantidadanimales):
		if(self.CantidadAnimales>cantidadanimales):
			self.Nacimientos(cantidadanimales)
		else:
			print("La cantidad de hembras prenadas no puede ser superior a la cantidad de animales en la granja")

	def Decesos(self,cantidadanimales):
		if(self.CantidadAnimales>cantidadanimales):
			self.CantidadAnimales-=cantidadanimales
			print("Fallecieron {0} animales, ahora posee {1}".format(cantidadanimales,self.CantidadAnimales))
		else:
			print("La cantidad de animales fallecidos no puede ser superior a la cantidad de animales en la granja")