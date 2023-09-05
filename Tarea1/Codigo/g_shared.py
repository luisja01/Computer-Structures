'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #1: Predicción de Saltos
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''

class g_shared:
    def __init__(self, bits_to_index, global_history_size):
        self.bits_to_index = bits_to_index # Bits del PC a indexar
        self.global_history_size = global_history_size     # Tamaño de historia global 
        self.global_history_table = [0] * self.global_history_size # Se rellena la tabla con 0s
        self.size_of_branch_table = 2**bits_to_index   # Tamaño de la tabla de branches 
        self.branch_table = [0 for i in range(self.size_of_branch_table)]  # Se rellena tabla con 0s

        #Resultados de la predicción 
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

    # Método para imprimir información
    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\t\t\tG-Shared")
        print("\tEntradas en el Predictor:\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia global:\t\t"+str(self.global_history_size))

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
        index = int(PC) % self.size_of_branch_table # Se obtiene LSB del PC

        # Se crea este for para pasar el array de historia global a un número entero
        decimal_result = 0 
        cont = self.global_history_size-1
        for i in range (0,self.global_history_size,1):
            num = ((self.global_history_table[i])*(2**cont))
            decimal_result = decimal_result + num 
            cont-=1

        real_index = (index ^ decimal_result) # Una vez teniendo el número entero se realiza la operación XOR
    
        branch_table_entry = self.branch_table[real_index] # La entrada va a ser indexada con el resultado obtenido del XOR
    
        # Realiza la predicción 
        if branch_table_entry in [0,1]:
            return "N"
        else:
            return "T"

    def update(self, PC, result, prediction): 
        # Se vuelve a realizar todo el proceso anterior para conseguir la entrada en la tabla de predicciones
        index = int(PC) % self.size_of_branch_table

        decimal_result = 0 
        cont = self.global_history_size-1
        for i in range (0,self.global_history_size,1):
            num = ((self.global_history_table[i])*(2**cont))
            decimal_result = decimal_result + num 
            cont-=1

        real_index = (index ^ decimal_result)
        branch_table_entry = self.branch_table[real_index]

         #Actualización de la tabla
        if branch_table_entry == 0 and result == "N":
            updated_branch_table_entry = branch_table_entry
            self.global_history_table.append(0) # Si el resultado es 'no se toma' se añade un 0 a historia global

        elif branch_table_entry != 0 and result == "N":
            updated_branch_table_entry = branch_table_entry - 1
            self.global_history_table.append(0)  # Si el resultado es 'no se toma' se añade un 0 a historia global
            

        elif branch_table_entry == 3 and result == "T":
            updated_branch_table_entry = branch_table_entry
            self.global_history_table.append(1) # Si el resultado es 'se toma' se añade un 1 a historia global
            
        else:
            updated_branch_table_entry = branch_table_entry + 1
            self.global_history_table.append(1) # Si el resultado es 'se toma' se añade un 1 a historia global
            
        self.global_history_table.pop(0) # Se elimina el primer elemento del vector de historia global
        self.branch_table[real_index] = updated_branch_table_entry # Se actualiza la tabla de predicciones

        #Actualización de la estadísticas 
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
        else:
            self.total_not_taken_pred_taken += 1

        self.total_predictions += 1
            





