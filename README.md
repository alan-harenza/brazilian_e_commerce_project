# Brazilian E-Commerce - Project - Kaggle.com

## Objeitvo
Este repositorio tem como funcao, desenvolver habilidades relacionadas a um Data Enginner e Analytics Enginner.

Sera usado como base, os  arquivos fornecidos em\
Brazilian E-Commerce Public Dataset by Olist\
do site: www.kaggle.com .
logo, não detenho os direitos autorais das informacoes, havendo duvidas, entrar no site e procurar o dataset mencionado.

## Conjunto de dados usados

Serao usados um conjunto de 9 bases de dados, todos no formato ".csv", para não alocar fiscamente no repositorio e ocupar\
espaço desnecessario, sera criado uma funcao em conjunto com a api fornecida pela kaggle para importar diretamente\
do site.

Bases: 

* olist_customers_dataset;
* olist_geolocation_dataset;
* olist_order_items_dataset;
* olist_order_payments_dataset;
* olist_order_review_dataset;
* olist_orders_dataset;
* olist_products_dataset;
* olist_seller_dataset e
* product_category_name_translation.

## Principais Bibliotecas

* Pyspark
* Pandas

as demais ficaram expostas no arquivo requirements.txt

## Recomendacoes

Para ficar melhor configurado é recomendado criar uma maquina virtual para rodar todos os scripts, desta forma, não ficamos\
instalando tudo na sua maquina, e concentramos tudo nesta vm ficar ficar mais simples e preservarmos nossso sistma.

### Passo a passo par a criacao da sua vm

Como estou rodando no ambiente do linux, irei provisonar os comando em linux, abrir o terminal de comando (cmd)

* sudo apt install python3-pip -y , instalacao do pacote pip, caso não houver feito (opicional),
* sudo apt install python3-venv -y , instalacao do pacote venv, responsavel para criacao da vm.

- criacao da vm no terminal do vs code

* $ python3 -m venv myenv (cria maquina virtual)
* $ source venv/bin/activate (ativa a maquina virtual)
* $ deactivate (desativa maquina virtual)

obs: criar um arquivo .gitignore e colocar o nome da maquina virtual, desta maneira, não sera incluso quando for fazer\
o processo de subida ao repositorio do github
