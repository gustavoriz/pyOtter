# pyOtter
Spark to Otter Dataframe Python library

<img src=('https://github.com/gustavoriz/pyOtter/blob/b4a04323eb233184213d913d2e349a9b208dba7c/PyOtter.png') width='50%'>

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
