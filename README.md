# pyOtter
Spark to Otter Dataframe Python library

# Meu Projeto

## Exemplo de Uso

<div style="border: 1px solid #e1e4e8; padding: 16px; border-radius: 8px; background-color: black; color: #fff">
if __name__ == "__main__":
    from pyspark.sql import SparkSession

    # Inicializando o Spark
    spark = SparkSession.builder.appName("Exemplo").getOrCreate()

    # Criando um DataFrame de exemplo
    data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    columns = ["Nome", "ID"]
    spark_df = spark.createDataFrame(data, columns)

    # Convertendo para MeuDataFrame
    meu_df = MeuDataFrame.from_spark_dataframe(spark_df)
    print("MeuDataFrame:")
    print(meu_df)

    # Filtrando dados
    filtered_df = meu_df.filter(lambda row: row["ID"] > 1)
    print("Filtrado:")
    print(filtered_df)

    # Join com outro DataFrame
    data2 = [(1, "A"), (2, "B"), (4, "D")]
    columns2 = ["ID", "Valor"]
    spark_df2 = spark.createDataFrame(data2, columns2)
    meu_df2 = MeuDataFrame.from_spark_dataframe(spark_df2)

    joined_df = meu_df.join(meu_df2, on="ID", how="inner")
    print("Join:")
    print(joined_df)

</div>

## Box com Fundo Colorido

<div style="border: 1px solid #e1e4e8; padding: 16px; border-radius: 8px; background-color: #f9f9f9;">
  Este é um box com fundo colorido.
</div>

## Box Personalizado

<div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #e7f4e4;">
  <h2 style="color: #4CAF50;">Título do Box</h2>
  <p>Este é um box personalizado.</p>
</div>
