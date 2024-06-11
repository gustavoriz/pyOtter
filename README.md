# pyOtter
<img src='https://github.com/gustavoriz/pyOtter/blob/b4a04323eb233184213d913d2e349a9b208dba7c/PyOtter.png' width='80%' align='center'>

### Sobre a pyOtter:

* As funções foram projetadas para tornar a manipulação de DataFrames mais intuitiva e prática, semelhante às operações realizadas com DataFrames em bibliotecas populares como pandas e Spark.
* A biblioteca pyOtter é útil para aqueles que precisam converter e manipular dados entre diferentes formatos de DataFrame, especialmente ao integrar operações Spark com operações nativas em Python.

## Exemplos de uso
### Contagem de linhas em um DataFrame
```
df.count_rows()
# Saída: Número de linhas no DataFrame

```

### Renomear colunas
```
df.rename_columns({'old_name': 'new_name'})
# Altera o nome da coluna 'old_name' para 'new_name'
```
### Exibir o esquema de dados
```
schema = df.show_schema()
# Saída: {'column1': <tipo>, 'column2': <tipo>, ...}
```
### Printar o esquema de dados
```
df.print_schema()
# Imprime os nomes das colunas e seus tipos de dados
```
### Mudar o formato dos Dados
```
df.change_schema({'column_name': int})
# Altera o tipo de dados da coluna 'column_name' para inteiro
```
### Filtrar dados
```
filtered_df = df.filter(column_name='value')
# Retorna um novo DataFrame contendo apenas as linhas onde 'column_name' é igual a 'value'
```
### Contar valores distintos
```
distinct_counts = df.count_distinct('column1', 'column2')
# Saída: {'column1': número de valores distintos, 'column2': número de valores distintos}
```
### Exportar para csv
```
df.export_to_csv('output.csv', delimiter=';')
# Exporta o DataFrame para 'output.csv' usando ';' como delimitador
```
### Join (junção) de DataFrames
```
df2 = ... # Outro DataFrame pyOtter
joined_df = df.join(df2, on='common_column', how='inner')
# Realiza uma junção inner baseada na coluna 'common_column'
```

## Funções do pyOtter

<strong> __init__(self, data=None, columns=None): </strong>

* Inicializa um objeto pyOtter com dados e colunas. Se nenhum dado ou coluna for fornecido, inicializa com listas vazias.

<strong>from_spark_dataframe(cls, spark_df):</strong>

* Classe de método que cria um objeto pyOtter a partir de um DataFrame Spark, convertendo os dados do Spark em um formato de dicionário Python.

<strong>count_rows(self):</strong>

* Retorna o número de linhas no DataFrame.

<strong>rename_columns(self, col_rename_map):</strong>

* Renomeia colunas do DataFrame de acordo com um mapeamento fornecido (dicionário onde as chaves são os nomes das colunas antigas e os valores são os novos nomes).

<strong>show_schema(self):</strong>

* Retorna um dicionário que mapeia cada coluna para seu tipo de dado, baseado no tipo do primeiro elemento presente em cada coluna.

<strong>change_schema(self, col_type_map):</strong>

* Altera os tipos de dados de colunas específicas fornecendo um mapeamento de colunas para novos tipos de dados.

<strong>filter(self, **conditions):</strong>

* Filtra os dados do DataFrame de acordo com condições fornecidas como argumentos de palavra-chave. As condições são pares coluna-valor.

<strong>count_distinct(self, *cols):</strong>

* Conta os valores distintos em uma ou mais colunas especificadas.

<strong>export_to_csv(self, filename, delimiter=','):</strong>

* Exporta o DataFrame para um arquivo CSV, permitindo especificar um delimitador customizável.

<strong>print_schema(self):</strong>

* Imprime o esquema dos dados, incluindo os nomes das colunas e seus tipos de dados.

<strong>join(self, other, on, how='inner'):</strong>

* Realiza uma junção (join) com outro DataFrame pyOtter baseado em uma coluna comum. Suporta tipos de junção: inner, left, right e outer.

<strong>__str__(self):</strong>

* Retorna uma representação em string do DataFrame, exibindo as colunas e suas respectivas linhas de dados, tabuladas.
