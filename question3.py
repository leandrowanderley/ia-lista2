from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Gripe', 'Febre'),
    ('Gripe', 'Tosse'),
    ('Gripe', 'DorCorpo'),
    ('Gripe', 'Congestao')
])

cpd_gripe = TabularCPD(variable='Gripe', variable_card=2, values=[[0.8], [0.2]])

cpd_febre = TabularCPD(variable='Febre', variable_card=2,
                       values=[[0.7, 0.1],
                               [0.3, 0.9]],
                       evidence=['Gripe'], evidence_card=[2])

cpd_tosse = TabularCPD(variable='Tosse', variable_card=2,
                       values=[[0.6, 0.2],
                               [0.4, 0.8]],
                       evidence=['Gripe'], evidence_card=[2])

cpd_dor = TabularCPD(variable='DorCorpo', variable_card=2,
                     values=[[0.8, 0.2],
                             [0.2, 0.8]],
                     evidence=['Gripe'], evidence_card=[2])

cpd_congestao = TabularCPD(variable='Congestao', variable_card=2,
                           values=[[0.5, 0.1],
                                   [0.5, 0.9]],
                           evidence=['Gripe'], evidence_card=[2])

model.add_cpds(cpd_gripe, cpd_febre, cpd_tosse, cpd_dor, cpd_congestao)

assert model.check_model()

infer = VariableElimination(model)

evidencias = {
    'Febre': 1,
    'Tosse': 1,
    'DorCorpo': 1,
    'Congestao': 0
}

resultado = infer.query(variables=['Gripe'], evidence=evidencias)
print(resultado)
