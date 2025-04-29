
case_base = [
    {
        "symptoms": { "febre", "tosse", "fadiga" },
        "disease": "Gripe",
        "treatment": "Repouso, hidratação e antitérmicos"
    },
    {
        "symptoms": { "dor de cabeça", "náusea", "rigidez no pescoço" },
        "disease": "Meningite",
        "treatment": "Hospitalização e antibióticos intravenosos"
    },
    {
        "symptoms": { "dor abdominal", "diarreia", "náusea" },
        "disease": "Gastroenterite",
        "treatment": "Hidratação e dieta leve"
    },
    {
        "symptoms": { "tosse", "falta de ar", "dor no peito" },
        "disease": "Pneumonia",
        "treatment": "Antibióticos e repouso"
    }
]

def retrieve_case(reported_symptoms, case_base):
    best_matches = []
    for case in case_base:
        case_symptoms = case["symptoms"]
        intersection = reported_symptoms & case_symptoms
        score = len(intersection) / len(case_symptoms)
        best_matches.append((score, case))
    
    best_matches.sort(reverse=True, key=lambda x: x[0])
    return best_matches[0]

def diagnose(patient_symptoms):
    symptoms = set(patient_symptoms)
    score, case = retrieve_case(symptoms, case_base)
    
    print("Sintomas do paciente:", ", ".join(symptoms))
    print("Diagnóstico sugerido:", case["disease"])
    print("Tratamento recomendado:", case["treatment"])
    print(f"Similaridade com o caso recuperado: {score:.2f}")


diagnose(["tosse", "febre", "fadiga"])