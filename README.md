# *Planejamento de Rotas com Algoritmo A\**

### *Projeto da disciplina de Inteligência Artificial*

**Integrantes:**  
*Ana Clara Araujo da Cruz*  
*Cauã Veloso Oliveira*  
*Thalita Muniz Amorim*  

**Professor:** *Alex Oliveira Barradas Filho*

---

## *Descrição do Projeto*

Este projeto implementa um sistema de *planejamento de rotas com trânsito* utilizando o algoritmo **A\*** do NetworkX.  
As cidades são modeladas como nós de um grafo, e as estradas são representadas por arestas contendo:

- *Tempo base de viagem*
- *Penalidades de trânsito*
- *Peso final (tempo total)*

O objetivo é determinar o *caminho mais rápido* entre duas cidades, mesmo quando a rota mais curta fisicamente não é a mais eficiente devido a congestionamentos.  
A heurística utilizada pelo A\* é a *distância euclidiana*, permitindo uma busca mais rápida e informada.

---

## *Tecnologias Utilizadas*

- *Python 3*
- *NetworkX* — construção e análise do grafo
- *Matplotlib* — visualização do mapa de rotas
- *Algoritmo A\** — busca do caminho ótimo

---

## *Como Executar o Projeto*

### **1. Instale as dependências**

```bash
pip install networkx matplotlib
```

---
### **2. Executar o programa**

```bash
python nome_do_arquivo.py
```

### **3. Selecionar opção no menu**

- *1 — Executar sem trânsito*
- *2 — Executar com trânsito simulado*

Ao rodar o programa, serão exibidos:

Melhor caminho
Custo total da rota
Gráfico mostrando a rota ótima em verde

---

## *Funcionamento do Algoritmo A*

- *O A* combina:*
- *G(n)* — custo acumulado
- *H(n) — distância euclidiana até o destino
- *F(n) = G(n) + H(n) — custo estimado total

Essa estrutura permite que o algoritmo explore caminhos promissores e evite rotas ruins.

---
## *Objetivo Acadêmico*

Este projeto foi desenvolvido para:
- *Compreender modelagem de grafos*
- *Aplicar o algoritmo A**
- *Simular trânsito como penalidades de arestas*
- *Comparar rotas com e sem congestionamento*
- *Visualizar a resposta do algoritmo*
- *Demonstração em Vídeo*

No vídeo são apresentados:
- *O problema*
- *A modelagem em grafo*
- *A implementação do A**
- *A execução prática*
- *Limitações e possíveis melhorias*

Link do vídeo: (adicionar após upload)
