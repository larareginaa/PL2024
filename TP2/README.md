### **TPC2**: Conversor de MD para HTML
### **Autor**: Lara Regina da Silva Pereira, A100556

------------------------------------------------------------------------------

# Enunciado

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/):

### Cabeçalhos
- Linhas iniciadas por "# texto", ou "## texto" ou "### texto"
    ```markdown
    # Exemplo
    ```
    ```html 
    <h1>Exemplo</h1> 
    ```

### Bold
- Pedaços de texto entre "**"
    ```markdown 
    Este é um **exemplo** ...
    ```
    ```html
    Este é um <b>exemplo</b> ...
    ```

### Itálico
- Pedaços de texto entre "*"
    ```markdown
    Este é um *exemplo* ...
    ``` 
    ```html
    Este é um <i>exemplo</i> ...
    ```

### Lista numerada
- Listas com numeração
    ```markdown
    1. Primeiro item
    2. Segundo item
    3. Terceiro item
    ```
    ```html
    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>
    ```

### Link
- [texto](endereço URL)
    ```markdown
    Como pode ser consultado em [página da UC](http://www.uc.pt)
    ```
    ```html
    Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
    ```

### Imagem
- ![texto alternativo](path para a imagem)
    ```markdown
    Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
    ```
    ```html
    Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
    ```

------------------------------------------------------------------------------

# Proposta de resolução

## Estratégia

Para converter um texto em formato MarkDown para um texto em formato HTML será necessário a substituição das expressões sintáticas características do primeiro formato para as equivalentes no segundo. Tais substituições foram efetuadas pela função ```sub``` da biblioteca ```re``` de Python, que identifica as ocorrências de uma dada expressão e as substitui por uma outra expressão especificada.

## Input/Output

O nome do ficheiro contento o texto em MarkDown deve ser passado como argumento na linha de comando, seguido do nome do ficheiro HTML onde deverá ser escrito o resultado da conversão. 

```bash
python3.12 tpc2.py teste.md resultado.html
```

## Substituições Sintáticas

### **Expressões Identificadoras**

| Sintaxte | RegEx identificadora | Descrição |
|    :-:   |          :-:         |    -      |
| **Cabeçalhos** | `(#+) +(.+)` | `(#+)` - um ou mais `#` (grupo 1)<br> ` +` - correspondência com um ou mais espaços em branco <br>`(.+)` - um ou mais caracteres na mesma linha (grupo 2)|
| **Negrito (Bold)** | `\*\*\(.*)\*\*\` | `\*\*\` - correspondência com duas ocorrências de `*`<br>`(.+)` - um ou mais de caracteres na mesma linha (grupo 1)  <br>`\*\*\` - correspondência com duas ocorrências de `*`|
| **Itálico** | `\*(.+)\*` | `\*` - correspondência com uma ocorrência de `*`<br>`(.+)` - um ou mais de caracteres na mesma linha (grupo 1)<br>`\*` - correspondência com uma ocorrência de `*`|
| **Lista Numerada** | `^\d+\. (.*)$` e `((<li>.+</li>)+)` | `^\d+\. ` - linha que inicia com um ou mais dígitos, seguidos de um ponto e de um espaço <br>`(.*)$` - linha que, antes de terminar, corresponde a zero ou mais caracteres (grupo 1) <br> `(<li>.+</li>)+` com `flags=re.MULTILINE` - correspondência com conjunto de linhas que iniciam com `<li>`, seguido de um ou mais caracteres, seguidos de `<li\>`|
| **Link** | `\[(.*)\]\((.*)\)` | `\[(.*)\]` - correspondência com `[` seguido de zero ou mais caracteres (grupo 1), finalizando com `]`<br> `\((.*)\)` - correspondência com `(` seguido de zero ou mais caracteres (grupo 2), finalizando com `)`|
| **Imagem** | `!\[(.*)\]\((.*)\)` | `!\[(.*)\]` - correspondência com `![` seguido de zero ou mais caracteres (grupo 1), finalizando com `]`<br> `\((.*)\)` - correspondência com `(` seguido de zero ou mais caracteres (grupo 2), finalizando com `)`|

### **Expressões Substitutas**

| Sintaxte | Expressão substituta | Descrição |
|    :-:   |          :-:         |    -      |
| **Cabeçalhos** | `f"<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>"` | `<h` seguido do número de caracteres presentes no grupo 1 (número de carcateres `#`), seguido de `>`, conteúdo do grupo 2 (texto do cabeçalho), seguido de `</h`, número de caracteres presentes no grupo 1 (número de carcateres `#`) e por fim `>`  (função `cabecalho`)|
| **Negrito (Bold)** | `r'<b>\1</b>'` | Caracteres `<b>` rodeiam o grupo 1 (texto a colocar a negrito)|
| **Itálico** | `r'<i>\1</i>'` | Caracteres `<i>` rodeiam o grupo 1 (texto a colocar a itálico)|
| **Lista Numerada** | `r'<li>\1</li>'` e `f"<ol>\n\t{"\n\t".join([i for i in match.group(1).split('\n')])}\n</ol>"` | Caracteres `<li>` rodeiam o grupo 1 (cada tópico da lista) <br>Caracteres `<ol>`, seguidos de `\n\t`, seguidos do conjunto de linhas da lista numerada intercaladas por `\n\t`, terminando com `\n</o<` (função `lista`) |
| **Link** | `r'<a href="\2">\1</a>'` | Caracteres `<a href=`, seguidos do grupo 2 (endereço URL) entre `"`, seguido de `>` e do grupo 1 (nome do link), finalizando com `</a>`|
| **Imagem** | `r'<img src="\2" alt=\"\1\"/>'` | Caracteres `<img src=`, seguidos do grupo 2 (caminho para a imagem) entre `"`, seguido de um espaço em branco, de `alt=` e do grupo 1 (nome do link), finalizando com `</a>` |

------------------------------------------------------------------------------