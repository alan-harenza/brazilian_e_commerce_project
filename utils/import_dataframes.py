from pandas import DataFrame
import kagglehub
from kagglehub import KaggleDatasetAdapter

def import_dataframes(file_path: str) -> DataFrame:
    '''
    Funcao para carregar um dataset do site do kaggle.com

    file_path: str
        nome do arquivo que esta querendo buscar + extensao
        opcoes:
            "olist_customers_dataset.csv";
            "olist_geolocation_dataset.csv";
            "olist_order_items_dataset.csv";
            "olist_order_payments_dataset.csv";
            "olist_order_reviews_dataset.csv";
            "olist_orders_dataset.csv";
            "olist_products_dataset.csv";
            "olist_sellers_dataset.csv";
            "product_category_name_translation.csv"
    
    return: pandas.DataFrame
        importacao do Dataframe que conta no site kaggle.com
        para mais informacoes https://www.kaggle.com/docs/api
    '''
    
    df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "olistbr/brazilian-ecommerce",
    file_path,
    # Para mais informacoes de documentacoes:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
    )

    return df