import Conejos
#Importamos el modulo Conejos que hereda de la clase Animales
import Elefante

conejos = Conejos.Conejos(6,14)
#Instanciamos la clase e inicializamos la clase conejos que hereda
#la funcion __init__ de la clase Animales

conejos.Repoducir(4)
conejos.Repoducir(4)
conejos.Repoducir(14)
conejos.Repoducir(10)
#Funcion heredada de la clase Animales
conejos.Alimentarse("Pasto",100)

conejos.ImprimirPartos()

elefante = Elefante.Elefante(1,16)
#Instancia la clase de Elefante y la construye

elefante.Repoducir(6)
elefante.Repoducir(4)
elefante.Repoducir(8)
elefante.Repoducir(12)

elefante.TomarAgua("Limpia",100)

elefante.ImprimirPartos()