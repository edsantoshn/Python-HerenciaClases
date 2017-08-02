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

conejos.repoducir(4)
conejos.repoducir(4)
conejos.repoducir(14)
conejos.repoducir(10)
#Funcion heredada de la clase Animales
conejos.alimentarse("Pasto",100)

conejos.imprimir_partos()


cantidad_elefantes_input = int(input('Ingrese la cantidad de elefantes existe: '))
cantidad_elefantes_parto_input = int(input('Ingrese la cantidad de elefantes por parto: '))
elefante = crear_elefantes(cantidad_elefantes_input,cantidad_elefantes_parto_input)

elefante.repoducir(6)
elefante.repoducir(4)
elefante.repoducir(8)
elefante.repoducir(12)

elefante.tomar_agua("Limpia",100)

elefante.imprimir_partos()
