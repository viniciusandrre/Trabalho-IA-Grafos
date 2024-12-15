from pyamaze import maze, agent
from queue import PriorityQueue

def h_score(celula,destino):
    linhac = celula[0]
    colunac = celula[1]
    linhad = destino[0]
    colunad = destino[1]
    return abs(colunac - colunad) + abs(linhac - linhad)

def aestrela(Labirinto):
    f_score = {celula: float("inf") for celula in Labirinto.grid}
    g_score = {}
    celula_inicial = (Labirinto.rows, Labirinto.cols)
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    print(f_score)

    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score[celula_inicial, destino], celula_inicial)
    fila.put(item)

    while not fila.empty():
        celula = fila.get()

        if celula == destino:
            break
        
        for direcao in "NSEW":
            if Labirinto.maze_mao[celula][direcao] == 1:
                linha_celula = celula[0]
                coluna_celula = celula[1]
                if direcao == "N":
                    proxima_celula = (linha_celula - 1, coluna_celula)
                elif direcao == "S":
                    proxima_celula = (linha_celula + 1, coluna_celula)
                elif direcao == "W":
                    proxima_celula = (linha_celula, coluna_celula - 1)
                elif direcao == "E":
                    proxima_celula = (linha_celula, coluna_celula + 1)

                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)
                
                if novo_f_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = ()
                    fila.put(novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                
            




labirinto = maze();
labirinto.CreateMaze()

agente = agent(labirinto, filled = True, footprints= True)
caminho = "NWNWNWNWNWNWNW"
labirinto.tracePath({agente: caminho}, delay = 300)
labirinto.run()