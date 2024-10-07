# Definição dos nós e suas conexões com os respectivos valores
graph = {
    'C1': [('C2', 120), ('C3', 150), ('C4', 250)],
    'C2': [('C5', 270)],
    'C3': [('C5', 300)],
    'C4': [('C5', 490)],
    'C5': [('C6', 550)],
    'C6': []
}

# Definição dos valores nos nós
node_values = {
    'C1': 0,
    'C2': 270,
    'C3': 270,
    'C4': 490,
    'C5': 520,  # Aqui considerando que pode variar dependendo do caminho
    'C6': 550
}

# Função para encontrar o melhor caminho com base nas condições
def find_best_path(graph, start, end, node_values):
    best_path = []
    current_node = start
    current_value = node_values[current_node]

    while current_node != end:
        best_next_node = None
        best_value = float('-inf')  # Para garantir que qualquer valor será maior

        # Verifica as conexões do nó atual
        for next_node, discount in graph[current_node]:
            # Calcula o valor final no próximo nó considerando o desconto
            next_value = node_values[next_node] - discount

            # Apenas escolhe o caminho se for melhor
            if next_value > best_value:
                best_value = next_value
                best_next_node = next_node

        if best_next_node:
            best_path.append((current_node, best_next_node, best_value))
            current_node = best_next_node
        else:
            break  # Se não encontrar próximo nó, finaliza

    return best_path

# Execução do algoritmo para encontrar o melhor caminho de C1 até C6
best_path = find_best_path(graph, 'C1', 'C6', node_values)
print("Melhor caminho encontrado:")
for step in best_path:
    print(f"{step[0]} -> {step[1]} com valor: {step[2]}")
