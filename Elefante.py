import Animales
class Elefante(Animales.Animales):
	def TomarAgua(self,tipoagua,cantidadagua):
		if(tipoagua.lower()=="limpia"):
			self.CantidadAgua+=cantidadagua
		else:
			print("El agua no es adecuada, busquemos otro lugar")

	def Comer(self,tipoalimento,cantidadcomer):
		if(tipoalimento.lower()=="Many"):
			self.CantidadAlimento+=cantidadcomer
			self.TipoAlimento=tipoalimento
		else:
			print("Solo me alimento de manies")
			