'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #1: Predicción de Saltos
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''

from optparse import OptionParser
import gzip
from bimodal import *
from g_shared import *
from p_shared import * 
from torneo import * 
parser = OptionParser()
parser.add_option("-s", dest="bits_to_index")
parser.add_option("--bp", dest="branch_predictor_type")
parser.add_option("--lh", dest="local_history_size")
parser.add_option("--gh", dest="global_history_size")
parser.add_option("-t", dest="TRACE_FILE", default="./branch-trace-gcc.trace.gz")

(options, args) = parser.parse_args()

is_tournament = False
if options.branch_predictor_type == "0":
    branch_predictor = bimodal(int(options.bits_to_index))
    branch_predictor.print_info()

elif options.branch_predictor_type == '1':
    branch_predictor = g_shared(int(options.bits_to_index),int(options.global_history_size))
    branch_predictor.print_info()

elif options.branch_predictor_type == '2':
    branch_predictor = p_shared(int(options.bits_to_index),int(options.local_history_size))
    branch_predictor.print_info()

elif options.branch_predictor_type == '3':
    branch_predictor = torneo(int(options.bits_to_index),int(options.global_history_size),int(options.local_history_size), )
    branch_predictor.print_info()

with gzip.open(options.TRACE_FILE,'rt') as trace_fh:
    for line in trace_fh:
        line = line.rstrip()
        PC,result = line.split(" ")
        if is_tournament:
            branch_predictor.predict_and_update(PC, result)
        else:
            prediction = branch_predictor.predict(PC)
            branch_predictor.update(PC, result, prediction)

branch_predictor.print_stats()
