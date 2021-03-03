#MODULOS-----------------------------------
from fractions import Fraction #para fracciones
import math #para logaritmos
import sys
import operator #para ordenar



##FUNCIONES---------------------------------

#Leer el texto base de un archivo y generar la Fuente de información con frecuencias absolutas.
def fuente_informacion_freq_absolutas(nombre_archivo):
    
    fuente_informacion = {} #diccionario que sera mi fuente (alfabeto + frecuencias)
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                #print(caracter)


                    #Miro si es el caracter de fin de línea en cuyo caso lo agregaré como un doble espacio separado, dos espacios simples vaya, no un nuevo símbolo que sea "  "
                if caracter == "\n":    
                        
                    caracter = " " #convierto el \n en un espacio
                    for i in range(0,2): #0 incluido, 2 excluido --> 2 iteraciones
                        if " " in fuente_informacion: #si ya he añadido antes un espacio
                            fuente_informacion[" "] = fuente_informacion[" "] + 1 #si ya estaba el simbolo solo le sumo una ocurrencia 
                        else:
                            fuente_informacion[" "] = 1 #si es la primera ocurrencia, añado al diccionario el espacio (" ") con una ocurrencia
                   
                else: #si no es el de fin de linea es otro pero que tampoco esta en el alfabeto actualmente

                    #miro si el caracter esta ya en el alfabeto
                    if caracter in fuente_informacion:


                        fuente_informacion[caracter] = fuente_informacion[caracter]+1  #si está le sumo uno a su nº de ocurencias
                    
                    else:
                        
                        fuente_informacion[caracter] = 1  #simplemente le pongo una ocurrencia (al ponerle 1 ocurrencia se añaden la clave y el valor, es decir el caracter y el 1)



            #sigo leyendo la siguiente
            linea = f.readline()
        



      

    #TENIENDO YA EL ALFABETO Y LAS FRECUENCIAS ABS EN EL DICCIONARIO DE NOMBRE fuente_informacion {caracter : freq} las devuelvo
    return fuente_informacion

def fuente_informacion_probabilidades(fuente_freq_abs):

    fuente_de_informacion = {}  

                #alfabeto = []  #defino dos listas para tener separadas ambas partes de la fuente 
                #probabilidades = []


    total_frecuencias = sum(fuente_freq_abs.values()) #sumo los valores de todas las claves del diccionario, es decir, las frecuencias absolutas de todos los simbolos (=TOTAL).
    print("TOTAL = ", total_frecuencias)

                #OTRA POSIBILIDAD:
                #posicion = 0
                #for i in fuente_freq_abs.keys():
                #    alfabeto.append(i)
                #    posicion = posicion + 1

                #posicion = 0
                #for j in fuente_freq_abs.values():
                #    probabilidades.append(Fraction(j,total_frecuencias))
                #    posicion = posicion + 1


                #print(alfabeto)
                #print (probabilidades)

    fuente_de_informacion = fuente_freq_abs.copy()  #copio tal cual la fuente


    for clave, valor in fuente_de_informacion.items():  #Clave itera las claves del diccionario una a una (fuente_de_informacion['L'] = 1/219) y valor itera por los valores del diccionario, así puedo sobreescribir
        fuente_de_informacion[clave] = Fraction(valor, total_frecuencias) #mantengo el simbolo del alfabeto y el valor para ese simbolo lo reemplazo con la probabilidad (freq relativa)
    
    #IMPORTANTE! 30/219 == 10/73 No nos liemos
    #print(fuente_de_informacion)
    
    return fuente_de_informacion

def entropia(fuente_inf):
    entropia = 0
    for valor in fuente_inf.values(): #Me va dando cada probabilidad de la fuente (psubi) iterara tantas veces como valores tenga la fuente, es decir, ya son las m veces que quiero iterar
        entropia = entropia + (valor * math.log(Fraction(1, valor),2)) #logaritmo en base 2 del inverso de la probabilidad para esa iteracion

    return entropia

def ordenar_mayor_a_menor_probabilidad(fuente_inf):
   
    copia_fuente_infor = {}
    fuente_ordenada = {}
    
    
    copia_fuente_infor = fuente_inf.copy() #hago una copia para que no me cambie la otra a este orden sino solamente la copia

    iterador_fuente_ordenada = sorted(copia_fuente_infor.items(), key=operator.itemgetter(1), reverse=True)

    print("Fuente Ordenada de Mayor a Menor probabilidad: (para saber la frecuencia buscar el símbolo en las Freqs. Abs):")

    for clave in enumerate(iterador_fuente_ordenada):
        print(clave[1][0], copia_fuente_infor[clave[1][0]])  #tenemos el orden de la lista de mayor a menor en fuente_ordenada. Entonces cogiendo el iterador de ella vamos seleccionando en la otra (lista original) segun marca el orden en la lista ordenada
        fuente_ordenada[clave[1][0]] = copia_fuente_infor[clave[1][0]]  #Voy metiendo en orden a un nuevo diccionario que será la fuente ordenada


    return fuente_ordenada

def anyadir_a_fuente(caracteres, fuente_informacion_extendida):

   #miro si el símbolo compuesto de 2 caracteres esta ya en el alfabeto
    if caracteres in fuente_informacion_extendida:
        fuente_informacion_extendida[caracteres] = fuente_informacion_extendida[caracteres]+1  #si está le sumo uno a su nº de ocurencias
    else:
        fuente_informacion_extendida[caracteres] = 1  #simplemente le pongo una ocurrencia (al ponerle 1 ocurrencia se añaden la clave y el valor, es decir el caracter y el 1)

    return fuente_informacion_extendida

def f_i_2en2_freq_absolutas(nombre_archivo):
    fuente_informacion_extendida = {} 
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: 

        linea = f.readline() 
        caracteres = ""

        while linea:
            
            for caracter in linea: #como tengo que hacer de 2 caracteres 1 símbolo, tengo que agrupar los dos caracteres antes de meterlos al diccionario
                
                #Miro si es el caracter de fin de línea en cuyo caso lo agregaré como dos espacios simples vaya
                if caracter == "\n":    

                    #o si no tengo ninguno y empieza el texto con un salto de linea y entonces se añaden los dos
                    if len(caracteres) == 0:
                        caracteres = "  "
                        fuente_informacion_extendida = anyadir_a_fuente(caracteres, fuente_informacion_extendida) #funcion que añade a la fuente los 2 caracteres
                        caracteres = ""


                    #mirare si ya tengo un caracter agrupado y entonces solo añadire 1 de los dos espacios y el otro quedará para la siguiente
                    if len(caracteres) == 1:
                        caracteres = caracteres + " "
                        fuente_informacion_extendida = anyadir_a_fuente(caracteres, fuente_informacion_extendida) #funcion que añade a la fuente los 2 caracteres
                        caracteres = ""
                        caracteres = caracteres + " " #dejo el segundo espacio grabado para la proxima iteracion


                    #o si ya tengo dos caracteres agrupados y entonces quedan los dos para la siguiente
                    if len(caracteres) == 2:
                        fuente_informacion_extendida = anyadir_a_fuente(caracteres, fuente_informacion_extendida) #funcion que añade a la fuente los 2 caracteres
                        caracteres = "  "


                else: #si no es el de fin de linea es otro


                    if len(caracteres) == 0:
                         caracteres = caracteres + caracter #long 1 actualmente
                    else:

                        if len(caracteres) == 1:
                            caracteres = caracteres + caracter
                            fuente_informacion_extendida = anyadir_a_fuente(caracteres, fuente_informacion_extendida)
                            caracteres = "" #long 0 actualmente
                                
                        #verifico lo primero no sea que ya tenga dos caracteres agrupados porque se empiece con un \n el texto
                        if len(caracteres) == 2:
                            fuente_informacion_extendida = anyadir_a_fuente(caracteres, fuente_informacion_extendida)
                            caracteres = ""
                            caracteres = caracteres + caracter #long 1 actualmente


            #sigo leyendo la siguiente
            linea = f.readline()
        


    #TENIENDO YA EL ALFABETO Y LAS FRECUENCIAS ABS EN EL DICCIONARIO DE NOMBRE fuente_informacion {caracter : freq} las devuelvo
    return fuente_informacion_extendida








##PROGRAMA------------------------
print()
print()

    #1. Alfabeto + Frecuencias Absolutas

fuente_freq_abs = fuente_informacion_freq_absolutas('/Users/mario/Desktop/Pracica_1_SI/datos_1.txt')
print("Freqs. Abs = ", fuente_freq_abs)
print()


    #2. Fuente de Información (Alfabeto + probabilidades/Frecuencia Relativa)

fuente_de_informacion = fuente_informacion_probabilidades(fuente_freq_abs)
print("Fuente de Informacion = ", fuente_de_informacion)
print()


    #3. Entropía

valor_entropia = entropia(fuente_de_informacion)
print(valor_entropia) 
print()


    #4. Ordenar la Fuente de Informacion de mayor a menor probabilidad

fuente_de_informacion_ordenada = ordenar_mayor_a_menor_probabilidad(fuente_de_informacion)
print()
print("En Forma de Diccionario:")
print(fuente_de_informacion_ordenada)
print()


    #5. Fuente Extendida (agrupando de 2 en dos en el texto)

fuente_extendida2en2_freq_abs = f_i_2en2_freq_absolutas('/Users/mario/Desktop/Pracica_1_SI/datos_1.txt')
print("Fuente Extendida 2en2 FRECUENCIAS:")
print(fuente_extendida2en2_freq_abs)
print()

    #para todos los demás cálculos que no son extraer el alfabeto y las frecuencias con la agrupacion pedida reutilizo las funciones que ya tengo
print("Fuente Extendida 2en2 PROBABILIDADES:")
fuente_extendida2en2_PROB = fuente_informacion_probabilidades(fuente_extendida2en2_freq_abs)
print(fuente_extendida2en2_PROB)
print()


print("Fuente Extendida 2en2 Valor ENTROPIA:")
fuente_extendida2en2_ENTRP = entropia(fuente_extendida2en2_PROB)
print(fuente_extendida2en2_ENTRP)
print()


print("Fuente Extendida 2en2 ORDENADA MAYOR A MENOR PROBABILIDAD:")
fuente_extendida2en2_ORDENADA = ordenar_mayor_a_menor_probabilidad(fuente_extendida2en2_PROB)
print()
print("FIN DEL PROGRAMA")





##APENDICES:

    #pintar todos los valores del diccionario
#for i in fuente_freq_abs.values():
#        print(i)

    #pintar todas las claves del diccionario
#for i in fuente_freq_abs.keys():
#        print(i)

    #manejar clave y valor a la vez en un diccionario para ir por las posiciones
#for clave, valor in fuente_de_informacion.items():  
#        fuente_de_informacion[clave] = Fraction(valor, total_frecuencias)


    #fraccion es numerador/denominador
#fraccion = Fraction(1, 2) #--> 1/2
#print(fraccion)


    #logaritmo en base 2 de 100
#math.log(100,2)



#utf8stdout = open(1, 'w', encoding='utf-8', closefd=False) # fd 1 is stdout
#cadena = "ó"
#print(cadena)
#for i in fuente_freq_abs.keys():
#    print(i, file=utf8stdout)
