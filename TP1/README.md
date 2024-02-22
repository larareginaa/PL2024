### **TPC1**: Análise de um *dataset*
### **Autor**: Lara Regina da Silva Pereira, A100556

------------------------------------------------------------------------------

# Enunciado

1. Proibido usar o módulo CSV;
2. Ler o dataset, processá-lo e criar os seguintes resultados:
    - **Problema 1**: Lista ordenada alfabeticamente das modalidades desportivas;
    - **Problema 2**: Percentagens de atletas aptos e inaptos para a prática desportiva;
    - **Problema 3**: Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos : ... [30-34], [35-39], ...)

------------------------------------------------------------------------------

# Proposta de resolução

## Processamento de informação

### ***Parsing***

A solução deste problema deverá começar pela leitura dos dados do ficheiro ```emd.csv```. O processo de *parsing* do ficheiro será iniciado pela função ```readlines```, que devolverá uma lista com as várias linhas do ficheiro. 

De seguida, a função ```processar_dados``` irá iterar sobre a lista de linhas e, para cada uma, extrair os vários elementos de dados, delimitados por vírgulas, com a função ```split``` da biblioteca ```re```. Desta lista, serão selecionados os elementos de dados atómicos relevantes para os problemas, através da sua posição na lista. Será ainda usada a função ```strip``` para eliminar eventuais *whitespaces* iniciais e finais.

### **Armazenamento de dados**

Ainda durante o processamento de informação, à medida que vão sendo extraídos os elemento de dados relevante para os problemas, serão atualizadas as informações das estruturas de dados previamente inicializadas.

- **Problema 1**: Serão armazenado num Conjunto as várias modalidades praticadas pelos atletas registados no ficheiro. A estrutura escolhida permite evitar o armazenamento de elementos repetidos e permite a sua fácil ordenação.

- **Problema 2**: Os dados serão armazenados num Dicionário com duas entradas, para o número de atletas aptos e inaptos para a prática desportiva, respetivamente.

- **Problema 3**: Será inicializado um Dicionário com valores ```0```, cujas chaves correspondem às faixas etárias dos vários atletas. Para cada atleta, será calculado o escalão etário a que pertence a partir da sua idade. 

## Obtenção dos Resultados

Finalmente, serão utilizadas as três estruturas para obter os resultados finais dos problemas. O Conjunto de modalidades será ordenado alfabeticamente (**Problema 1**). As percentagens dos atletas aptos e inaptos para a prática desportiva serão calculadas com base no número total de atletas registados (**Problema 2**). Finalmente, os pares chave-valor do dicionário de escalões indicará a distribuição dos atletas por escalão etário (**Problema 3**). Estes resultados irão gerar o output do programa na função ```imprimir_outputs```.

------------------------------------------------------------------------------
