# pyOtter
<center><img src='https://github.com/gustavoriz/pyOtter/blob/25523db025ce7e7f8d82505d67c30c9eeaa5a32a/pyOtter.png' width='80%' align='center'></center>

### Sobre a pyOtter:

* As funções foram projetadas para tornar a manipulação de DataFrames mais intuitiva e prática, semelhante às operações realizadas com DataFrames em bibliotecas populares como pandas e Spark.
* A biblioteca pyOtter é útil para aqueles que precisam converter e manipular dados entre diferentes formatos de DataFrame, especialmente ao integrar operações Spark com operações nativas em Python.
* O pyOtter não é adequado para processamento de grandes volumes de dados que excedem a memória RAM disponível. Para isso, é recomendada a sua utilização em conjunto com outros mecanismos, como o uso de clusters do Spark para filtrar e reduzir Big Datas, para então utilizar as funções do pyOtter. O uso conjunto com o pyOtter pode tornar um código Spark mais performático.

## Exemplos de uso
### Convertendo um Dataframe Spark para um Dataframe pyOtter
```
df = pyOtter.from_spark_dataframe(spark_df)
print(df)
```
### Convertendo um grande Dataframe Spark para um Dataframe pyOtter
```
df = pyOtter.from_big_spark_dataframe(spark_df)
print(df)
```
### Convertendo um Dataframe pyOtter para um Dataframe Spark
```
spark_df = df.to_spark_dataframe(spark)
spark_df.show()
```
### Convertendo um Dataframe Pandas para um Dataframe pyOtter
```
df = pyOtter.from_pandas_dataframe(pandas_df)
print(df)
```
### Convertendo um Dataframe pyOtter para um Dataframe Pandas
```
pandas_df_back = df.to_pandas_dataframe()
print(pandas_df_back)
```

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

<strong>from_big_spark_dataframe(cls, spark_df):</strong>

* Esta classe utiliza o método mapPartitions com redução final, minimizando a transferência de dados entre o driver e os executores, o que é importante para grandes conjuntos de dados. Essa função irá processar cada partição do DataFrame do Spark em paralelo nos executores, convertendo cada linha em um dicionário. Em seguida, ele irá reduzir todas as partições em uma única lista de dicionários. Isso minimiza a quantidade de dados transferidos entre o driver e os executores, o que é crucial para otimizar o desempenho em grandes conjuntos de dados.

<strong>from_pandas_dataframe(cls, spark_df):</strong>

* Classe de método que cria um objeto pyOtter a partir de um DataFrame Pandas, convertendo os dados do Pandas em um formato de dicionário Python.

<strong>to_pandas_dataframe(self)</strong>

* Este método de instância converte o DataFrame pyOtter em um DataFrame pandas.

<strong>to_spark_dataframe(self)</strong>

* Este método de instância converte o DataFrame pyOtter em um DataFrame spark.

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

## License

![MIT License](https://img.shields.io/badge/license-MIT-green) This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
