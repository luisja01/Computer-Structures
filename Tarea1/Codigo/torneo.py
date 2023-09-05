'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #1: Predicción de Saltos
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''


# Se inluyen los predictores a utilizar 
from g_shared import *
from p_shared import * 

class torneo:
    def __init__(self, bits_to_index, global_history_size,local_history_register_size):
        self.bits_to_index = bits_to_index
        self.global_history_size = global_history_size
        self.local_history_register_size = local_history_register_size
        # Se definen las clases de los predictores 
        self.g_shared = g_shared(bits_to_index, global_history_size)
        self.p_shared = p_shared(bits_to_index, local_history_register_size)
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

        #Contador de torneo
        self.contador = 0

   # Método para imprimir resultados 
    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\t\t\tTorneo")
        print("\tSobre el predictor Global:\t")
        print("\tEntradas en el Predictor:\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia global:\t\t"+str(self.global_history_size))
        print("\tSobre el predictor Local:\t")
        print("\tEntradas en el History Table:\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia local:\t\t"+str(self.local_history_register_size))
        print("\tEntradas en el Pattern Table:\t\t\t\t"+str(2**self.local_history_register_size))

    # Método para imprimir estadísticas de resultados 
    def print_stats(self):
        print("Resultados de la simulación")
        print("\t# branches:\t\t\t\t\t\t"+str(self.total_predictions))
        print("\t# branches tomados predichos correctamente:\t\t"+str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente:\t\t"+str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente:\t\t"+str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente:\t"+str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken+self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas:\t\t\t\t"+str(formatted_perc)+"%")


    def predict_and_update (self, PC, result):

        # Se hacen las debidas predicciones con cada método
        pred_global = self.g_shared.predict(PC)
        pred_local = self.p_shared.predict(PC)

        # En caso de que el contador se encuentre en G-Share como método de predicción
        if self.contador == 1 or self.contador == 0:
            if result == "T" and result == pred_global:
                self.total_taken_pred_taken += 1
            elif result == "T" and result != pred_global:
                self.total_taken_pred_not_taken += 1
            elif result == "N" and result == pred_global:
                self.total_not_taken_pred_not_taken += 1
            else:
                self.total_not_taken_pred_taken += 1

        # En caso de que el contador se encuentre en P-Share como método de predicción
        else:
            if result == "T" and result == pred_local:
                self.total_taken_pred_taken += 1
            elif result == "T" and result != pred_local:
                self.total_taken_pred_not_taken += 1
            elif result == "N" and result == pred_local:
                self.total_not_taken_pred_not_taken += 1
            else:
                self.total_not_taken_pred_taken += 1
        
        self.total_predictions += 1 # Se aumenta total de predicciones 

        # Se actualiza el contador
        if pred_global == pred_local:
            self.contador = self.contador

        elif self.contador == 0 and result == pred_global:
            self.contador = 0

        elif self.contador != 0 and result == pred_global:
            self.contador -= 1

        elif self.contador ==3 and result == pred_local:
            self.contador = 3

        else:
            self.contador+=1

        # Se actualizan los predictores
        self.g_shared.update(PC, result, pred_global)
        self.p_shared.update(PC, result, pred_local)
