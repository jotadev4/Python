import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Classe para representar um nó na árvore binária
class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.left = None   # Ponteiro para o filho da esquerda
        self.right = None  # Ponteiro para o filho da direita

def bfs_tree(root):
    """Função para realizar a busca em largura na árvore e retornar as arestas."""
    if root is None:
        return []

    queue = deque([root])
    bfs_edges = []

    while queue:
        node = queue.popleft()
        if node.left:
            bfs_edges.append((node.data, node.left.data))
            queue.append(node.left)
        if node.right:
            bfs_edges.append((node.data, node.right.data))
            queue.append(node.right)

    return bfs_edges

def bfs_grafo():
    """Função para realizar o BFS e desenhar o grafo."""
    G = nx.DiGraph()
    G.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (3, 7)])
    
    # Realizar a busca em largura (BFS) a partir do nó 0
    bfs_edges = list(nx.bfs_edges(G, 0))
    print("BFS Tree Edges:", bfs_edges)

    # Calcular o layout apenas uma vez
    pos = nx.spring_layout(G)

    # Desenhar o grafo
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=16)
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='red', width=2)

    # Mostrar a visualização
    plt.title("Busca em Largura (BFS) no Grafo")
    plt.show()

# Esta classe representa um grafo direcionado usando representação de lista de adjacência
class Grafo:
    def __init__(self, V):
        self.V = V  # Número de vértices
        self.adj = [[] for _ in range(V)]  # Listas de adjacência

    def adicionarAresta(self, v, w):
        self.adj[v].append(w)

    def BFS(self, s):
        fila = deque()
        visitado = [False] * self.V
        visitado[s] = True
        fila.append(s)

        caminho = []  # Lista para armazenar o caminho das arestas

        while fila:
            atual = fila.popleft()
            if caminho:  # Se já temos um caminho, adiciona um "-"
                caminho.append("-")
            caminho.append(chr(atual + 65))  # Adiciona a letra do vértice ao caminho

            for i in self.adj[atual]:
                if not visitado[i]:
                    fila.append(i)
                    visitado[i] = True

        return ''.join(caminho)

    def BFS_completo(self):
        visitados = [False] * self.V
        caminhos = []
        for i in range(self.V):
            if not visitados[i]:
                caminho = self.BFS(i)
                if caminho:
                    caminhos.append(f"Caminho a partir de {chr(i + 65)}: {caminho}")
                    visitados[i] = True
        return caminhos

def soma_vetores(v1, v2, tam):
    for i in range(min(len(v1), tam)):
        v1[i] += v2[i]  # Soma cumulativa dos vetores

def main():
    # Cria um grafo com 26 vértices (A até Z)
    g = Grafo(26)

    # Exemplo de arestas (A até Z)
    edges = [
        (0, 1), (0, 2), (1, 3), (2, 4), (2, 5),
        (6, 7), (8, 9), (10, 11), (12, 13), (14, 15)
    ]
    
    for v, w in edges:
        g.adicionarAresta(v, w)

    # Solicita o número de semanas
    while True:
        try:
            semana = int(input("Digite o número de semanas: "))
            if semana <= 0:
                print("Por favor, insira um número de semanas maior que 0.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.")

    # Inicializa os vetores com tamanho apropriado
    vetor = [0.0] * semana
    soma = [0.0] * semana

    # Leitura dos valores dos vetores e soma cumulativa
    for i in range(semana):
        while True:
            try:
                print(f"Digite os valores da semana {chr(i + 65)} (separados por espaço): ")
                valores = list(map(float, input().split()))
                vetor[:len(valores)] = valores
                soma_vetores(soma, vetor, i + 1)
                break
            except ValueError:
                print("Por favor, insira valores numéricos separados por espaço.")

    # Encontrar o valor máximo
    semana_maximo = max(range(semana), key=lambda i: soma[i])
    maximo = soma[semana_maximo]

    # Imprimir o resultado
    print(f"O valor máximo da soma é: {maximo:.2f}")
    print(f"Ocorreu na semana: {semana_maximo + 1}")

    # Realiza a BFS completa e imprime caminhos
    caminhos = g.BFS_completo()
    for caminho in caminhos:
        print(caminho)

    # Criar e desenhar a árvore binária
    root = Node(5)
    root.left = Node(12)
    root.right = Node(7)
    root.left.left = Node(18)
    root.left.left.left = Node(4)
    root.left.left.right = Node(13)
    root.right.right = Node(69)

    # Obter as arestas da BFS da árvore
    bfs_tree_edges = bfs_tree(root)
    print("BFS Tree Edges:", bfs_tree_edges)

    # Criar um grafo para a árvore binária
    tree_graph = nx.DiGraph()
    for edge in bfs_tree_edges:
        tree_graph.add_edge(edge[0], edge[1])

    # Visualizar a árvore binária
    pos = nx.spring_layout(tree_graph)
    nx.draw(tree_graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
    plt.title("Árvore Binária BFS")
    plt.show()

    # Chamar a função para realizar e visualizar o BFS usando networkx
    bfs_grafo()

if __name__ == "__main__":
    main()
