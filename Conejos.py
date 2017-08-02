import Animales
#Importamos el Modulo Animales para utilizar como clase padre la clase Animales
class Conejos(Animales.Animales):
	"""Creamos la clase conejos y heredamos parte de su comportamiento de la clase Animales"""
	def __reserva(self,reserva):
		"""Esta funcion privada o encapsulada, aumenta la cantidad de alimento que el animal tiene almacenado"""
		self.reserva_alimenticia+=reserva
	def Alimentarse(self,tipo_alimento,cantidad_alimento):					
		"""Recibe el tipo de alimento y la cantidad del mismo que se prentende dar a los conejos, si es pasto llama a la funcion __Reserva caso contrario manda mensaje"""
		if(tipo_alimento.lower()=="pasto"):
			self.__reserva(cantidad_alimento)
		else:
			print("No debe alimentar a animales herviboros con {0}".format(tipo_alimento))
