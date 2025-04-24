# Letra A

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperatura = ctrl.Antecedent(np.arange(0, 71, 1), 'temperatura')
fluxo = ctrl.Antecedent(np.arange(0, 61, 1), 'fluxo')
abertura = ctrl.Consequent(np.arange(0, 101, 1), 'abertura')

temperatura['baixa'] = fuzz.trimf(temperatura.universe, [0, 0, 30])
temperatura['media'] = fuzz.trimf(temperatura.universe, [20, 35, 50])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [40, 70, 70])

fluxo['baixo'] = fuzz.trimf(fluxo.universe, [0, 0, 20])
fluxo['medio'] = fuzz.trimf(fluxo.universe, [10, 30, 40])
fluxo['alto'] = fuzz.trimf(fluxo.universe, [30, 60, 60])

abertura['pequena'] = fuzz.trimf(abertura.universe, [0, 0, 30])
abertura['moderada'] = fuzz.trimf(abertura.universe, [20, 50, 70])
abertura['grande'] = fuzz.trimf(abertura.universe, [60, 100, 100])

# Letra B
rule1 = ctrl.Rule(temperatura['baixa'] & fluxo['alto'], abertura['grande'])
rule2 = ctrl.Rule(temperatura['baixa'] & fluxo['medio'], abertura['moderada'])
rule3 = ctrl.Rule(temperatura['media'] & fluxo['alto'], abertura['moderada'])
rule4 = ctrl.Rule(temperatura['media'] & fluxo['baixo'], abertura['pequena'])
rule5 = ctrl.Rule(temperatura['alta'] & fluxo['baixo'], abertura['pequena'])
rule6 = ctrl.Rule(temperatura['alta'] & fluxo['alto'], abertura['moderada'])

sistema_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

sistema.input['temperatura'] = 25
sistema.input['fluxo'] = 50
sistema.compute()

print(f"Abertura da válvula: {sistema.output['abertura']:.2f}%")
abertura.view(sim=sistema)
