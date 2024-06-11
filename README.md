# pyOtter
Spark to Otter Dataframe Python library

![pyOtte](https://github.com/gustavoriz/pyOtter/blob/b4a04323eb233184213d913d2e349a9b208dba7c/PyOtter.png)

## Funções do pyOtter


## Exemplos de uso

<strong> __init__(self, data=None, columns=None): </strong>

* Inicializa um objeto pyOtter com dados e colunas. Se nenhum dado ou coluna for fornecido, inicializa com listas vazias.
from_spark_dataframe(cls, spark_df):

Classe de método que cria um objeto pyOtter a partir de um DataFrame Spark, convertendo os dados do Spark em um formato de dicionário Python.
count_rows(self):

Retorna o número de linhas no DataFrame.
rename_columns(self, col_rename_map):

Renomeia colunas do DataFrame de acordo com um mapeamento fornecido (dicionário onde as chaves são os nomes das colunas antigas e os valores são os novos nomes).
show_schema(self):

Retorna um dicionário que mapeia cada coluna para seu tipo de dado, baseado no tipo do primeiro elemento presente em cada coluna.
change_schema(self, col_type_map):

Altera os tipos de dados de colunas específicas fornecendo um mapeamento de colunas para novos tipos de dados.
filter(self, **conditions):

Filtra os dados do DataFrame de acordo com condições fornecidas como argumentos de palavra-chave. As condições são pares coluna-valor.
count_distinct(self, *cols):

Conta os valores distintos em uma ou mais colunas especificadas.
export_to_csv(self, filename, delimiter=','):

Exporta o DataFrame para um arquivo CSV, permitindo especificar um delimitador customizável.
print_schema(self):

Imprime o esquema dos dados, incluindo os nomes das colunas e seus tipos de dados.
join(self, other, on, how='inner'):

Realiza uma junção (join) com outro DataFrame pyOtter baseado em uma coluna comum. Suporta tipos de junção: inner, left, right e outer.
__str__(self):

Retorna uma representação em string do DataFrame, exibindo as colunas e suas respectivas linhas de dados, tabuladas.
