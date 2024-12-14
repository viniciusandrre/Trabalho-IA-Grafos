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

    



labirinto = maze();
labirinto.CreateMaze()

agente = agent(labirinto, filled = True, footprints= True)
caminho = "NWNWNWNWNWNWNW"
labirinto.tracePath({agente: caminho}, delay = 300)
labirinto.run()