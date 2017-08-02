import Animales
class Elefante(Animales.Animales):
	"""Importamos el modulo Animales y le heredamos todos sus metodos (funciones) y atributos, construimos metodos especificios para los elefantes"""
	def tomar_agua(self,tipo_agua,cantidad_agua):
		"""Recibe el tipo de agua y la cantidad de la misma, si el agua es limpia procede a tomar caso contrario manda error"""
		if(tipo_agua.lower()=="limpia"):
			self.cantidad_agua+=cantidad_agua
		else:
			print("El agua no es adecuada, busquemos otro lugar")

	def Comer(self,tipo_alimento,cantidad_comer):
		"""Recibe el tipo de alimento y la cantidad del mismo, si el alimento es mani el elefante procede a comer, caso contrario manda error"""
		if(tipo_alimento.lower()=="mani"):
			self.cantidad_alimento+=cantidad_comer
			self.tipo_alimento=tipo_alimento
		else:
			print("Solo me alimento de manies")
			
