import Animales
#Importamos el Modulo Animales para utilizar como clase padre la clase Animales
class Conejos(Animales.Animales):
	"""Creamos la clase conejos y heredamos parte de su comportamiento de la clase Animales"""
	def __Reserva(self,reserva):
		"""Esta funcion privada o encapsulada, aumenta la cantidad de alimento que el animal tiene almacenado"""
		self.ReservaAlimenticia+=reserva
	def Alimentarse(self,TipoAlimento,CantidadAlimento):					
		"""Recibe el tipo de alimento y la cantidad del mismo que se prentende dar a los conejos, si es pasto llama a la funcion __Reserva caso contrario manda mensaje"""
		if(TipoAlimento.lower()=="pasto"):
			self.__Reserva(CantidadAlimento)
		else:
			print("No debe alimentar a animales herviboros con {0}".format(TipoAlimento))