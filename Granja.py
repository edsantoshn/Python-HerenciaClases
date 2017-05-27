import Conejos
#Importamos el modulo Conejos que hereda de la clase Animales

conejos = Conejos.Conejos(6,4)
#Instanciamos la clase e inicializamos la clase conejos que hereda
#la funcion __init__ de la clase Animales

conejos.Repoducir(4)
#Funcion heredada de la clase Animales
conejos.Alimentarse("Pasto",100)