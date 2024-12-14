from pyamaze import maze, agent

def h_score(celula,destino):
    linhac = celula[0]
    colunac = celula[1]
    linhad = destino[0]
    return abs(colunac - colunad) + abs(linhac - linhad)

labirinto = maze();
labirinto.CreateMaze()

agente = agent(labirinto, filled = True, footprints= True)
caminho = "NWNWNWNWNWNWNW"
labirinto.tracePath({agente: caminho}, delay = 300)
labirinto.run()