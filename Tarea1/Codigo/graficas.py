'''
IE 0521 – Estructuras de Computadoras Digitales II
Tarea #1: Predicción de Saltos
Profesor:  Erick Carvajal Barboza, PhD
Estudiante: Luis Javier Herrrera Barrantes, B93840 
II-2022
'''

import matplotlib.pyplot as plt

# Resultados obtendios con G_Shared
# Cantidad de bits del PC a indexar
x = [4,8,12,16,20]
# Resultados para una historia global de 2 bits
y_2_gshared = [67.674,76.613,88.577,90.805,90.839]
# Resultados para una historia global de 4 bits 
y_4_gshared = [65.489,74.939,88.501,91.828, 91.914]
# Resultados para una historia global de 6 bits 
y_6_gshared = [73.050, 88.186, 92.328, 92.494]
x_6_gshared = [8,12,16,20] # evitar el caso donde los bits de historia global son mayores a los bits a indexar

# Resultados para una historia global de 8 bits 
y_8_gshared = [71.718,87.632, 92.986, 93.216]
# Resultados para una historia global de 12 bits
y_12_gshared = [86.599, 94.219, 94.593]
x_12_gshared = [12,16,20] 
# Resultados para una historia global de 16 bits  
y_16_gshared = [94.919, 95.391]
x_16_gshared = [16,20]

fig1 = plt.figure("Figure 1")
# Graficando para dos bits de hisotria global
plt.plot(x, y_2_gshared, label = "2 bits de historia global", marker = 'o')
  
# Graficando para historia global de 4 bits
plt.plot(x, y_4_gshared , label = "4 bits de historia global", marker = 'o')

# Graficando para historia global de 6 bits
plt.plot(x_6_gshared, y_6_gshared , label = "6 bits de historia global", marker = 'o')

# Graficando para historia global de 8 bits
plt.plot(x_6_gshared, y_8_gshared , label = "8 bits de historia global", marker = 'o')

# Graficando para historia global de 12 bits
plt.plot(x_12_gshared, y_12_gshared , label = "12 bits de historia global", marker = 'o')

# Graficando para historia global de 16 bits
plt.plot(x_16_gshared, y_16_gshared , label = "16 bits de historia global", marker = 'o')

# Graficando para historia global de 20 bits
plt.plot(20, 96.115, label = "20 bits de historia global", marker = 'o')

# Nombre de los ejes
plt.xlabel('Cantidad de bits del PC')
plt.ylabel('Predicciones correctas (%)')

# Titulo de la gráfica
plt.title('Rendimiento del predictor G-Shared')
plt.grid(axis='y')
plt.legend()


# Resultados obtenidos con Bimodal 
x_bimodal = [1,2,4,8,16,20,22]
y_bimodal = [62.128,64.529, 68.916, 77.874, 88.869, 88.951, 88.951]


fig2 = plt.figure("Figure 2")

# Graficando para resultados del bimodal 
plt.plot(x_bimodal, y_bimodal, marker = 'o')

# Nombre de los ejes
plt.xlabel('Cantidad de bits del PC')
plt.ylabel('Predicciones correctas (%)')

# Titulo de la gráfica
plt.title('Rendimiento del predictor Bimodal')
plt.grid(axis='y')

#2, 4, 6, 8, 12, 16, 20 hisotria local 
# Resultados obtenidos con P-Shared
x_pshared = [4,8,12,16,20]  # Bits del PC para indexar

# 2 bits de historia local
y_pshared_2b =[66.836,74.220, 84.939, 86.597, 86.692] 
# 4 bits de hisotria local
y_pshared_4b =[67.861, 75.324, 86.755, 88.252, 88.361] 
# 6 bits de hisotria local
y_pshared_6b =[68.543, 76.427, 88.027, 89.488, 89.580] 
# 8 bits de historia local
y_pshared_8b =[69.710,77.388, 89.109, 90.518, 90.589] 
# 12 bits de hisotria local
y_pshared_12b =[76.747, 82.066, 91.415, 92.584, 92.648] 
# 16 bits de historia local
y_pshared_16b =[84.616, 85.820, 92.497, 93.507, 93.559] 
# 20 bits de historia local
y_pshared_20b =[87.913,86.464, 92.391, 93.401, 93.447] 

# Grafica de resultados P-Shared
fig3 = plt.figure("Figure 3")

# Graficando para 2 bits de hisotria local
plt.plot(x_pshared, y_pshared_2b, label = "2 bits de historia local", marker = 'o')

# Graficando para 4 bits de hisotria local
plt.plot(x_pshared, y_pshared_4b, label = "4 bits de historia local", marker = 'o')

# Graficando para 6 bits de hisotria local
plt.plot(x_pshared, y_pshared_6b, label = "6 bits de historia local", marker = 'o')

# Graficando para 8 bits de hisotria local
plt.plot(x_pshared, y_pshared_8b, label = "8 bits de historia local", marker = 'o')
  
  # Graficando para 12 bits de hisotria local
plt.plot(x_pshared, y_pshared_12b, label = "12 bits de historia local", marker = 'o')
  
# Graficando para 16 bits de hisotria local
plt.plot(x_pshared, y_pshared_16b, label = "16 bits de historia local", marker = 'o')
  
# Graficando para 20 bits de hisotria local
plt.plot(x_pshared, y_pshared_20b, label = "20 bits de historia local", marker = 'o')

# Nombre de los ejes
plt.xlabel('Cantidad de bits del PC')
plt.ylabel('Predicciones correctas (%)')

# Titulo de la gráfica
plt.title('Rendimiento del predictor P-Shared')
plt.grid(axis='y')
plt.legend()


plt.show()


