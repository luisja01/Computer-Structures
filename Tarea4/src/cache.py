'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #4: Simulador de Memoria Caché
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''
from math import log
import random
import numpy as np 

class cache:
    def __init__(self, capacidad_cache,asociatividad_cache, tamaño_bloque, politica_remplzaco ):
        self.capacidad_cache = capacidad_cache    # Capacidad total del caché
        self.asociatividad_cache = asociatividad_cache  # Cantidad de ways en cada set
        self.tamaño_bloque = tamaño_bloque # Bytes por bloque en el caché 
        self.politica_remplazo = politica_remplzaco # política utilizada para expulsar los bloques del caché 

        # otros parámetros importantes
        self.offset_size = log(tamaño_bloque,2) # tamaño de bits del offset 
        self.bloques = (capacidad_cache*1024) / tamaño_bloque # cantidad de bloques
        self.sets = self.bloques / asociatividad_cache # cantidad de sets 
        self.index_size = log(self.sets,2) # tamaño de bits del  index
        self.tag_size = 36-self.offset_size - self.index_size # tamaño de bits del tag 

        #Matriz para simular memoria caché
        self.cache_matrix = np.empty((int(self.sets),int(self.asociatividad_cache*2))) # se genera una matriz vacía 
        # se multiplica por 2 la cantidad de ways para utilizar un espacio extra de la matriz como contador de edad para cada way


        # Contadores a utilizar
        self.total_misses = 0
        self.memory_access = 0
        self.read_misses = 0 
        self.read_access = 0
        self.write_misses = 0
        self.write_access = 0
  
    # Información de entrada a imprimir 
    def print_info(self):
        print("Parámetros utilizados:")
        print("\tCapacidad del caché en kB:\t\t\t\t"+str(self.capacidad_cache))
        print("\tAsociatividad del caché:\t\t\t\t"+str(self.asociatividad_cache))
        print("\tTamaño de del bloque en bytes\t\t\t\t"+str(self.tamaño_bloque))
        print("\tPolítica de remplazo:\t\t\t\t\t"+self.politica_remplazo)

    # Método para imprimir resultados 
    def print_stats(self):
        print("Resultados de la simulación")
        print("\tCantidad total de misses:\t\t\t\t"+str(self.total_misses))
        print("\tMiss rate total (%):\t\t\t\t\t"+str((self.total_misses/self.memory_access)*100))
        print("\tCantidad de misses de lectura:\t\t\t\t"+str(self.read_misses))
        print("\tMiss rate de lectura (%):\t\t\t\t"+str((self.read_misses/self.read_access)*100))
        print("\tCantidade de misses de escritura:\t\t\t"+str(self.write_misses))
        print("\tMiss rate de escritura (%):\t\t\t\t"+str((self.write_misses/self.write_access)*100))

    # Método para implemetación del caché 
    def implementation (self, address, result):

        # Se separan las direcciones y se convierten en enteros utilizables
        tag = address[0:int(self.tag_size)]
        index = address[int(self.tag_size): int(self.tag_size+self.index_size)]
        tag_dec=int(tag,2)
        index_dec = int(index,2)

    
        # Dependiendo del resultado se aumenta el contador respectivo
        if result == 'r':
            self.read_access+=1
        elif result == 'w': 
            self.write_access+=1
    
        # Nuevo acceso a memoria
        self.memory_access+=1
        cont = 0 

        # Se recorre el set indicado por index way por way para ver si hay hit o miss
        for i in range (0,int(self.asociatividad_cache*2),2):

            if float(self.cache_matrix[index_dec,i]) == float(tag_dec): # Caso en que hay hit
                self.cache_matrix[index_dec,i+1]=0 # Se pone la edad del elemento en 0 
                for j in range (0,int(self.asociatividad_cache*2),2): # Se suma 1 a las edades del resto de elementos del set
                    if j+1 == i+1: 
                        pass
                    else:  
                        self.cache_matrix[index_dec,j+1]+=1 # Suma 1 
                break 
            else:
                cont+=1 # En caso de que no se encuentre el dato en un way se suma 
            
        if cont == int(self.asociatividad_cache): # Si cont = asociatividad significa que no encontró el dato en ningún way y hay miss
            # Se aumentan los contadores 
            self.total_misses+=1
            if result == 'r':
                self.read_misses+=1
            elif result == 'w':
                self.write_misses+=1
            
            # Caso de rempazo LRU 
            if self.politica_remplazo == 'l':
                maxi = 0

                # Se busca el way en el set específico con mayor edad 
                for i in range (0,int(self.asociatividad_cache*2),2):
                    if self.cache_matrix[index_dec,i+1] >= maxi:
                        maxi = self.cache_matrix[index_dec,i+1]
                        pos = i # Se obtiene la posición con más edad

                
                if self.asociatividad_cache == 1: # Si la asociatividad es 1 solo hay un way para victimizar
                    pos = 0
                try : 
                    self.cache_matrix[index_dec, pos] = float(tag_dec) # Se victimiza el dato viejo con el nuevo

                except UnboundLocalError: 
                    pos = 0
                    self.cache_matrix[index_dec, pos] = float(tag_dec) # Se victimiza el dato viejo con el nuevo

                self.cache_matrix[index_dec, pos+1] = 0 # Se pone la edad en 0

                # Se aumenta la edad del resto de los elementos del way en 1
                for i in range (0,int(self.asociatividad_cache*2),2):
                    if i+1 == pos+1: 
                        pass #elemento accesado se ignora 
                    else:  
                        self.cache_matrix[index_dec,i+1]+=1 # aumenta en 1

            # Caso de remplazo aleatorio 
            elif self.politica_remplazo == 'r':
                rand = random.randint(0,int(self.asociatividad_cache)-1)*2 # Se obitene número aleatorio indexable a las columnas del caché 
                
                if self.asociatividad_cache == 1: # Si la asociatividad es 1 solo hay un way para victimizar
                    rand = 0

                self.cache_matrix[index_dec,rand] = float(tag_dec) # Se remplaza el dato viejo con el nuevo 


    
