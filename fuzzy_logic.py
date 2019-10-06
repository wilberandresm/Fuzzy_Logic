import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Antecedentes/entradas
tamano = ctrl.Antecedent(np.arange(0, 11, 1), 'tamano')
distancia = ctrl.Antecedent(np.arange(0, 11, 1), 'distance')
precio = ctrl.Consequent(np.arange(0, 26, 1), 'precio')

#conjuntos difusos con sus especificaciones
tamano['pequeña']=fuzz.trapmf(tamano.universe,[40,60,80,90])#trapezoidal
tamano['mediana']=fuzz.trapmf(tamano.universe,[80,100,200,220])
tamano['grande']=fuzz.trapmf(tamano.universe,[180,400,600,810])

distancia['cerca del centro historico']=fuzz.trimf(distancia.universe,[1,4,7])#triangular
distancia['lejos del centro historico']=fuzz.trimf(distancia.universe,[5,10,12])
distancia['afueras de cartagena']=fuzz.trimf(distancia.universe,[11,13,16])

precio['bajo']=fuzz.trapmf(precio.universe,[60,70,80,90])
precio['medio']=fuzz.trapmf(precio.universe,[80,120,150,200])
precio['alto']=fuzz.trapmf(precio.universe,[180,200,600,3050])