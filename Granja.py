import Conejos
#Importamos el modulo Conejos que hereda de la clase Animales
import Elefante

def crear_conejos(self,cantidad_conejos,cantidad_conejos_parto):
	return Conejos.Conejos(cantidad_conejos,cantidad_conejos_parto)
	#Instanciamos la clase e inicializamos la clase conejos que hereda
	#la funcion __init__ de la clase Animales
def crear_elefantes(self,cantidad_elefantes,cantidad_elefantes_parto):
	return Elefante.Elefante(1,16)
	#Instancia la clase de Elefante y la construye

cantidad_conejos_input = int(input('Ingrese la cantidad de conejos existe: '))
cantidad_conejos_parto_input = int(input('Ingrese la cantidad de conejos por parto: '))
conejos = crear_conejos(cantidad_conejos_input,cantidad_conejos_parto_input)

conejos.Repoducir(4)
conejos.Repoducir(4)
conejos.Repoducir(14)
conejos.Repoducir(10)
#Funcion heredada de la clase Animales
conejos.Alimentarse("Pasto",100)

conejos.ImprimirPartos()


cantidad_elefantes_input = int(input('Ingrese la cantidad de elefantes existe: '))
cantidad_elefantes_parto_input = int(input('Ingrese la cantidad de elefantes por parto: '))
elefante = crear_elefantes(cantidad_elefantes_input,cantidad_elefantes_parto_input)

elefante.Repoducir(6)
elefante.Repoducir(4)
elefante.Repoducir(8)
elefante.Repoducir(12)

elefante.TomarAgua("Limpia",100)

elefante.ImprimirPartos()