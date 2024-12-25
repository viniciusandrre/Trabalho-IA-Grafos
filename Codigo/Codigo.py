from pyamaze import maze, agent, COLOR, textLabel  # Importa as classes para gerar o labirinto, o agente que o percorre, cores e texto
from queue import PriorityQueue  # Importa a fila de prioridade para a implementação do algoritmo aestrela
import time  # Para medir o tempo de execução

# Define o destino no labirinto como a célula (1,1)
destino = (1,1)

# Função heurística que calcula a estimativa de custo restante até o destino
def h_score(celula,destino):
    linhac = celula[0] # Linha da célula atual
    colunac = celula[1]  # Coluna da célula atual
    linhad = destino[0]  # Linha do destino
    colunad = destino[1] # Coluna do destino

    # Retorna a distância de Manhattan (distância em grade) entre a célula atual e o destino
    return abs(colunac - colunad) + abs(linhac - linhad)

# Implementação do algoritmo aestrela para encontrar o caminho mais curto em um labirinto
def aestrela(labirinto):
    iteracoes = 0  # Contador de iterações
    analisadas = set()  # Conjunto para armazenar todas as células visitadas

    # Inicializa os custos f e g para todas as células no labirinto

    f_score = {celula: float("inf") for celula in labirinto.grid} # Custo total estimado (f = g + h)
    g_score = {} # Custo acumulado do caminho percorrido (g)

    # Define a célula inicial como a última célula do labirinto (inferior direita)
    celula_inicial = (labirinto.rows, labirinto.cols)
    g_score[celula_inicial] = 0  # Custo acumulado inicial é 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino) # Calcula f_score inicial
    print(f_score)

    # Cria uma fila de prioridade e insere a célula inicial
    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)  # Tupla contendo f_score, heurística e a célula
    fila.put(item) # Adiciona o item à fila

    caminho = {} # Dicionário para rastrear o caminho (predecessores)

    # Enquanto houver células na fila, continua a busca
    while not fila.empty():
        iteracoes+=1
        
        # Obtém a célula de menor custo (desempacotando a tupla para pegar a célula)
        celula = fila.get()[2]

        analisadas.add(celula)  # Marca a célula como visitada
        # Se alcançou o destino, sai do loop
        if celula == destino:
            break
         # Explora as células vizinhas (Norte, Sul, Leste, Oeste)
        for direcao in "NSEW":
             # Verifica se a direção está disponível na célula atual
            if labirinto.maze_map[celula][direcao] == 1:
                linha_celula = celula[0]
                coluna_celula = celula[1]
                 # Calcula a célula vizinha com base na direção
                if direcao == "N":
                    proxima_celula = (linha_celula - 1, coluna_celula)
                elif direcao == "S":
                    proxima_celula = (linha_celula + 1, coluna_celula)
                elif direcao == "W":
                    proxima_celula = (linha_celula, coluna_celula - 1)
                elif direcao == "E":
                    proxima_celula = (linha_celula, coluna_celula + 1)

                 # Calcula os novos valores de g_score e f_score para a célula vizinha
                novo_g_score = g_score[celula] + 1  # Incrementa o custo acumulado
                novo_f_score = novo_g_score + h_score(proxima_celula, destino) # f = g + h

                  # Atualiza os scores e adiciona à fila se o novo f_score for menor
                if novo_f_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = (novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                    fila.put(item)  # Adiciona a célula vizinha à fila
                    caminho[proxima_celula] = celula # Define a célula atual como predecessora da vizinha

    # Reconstrução do caminho final do destino até a célula inicial
    caminho_final = {}

    celula_analisada = destino
    print("Celulas analisadas", len(caminho.keys())) # Exibe o número de células analisadas

       # Caminha de volta do destino até a célula inicial, construindo o caminho final
    while celula_analisada != celula_inicial:
        caminho_final[caminho[celula_analisada]] = celula_analisada
        celula_analisada = caminho[celula_analisada]
    print(f"Número de iterações realizadas: {iteracoes}")  # Exibe o número de iterações
    return caminho_final, analisadas # Retorna o caminho reconstruído e as células visitadas

# Exibição das métricas de desempenho
def exibir_metricas(tempo_execucao, eficiencia, custo_caminho, iteracoes, celulas_analisadas, total_celulas):
    print("\n--- MÉTRICAS DE DESEMPENHO ---")
    print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
    print(f"Eficiência da busca: {eficiencia:.2f}%")
    print(f"Custo do caminho encontrado: {custo_caminho} passos")
    print(f"Número de iterações: {iteracoes}")
    print(f"Células analisadas (total): {len(celulas_analisadas)}")
    print(f"Total de células no labirinto: {total_celulas}")

# Função para calcular a densidade do labirinto
def calcular_densidade(labirinto):
     # Conta o total de células no labirinto. Cada célula pode ter até 4 conexões possíveis (Norte, Sul, Leste, Oeste).
    total_celulas = len(labirinto.grid)
    caminhos = sum([sum(cell.values()) for cell in labirinto.maze_map.values()])
    densidade = (caminhos / (4 * total_celulas)) * 100  # Percentual de caminhos
    print(f"Densidade do Labirinto: {densidade:.2f}%")
    return densidade
                
# Cria um labirinto de tamanho 100x100
labirinto = maze(50,50)
labirinto.CreateMaze(theme=COLOR.light) # Gera o labirinto com caminhos e barreiras, cor do labirinto branca

# Cria o agente que percorrerá o labirinto, configurado para preencher células percorridas
agente1 = agent(labirinto, filled=True, footprints=True, color='red', shape='square')  # Principal
agente_destino = agent(labirinto, 1, 1, filled=True, color='green')  # Destino

# Executa o algoritmo aestrela para encontrar o caminho
inicio = time.time() #inicia o tempo
caminho, analisadas = aestrela(labirinto) # Recebe o caminho e as células visitadas
fim = time.time() # determina o fim do tempo

# Cálculo das métricas
tempo_execucao = fim - inicio #Determina o tempo de execução do código
total_celulas = len(labirinto.grid) #Número total de células
celulas_analisadas = len(analisadas) #Células Analisadas
eficiencia = (celulas_analisadas / total_celulas) * 100  #Eficiência da busca
custo_caminho = len(caminho) #Total de passos para o fim do labirinto

# Exibe as métricas de desempenho
exibir_metricas(
tempo_execucao = tempo_execucao,
eficiencia = eficiencia, 
custo_caminho = custo_caminho, 
iteracoes = len(analisadas), 
celulas_analisadas = analisadas, 
total_celulas =  total_celulas
)

# Calcula a densidade do labirinto
calcular_densidade(labirinto)

textLabel(labirinto, "Tempo de execução", round(tempo_execucao, 3)) #Coloca o tempo de execução na tela

# Traça o caminho no labirinto para visualização
labirinto.tracePath({agente1: caminho}, delay = 15)
labirinto.tracePath({agente_destino: []})

# Executa a visualização gráfica do labirinto com o caminho traçado
labirinto.run()