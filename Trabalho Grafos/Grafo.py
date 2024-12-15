from pyamaze import maze, agent  # Importa as classes para gerar o labirinto e o agente que o percorre
from queue import PriorityQueue  # Importa a fila de prioridade para a implementação do algoritmo aestrela

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

        # Obtém a célula de menor custo (desempacotando a tupla para pegar a célula)
        celula = fila.get()[2]
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
    return caminho_final  #Retorna o caminho reconstruído
                
# Cria um labirinto de tamanho 100x100
labirinto = maze(100,100)
labirinto.CreateMaze() # Gera o labirinto com caminhos e barreiras

# Cria o agente que percorrerá o labirinto, configurado para preencher células percorridas
agente1 = agent(labirinto, filled=True, footprints=True, color='red')  # Principal
agente_destino = agent(labirinto, 1, 1, filled=True, color='green')  # Destino

# Executa o algoritmo aestrela para encontrar o caminho
caminho = aestrela(labirinto)

# Traça o caminho no labirinto para visualização
labirinto.tracePath({agente1: caminho}, delay = 10)
labirinto.tracePath({agente_destino: []})

# Exibe informações das células analisadas
print("Células analisadas:", len(caminho.keys()))
# Exibe o número total de células no labirinto com o destino
print("Total de celulas", len(labirinto.maze_map.keys()))

# Executa a visualização gráfica do labirinto com o caminho traçado
labirinto.run()