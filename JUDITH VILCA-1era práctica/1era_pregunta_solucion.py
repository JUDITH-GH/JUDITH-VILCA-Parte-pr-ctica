"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía de un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo entero, aplicar conversión de datos
- Identificar si la edad es mayor de 30 mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10
de su sueldo, según corresponda
"""
#Variable tipo String
nombre="Judith"
compañia="Sara"
#Variable tipo entero
salario=100
edad="30"

if int(edad)>30:
    bono_final = (salario ** 2) + (0.05 * salario)
    print("Usted tiene un bono de 10% en el mes de diciembre, con un bono final de: {} soles".format(bono_final))
else:
    bono_final = (salario ** 2) + (0.05 * salario)
    print("Usted tiene un bono del 5% en el mes diciembre, con un bono final de: {} soles".format(bono_final))
