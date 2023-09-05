En este documento se incluyen los comandos a ejecutar en la terminal de Linux para poder correr los ejemplos que se muestran en el enunciado de la Tarea #1.


Para correr el predictor Bimodal ejecutar la siguiente línea en terminal:

python3 branch_predictor.py --bp 0 -s 8


Para correr el predictor G-Shared ejecutar la siguiente línea en terminal:

python3 branch_predictor.py --bp 1 -s 12 --gh 6


Para correr el predictor P-Shared ejecutar la siguiente línea en terminal:

python3 branch_predictor.py --bp 2 -s 8 --lh 12


Para correr el predictor de torneo primero se debe ir al código 'branch_predictor.py' en la línea 24.
Ahí se debe cambiar la variable 'is_tournament = False' a 'is_tournament = True'. 
Una vez realizado el cambio anterior se debe ejecutar la siguiente línea en terminal:

python3 branch_predictor.py --bp 3 -s 12 --lh 12 --gh 6


Por último, si se desea visualizar las gráficas utilizadas en el reporte se debe escribir en terminal:
(es necesario tener la bilbioteca MatPlotLib instalada para correr el código y que funcione)

python3 graficas.py