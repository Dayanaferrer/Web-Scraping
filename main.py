import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Função para calcular o desconto
def calcular_desconto(preco_atual, preco_anterior):
    return ((preco_anterior - preco_atual) / preco_anterior) * 100 if preco_anterior else 0

url = "https://www.mercadolivre.com.br/ofertas"

site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')

# Verificando se a requisição foi bem-sucedida
if site.status_code == 200:
    # Inicializando listas para armazenar os dados
    precos_atuais = []
    precos_anteriores = []
    descontos = []
    parcelamentos = []
    vendedores = []

    # Encontrando todos os elementos que contêm informações dos produtos
    produtos = soup.find_all('div', class_='promotion-item__description')

    # Iterando sobre cada produto
    for produto in produtos:
        # Extraindo o preço atual
        preco_atual_element = produto.find('span', class_='andes-money-amount__fraction')
        preco_atual = float(preco_atual_element.text) if preco_atual_element else 0

        # Extraindo o preço anterior
        preco_anterior_element = produto.find('s', class_='andes-money-amount__fraction')
        preco_anterior = float(preco_anterior_element.text) if preco_anterior_element else 0

        # Calculando o desconto
        desconto = calcular_desconto(preco_atual, preco_anterior)

        # Verificando se o desconto é superior a 15%
        if desconto > 15:
            # Extraindo outras informações relevantes
            porcentagem_desconto = produto.find('span', class_='promotion-item__discount-text').text
            parcelamento = produto.find('span', class_='promotion-item__installments').text
            vendedor = produto.find('span', class_='promotion-item__seller').text

            # Armazenando os dados nas listas
            precos_atuais.append(preco_atual)
            precos_anteriores.append(preco_anterior)
            descontos.append(desconto)
            parcelamentos.append(parcelamento)
            vendedores.append(vendedor)

    # Criando um DataFrame com os dados
    data = {
        'Preço atual': precos_atuais,
        'Preço anterior': precos_anteriores,
        'Desconto (%)': descontos,
        'Parcelamento': parcelamentos,
        'Vendedor': vendedores
    }
    df = pd.DataFrame(data)

    # Organizando o DataFrame em ordem alfabética
    df.sort_values(by='Vendedor', inplace=True)

    # Gerando um CSV com os dados
    df.to_csv('ofertas_mercado_livre.csv', index=False)

    # Exportando para o Excel
    df.to_excel('ofertas_mercado_livre.xlsx', index=False)

    # Calculando estatísticas descritivas
    estatisticas_descritivas = df.describe()

    # Criando um boxplot
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['Desconto (%)'], vert=False)
    plt.title('Distribuição de descontos')
    plt.xlabel('Desconto (%)')
    plt.show()

    # Imprimindo as estatísticas descritivas
    print("Estatísticas Descritivas:")
    print(estatisticas_descritivas)

else:
    print("Erro ao acessar a página:", site.status_code)
