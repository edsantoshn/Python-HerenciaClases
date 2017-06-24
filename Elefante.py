import Animales
class Elefante(Animales.Animales):
	"""Importamos el modulo Animales y le heredamos todos sus metodos (funciones) y atributos, construimos metodos especificios para los elefantes"""
	def TomarAgua(self,tipoagua,cantidadagua):
		"""Recibe el tipo de agua y la cantidad de la misma, si el agua es limpia procede a tomar caso contrario manda error"""
		if(tipoagua.lower()=="limpia"):
			self.CantidadAgua+=cantidadagua
		else:
			print("El agua no es adecuada, busquemos otro lugar")

	def Comer(self,tipoalimento,cantidadcomer):
		"""Recibe el tipo de alimento y la cantidad del mismo, si el alimento es mani el elefante procede a comer, caso contrario manda error"""
		if(tipoalimento.lower()=="mani"):
			self.CantidadAlimento+=cantidadcomer
			self.TipoAlimento=tipoalimento
		else:
			print("Solo me alimento de manies")
			