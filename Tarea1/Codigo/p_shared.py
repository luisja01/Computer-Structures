'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #1: Predicción de Saltos
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''

class p_shared:
    def __init__(self, bits_to_index, local_history_register_size):
        self.bits_to_index = bits_to_index    # Bits del PC a indexar
        self.local_history_register_size = local_history_register_size  # Tamaño de los registros de historia local 
        self.size_of_local_history_table = 2**bits_to_index  # Tamaño de la tabla de historia local 
        self.local_history_table = []    # Se crea la tabla de historia local 
        self.pattern_table_size = 2**local_history_register_size   # Tamanño de tabla de predicciones
        self.pattern_table = [0 for i in range(self.pattern_table_size)] # Se rellena con 0s 

        # Se rellena la tabla de hisotria local con vecotres de 0 del tamaño ingresado
        for i in range(0,self.size_of_local_history_table,1):
            x = [0] * self.local_history_register_size
            self.local_history_table.append(x)

        # Resultados de la predicción 
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

    # Información de entrada a imprimir 
    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\t\t\tP-Shared")
        print("\tEntradas en el History Table:\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia local:\t\t"+str(self.local_history_register_size))
        print("\tEntradas en el Pattern Table:\t\t\t\t"+str(2**self.local_history_register_size))

    # Método para imprimir resultados 
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

    # Método de predicción 
    def predict (self, PC):
        index = int(PC) % self.size_of_local_history_table   # Bits LSB del PC que se van a utilizar para indexar 
        local_history_entry = self.local_history_table[index] # Se encuentra la entrada indica en la historia local

        # Con el for loop se convierte los valores de los arreglos en la tabla de historia local para lugo poder indexar 
        # con ese valor en el pattern table 
        decimal_result = 0 
        cont = self.local_history_register_size-1
        for i in range (0,self.local_history_register_size,1):
            num = (local_history_entry[i])*(2**cont)
            decimal_result = decimal_result + num 
            cont-=1
 
        # Teniendo el valor en decimal ya se puede indxar en el pattern table para realizar la predicción
        pattern_table_entry = self.pattern_table[decimal_result]

        # Se realiza la predicción 
        if pattern_table_entry in [0,1]:
            return "N"
        else:
            return "T"

    def update(self, PC, result, prediction): 

        # Se realiza todo el procedimiento anterior nuevamente para encontrar la entrada en el pattern table
        index = int(PC) % self.size_of_local_history_table
        local_history_entry = self.local_history_table[index] 

        decimal_result = 0 
        cont = self.local_history_register_size-1
        for i in range (0,self.local_history_register_size,1):
            num = (local_history_entry[i])*(2**cont)
            decimal_result = decimal_result + num 
            cont-=1

        pattern_table_entry = self.pattern_table[decimal_result]

        branch_table_entry = pattern_table_entry # Simplificación del código
       
         # Se actualiza la tabla de predicciones 
        if branch_table_entry == 0 and result == "N":
            updated_branch_table_entry = branch_table_entry
            local_history_entry.append(0) # Si el resultado es 'no se toma' se añade un 0 a historia local

        elif branch_table_entry != 0 and result == "N":
            updated_branch_table_entry = branch_table_entry - 1
            local_history_entry.append(0) # Si el resultado es 'no se toma' se añade un 0 a historia local
            

        elif branch_table_entry == 3 and result == "T":
            updated_branch_table_entry = branch_table_entry
            local_history_entry.append(1)  # Si el resultado es 'se toma' se añade un 1 a historia local
            
        else:
            updated_branch_table_entry = branch_table_entry + 1
            local_history_entry.append(1) # Si el resultado es 'se toma' se añade un 1 a historia local
            
        local_history_entry.pop(0) # Se eliminal el primer elemento de la historia local 
        self.pattern_table[decimal_result] = updated_branch_table_entry # Se actualiza el pattern table con el resultado real

        #Se actualizan los contadores de resultados
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
        else:
            self.total_not_taken_pred_taken += 1

        self.total_predictions += 1
            



