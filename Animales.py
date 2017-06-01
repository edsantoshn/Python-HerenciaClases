import datetime
class Animales(object):
	"""Algunos de los procesos que comparten los animales entre ellos, sin importar su raza o clase"""
	def __init__(self,reproduccionanimales,cantidadanimales):
		self.CantidadAnimales = cantidadanimales
		self.Reproduccion = reproduccionanimales
		self.ReservaAlimenticia = 0
		self.CantidadAlimento=0
		self.TipoAlimento=""
		self.CantidadAgua=0
		self.Partos=[]
		self.PartosAnimales=[]

	def __Nacimientos(self,hembrasprenadas):
		nacidos = (self.Reproduccion*hembrasprenadas)
		self.CantidadAnimales+=nacidos
		self.Partos.append(datetime.datetime.today())
		self.PartosAnimales.append(nacidos)
		print("Tiene {0} nuevos animales, ahora posee {1}".format(nacidos,self.CantidadAnimales))

	def Repoducir(self,cantidadanimales):
		if(self.CantidadAnimales>cantidadanimales):
			self.__Nacimientos(cantidadanimales)
		else:
			print("La cantidad de hembras prenadas no puede ser superior a la cantidad de animales en la granja")

	def Decesos(self,cantidadanimales):
		if(self.CantidadAnimales>cantidadanimales):
			self.CantidadAnimales-=cantidadanimales
			print("Fallecieron {0} animales, ahora posee {1}".format(cantidadanimales,self.CantidadAnimales))
		else:
			print("La cantidad de animales fallecidos no puede ser superior a la cantidad de animales en la granja")

	def ImprimirPartos(self):
		print("Cantidad\tFecha de Nacimiento")
		rango = len(self.Partos)
		if(rango>0):
			for elemento in range(rango):
				print("{0}\t\t{1}".format(self.PartosAnimales[elemento],self.Partos[elemento]))
		elif(rango==0):
			for elemento in range(rango):
				print("{0}\t\t{1}".format(self.PartosAnimales[0],self.Partos[0]))
		else:
			print("No existe partos recientemente")