import Animales
#Importamos el Modulo Animales para utilizar como clase padre la clase Animales
class Conejos(Animales.Animales):
	"""Creamos la clase conejos y heredamos parte de su comportamiento de la clase Animales"""
	def __Reserva(self,reserva):
		self.ReservaAlimenticia+=reserva
	def Alimentarse(self,TipoAlimento,CantidadAlimento):					
		if(TipoAlimento=="Pasto"):
			self.__Reserva(CantidadAlimento)
		else:
			print("No debe alimentar a animales herviboros con {0}".format(TipoAlimento))