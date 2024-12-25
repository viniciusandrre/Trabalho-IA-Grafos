# A* Maze Solver

Este projeto implementa o algoritmo **A*** para encontrar o caminho mais curto em um labirinto gerado aleatoriamente. Ele utiliza a biblioteca `pyamaze` para criar e visualizar o labirinto, além de exibir métricas de desempenho como tempo de execução, eficiência da busca e o custo do caminho encontrado.

## Funcionalidades
- Geração de labirintos aleatórios de tamanho definido.
- Implementação do algoritmo **A*** para encontrar o caminho mais curto.
- Visualização gráfica do labirinto, incluindo o caminho encontrado.
- Cálculo e exibição de métricas de desempenho:
  - **Tempo de execução**
  - **Eficiência da busca**
  - **Custo do caminho encontrado**

## Requisitos
- Python 3.6+
- Biblioteca `pyamaze`
- Biblioteca `queue` (inclusa por padrão no Python)
- Biblioteca `time` (inclusa por padrão no Python)

## Como executar o programa
1. Clone o repositório ou copie o arquivo principal para o seu ambiente local.
2. Instale a biblioteca `pyamaze` se ainda não estiver instalada:
   ```bash
   pip install pyamaze
   ```
3. Execute o script em um ambiente Python compatível:
   ```bash
   python Grafo.py
   ```

## Estrutura do código

### Algoritmo A*
O algoritmo utiliza uma combinação do custo acumulado (gâ) e da heurística (h) para priorizar o processamento das células mais promissoras. A heurística padrão é a **distância Manhattan**:
```python
abs(celula[0] - destino[0]) + abs(celula[1] - destino[1])
```
O código também utiliza uma fila de prioridade para organizar as células com base nos custos estimados (f = g + h).

### Geração do labirinto
O labirinto é gerado usando a função `CreateMaze` da biblioteca `pyamaze`.

Exemplo:
```python
labirinto = maze(10, 10)
labirinto.CreateMaze()
```

### Visualização
O caminho encontrado pelo algoritmo é traçado no labirinto usando a função `tracePath`. A visualização inclui agentes que percorrem o labirinto:
- Um agente principal (vermelho) que segue o caminho encontrado.
- Um agente destino (verde) para marcar o ponto final.

### Métricas de desempenho
O programa calcula as seguintes métricas:
- **Tempo de execução**: Calculado com a biblioteca `time`.
- **Eficiência da busca**: Proporção entre o custo do caminho e o total de células analisadas.
- **Custo do caminho encontrado**: Número total de passos no caminho final.

Essas informações são exibidas no terminal e/ou diretamente no mapa usando `textLabel` (se suportado pela versão do `pyamaze`).

## Exemplo de Saída

```plaintext
--- MÉTRICAS DE DESEMPENHO ---
Tempo de execução: 0.0874 segundos
Eficiência da busca: 29.72%
Custo do caminho encontrado: 2972 passos
Número de iterações: 8415
Células analisadas (total): 8415
Total de células no labirinto: 10000
```

## Personalizações
- **Alterar tamanho do labirinto**: Modifique os parâmetros do construtor da classe `maze`.
  ```python
  labirinto = maze(20, 20)
  ```
- **Alterar heurística**: Substitua a função `h_score` para usar uma distância Euclidiana ou outra métrica.
  ```python
  def h_score(celula, destino):
      return ((celula[0] - destino[0])**2 + (celula[1] - destino[1])**2)**0.5
  ```
- **Mudar a visualização**: Ajuste o delay na função `tracePath` para tornar a animação mais rápida ou mais lenta.
  ```python
  labirinto.tracePath({agente1: caminho}, delay=5)
  ```

## Limitações
- O desempenho pode ser afetado em labirintos muito grandes ou densos.
- A visualização pode ser lenta se o delay não for ajustado adequadamente.

## Contribuições
Contribuições são bem-vindas! Caso deseje melhorar o projeto ou adicionar funcionalidades, abra um pull request ou relate um problema.

## Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

