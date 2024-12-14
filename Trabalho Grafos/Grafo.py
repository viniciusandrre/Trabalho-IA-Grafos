from pyamaze import maze, agent

labirinto = maze();
labirinto.CreateMaze()

agente = agent(labirinto, filled = True, footprints= True)
caminho = "NWNWNWNWNWNWNW"
labirinto.tracePath({agente: caminho}, delay = 300)
labirinto.run()