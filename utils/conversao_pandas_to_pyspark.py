from pandas import DataFrame as dataframe
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

def conversao_pandas_to_pyspark(df: dataframe) -> DataFrame:
    '''
    funcao que recebe um dataframe do pandas e
    o transforma em um dataframe do pyspark

    input
        df: dataframe

    return:
        df_sp: DataFrame
    '''
    spark = SparkSession\
    .builder\
    .master('local[*]')\
    .appName("PandasToSpark")\
    .getOrCreate()

    df_sp = spark.createDataFrame(df)

    return df_sp