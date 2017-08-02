import datetime
class Animales(object):
	"""Algunos de los procesos que comparten los animales entre ellos, sin importar su raza o clase"""
	def __init__(self,reproduccion_animales,cantidad_animales):
		self.cantidad_animales = cantidad_animales
		self.reproduccion = reproduccion_animales
		self.reserva_alimenticia = 0
		self.cantidad_alimento=0
		self.tipo_alimento=""
		self.cantidad_agua=0
		self.partos=[]
		self.partos_animales=[]

	def __nacimientos(self,hembras_prenadas):
		"""
		Clase privada solo puede ser accedida desde Self.Reproducir y no puede ser accedida de forma independiente, solamente se agrega __ (dos guiones bajo)
		Recibe la cantidad de hembras preñadas, luego multiplica dicha cantidad por animales que pueden tener por parto aumenta la cantidad de animales en la granja
		"""
		nacidos = (self.reproduccion*hembras_prenadas)
		self.CantidadAnimales+=nacidos
		self.partos.append(datetime.datetime.today())
		self.partos_animales.append(nacidos)
		print("Tiene {0} nuevos animales, ahora posee {1}".format(nacidos,self.cantidad_animales))

	def repoducir(self,cantidad_animales):
		"""Recibe la cantidad de animales preñados, verifica si es menor a la cantidad existentes en la granja y accede a la funcion __Nacimientos"""
		if(self.cantidad_animales>cantidad_animales):
			self.__nacimientos(cantidad_animales)
		else:
			print("La cantidad de hembras prenadas no puede ser superior a la cantidad de animales en la granja")

	def decesos(self,cantidad_animales):
		if(self.cantidad_animales>cantidadanimales):
			self.cantidad_animales-=cantidad_animales
			print("Fallecieron {0} animales, ahora posee {1}".format(cantidad_animales,self.cantidad_animales))
		else:
			print("La cantidad de animales fallecidos no puede ser superior a la cantidad de animales en la granja")

	def imprimir_partos(self):
		"""Imprime la cantidad de partos que existe en la granja"""
		print("Cantidad\tFecha de Nacimiento")
		rango = len(self.Partos)
		if(rango>0):
			for elemento in range(rango):
				print("{0}\t\t{1}".format(self.partos_animales[elemento],self.partos[elemento]))
		elif(rango==0):
			for elemento in range(rango):
				print("{0}\t\t{1}".format(self.partos_animales[0],self.partos[0]))
		else:
			print("No existe partos recientemente")
