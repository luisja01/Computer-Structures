'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #4: Simulador de Memoria Caché
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''

from optparse import OptionParser
import gzip
from cache import *

 
parser = OptionParser()
parser.add_option("-s", dest="capacidad_cache")
parser.add_option("-a", dest="asociatividad_cache")
parser.add_option("-b", dest="tamaño_bloque")
parser.add_option("-r", dest="politica_remplazo")
parser.add_option("-t", dest="TRACE_FILE", default="./traces/465.tonto-1769B.trace.txt.gz")

(options, args) = parser.parse_args()



memoria_cache = cache(int(options.capacidad_cache), int(options.asociatividad_cache), int(options.tamaño_bloque), str(options.politica_remplazo))

memoria_cache.print_info()


with gzip.open(options.TRACE_FILE,'rt') as trace_fh:
    for line in trace_fh:
        line = line.rstrip()
        result,address = line.split(" ")
        decimal = int(address, 16)
        binary=format(decimal,'036b')
        memoria_cache.implementation(binary,result)


memoria_cache.print_stats()
