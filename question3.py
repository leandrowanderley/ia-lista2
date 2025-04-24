from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Estrutura da rede (Gripe → sintomas)
model = DiscreteBayesianNetwork([
    ('Gripe', 'Febre'),
    ('Gripe', 'Tosse'),
    ('Gripe', 'DorCorpo'),
    ('Gripe', 'Congestao')
])

# 2. Tabelas de probabilidade condicional (CPDs)

# Prior de Gripe
cpd_gripe = TabularCPD(variable='Gripe', variable_card=2, values=[[0.8], [0.2]])

# Febre | Gripe
cpd_febre = TabularCPD(variable='Febre', variable_card=2,
                       values=[[0.7, 0.1],   # Febre=Não
                               [0.3, 0.9]],  # Febre=Sim
                       evidence=['Gripe'], evidence_card=[2])

# Tosse | Gripe
cpd_tosse = TabularCPD(variable='Tosse', variable_card=2,
                       values=[[0.6, 0.2],
                               [0.4, 0.8]],
                       evidence=['Gripe'], evidence_card=[2])

# Dor no corpo | Gripe
cpd_dor = TabularCPD(variable='DorCorpo', variable_card=2,
                     values=[[0.8, 0.2],
                             [0.2, 0.8]],
                     evidence=['Gripe'], evidence_card=[2])

# Congestão nasal | Gripe
cpd_congestao = TabularCPD(variable='Congestao', variable_card=2,
                           values=[[0.5, 0.1],
                                   [0.5, 0.9]],
                           evidence=['Gripe'], evidence_card=[2])

# 3. Adicionando CPDs ao modelo
model.add_cpds(cpd_gripe, cpd_febre, cpd_tosse, cpd_dor, cpd_congestao)

# Verificar consistência
assert model.check_model()

# 4. Inferência
infer = VariableElimination(model)

# Observação dos sintomas:
evidencias = {
    'Febre': 1,        # 1 = Sim
    'Tosse': 1,
    'DorCorpo': 1,
    'Congestao': 0     # 0 = Não
}

resultado = infer.query(variables=['Gripe'], evidence=evidencias)
print(resultado)
