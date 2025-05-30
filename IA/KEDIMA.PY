import random

# Banco de dados simples com treinos
exercicios = {
    "aquecimento": ["Polichinelos", "Corrida no lugar", "Pular corda (simulado)", "Mobilidade articular"],
    "superior": ["Flexões", "Tríceps no banco", "Elevação lateral com garrafas", "Prancha alta"],
    "inferior": ["Agachamentos", "Afundos", "Ponte de glúteo", "Subida em degrau"],
    "abdomen": ["Abdominais", "Prancha", "Bicicleta no solo", "Elevação de pernas"],
    "alongamento": ["Toque os pés", "Alongamento de tríceps", "Círculos com os braços", "Respiração profunda"]
}

# Função principal da Kedima
def gerar_plano(duracao_min, foco):
    print("Olá! Eu sou a Kedima, sua IA de treinos em casa.")
    print(f"Criando um plano de treino de {duracao_min} minutos focado em {foco}...\n")

    plano = []

    # Aquecimento sempre presente
    plano.append("Aquecimento:")
    plano += random.sample(exercicios["aquecimento"], 2)

    # Parte principal
    if foco in exercicios:
        plano.append(f"\nExercícios de {foco.capitalize()}:")
        plano += random.sample(exercicios[foco], 3)
    else:
        plano.append("\nTreino misto:")
        plano += random.sample(
            exercicios["superior"] + exercicios["inferior"] + exercicios["abdomen"], 3
        )

    # Alongamento no final
    plano.append("\nAlongamento final:")
    plano += random.sample(exercicios["alongamento"], 2)

    # Exibir plano
    for item in plano:
        if item.endswith(":"):
            print(f"\n{item}")
        else:
            print(f"- {item}")

# Exemplo de uso:
gerar_plano(duracao_min=20, foco="abdomen")
 import random

# Banco de dados de treinos
exercicios = {
    "aquecimento": ["Polichinelos", "Corrida no lugar", "Pular corda (simulado)", "Mobilidade articular"],
    "superior": ["Flexões", "Tríceps no banco", "Elevação lateral com garrafas", "Prancha alta"],
    "inferior": ["Agachamentos", "Afundos", "Ponte de glúteo", "Subida em degrau"],
    "abdomen": ["Abdominais", "Prancha", "Bicicleta no solo", "Elevação de pernas"],
    "alongamento": ["Toque os pés", "Alongamento de tríceps", "Círculos com os braços", "Respiração profunda"]
}

def gerar_plano(duracao_min, foco):
    print("\nOlá! Eu sou a Kedima, sua IA de treinos em casa.")
    print(f"Criando um plano de treino de {duracao_min} minutos com foco em {foco}...\n")

    plano = []

    plano.append("Aquecimento:")
    plano += random.sample(exercicios["aquecimento"], 2)

    if foco in exercicios:
        plano.append(f"\nExercícios de {foco.capitalize()}:")
        plano += random.sample(exercicios[foco], 3)
    else:
        plano.append("\nTreino misto:")
        plano += random.sample(
            exercicios["superior"] + exercicios["inferior"] + exercicios["abdomen"], 3
        )

    plano.append("\nAlongamento final:")
    plano += random.sample(exercicios["alongamento"], 2)

    for item in plano:
        if item.endswith(":"):
            print(f"\n{item}")
        else:
            print(f"- {item}")

# Interação com o usuário
duracao = input("Quantos minutos você tem para treinar? ")
foco = input("Qual área deseja treinar (superior, inferior, abdomen ou misto)? ").lower()

try:
    duracao = int(duracao)
    gerar_plano(duracao, foco)
except ValueError:
    print("Por favor, digite um número válido para a duração do treino.")
