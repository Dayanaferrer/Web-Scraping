# Projeto de Web Scraping do Mercado Livre

Este é um projeto de web scraping que visa coletar informações sobre produtos em oferta no site do Mercado Livre, calcular estatísticas descritivas e apresentá-las visualmente em um boxplot. O objetivo é identificar produtos com descontos acima de 15% e analisar sua distribuição de preços.

## Como funciona

1. **Scraping dos dados**: O script Python utiliza a biblioteca BeautifulSoup para fazer scraping da página do Mercado Livre que contém o carrossel de ofertas. Ele identifica os produtos em oferta, calcula o desconto percentual e filtra aqueles com desconto superior a 15%.

2. **Organização do DataSet**: Os dados coletados são organizados em um DataFrame do Pandas, com colunas para nome do produto, preço original, preço com desconto, desconto percentual, etc.

3. **Cálculo de estatísticas descritivas**: São calculadas estatísticas descritivas, como média, mediana, desvio padrão, etc., para analisar a distribuição dos descontos.

4. **Geração de gráficos**: Um boxplot é gerado usando a biblioteca Matplotlib para visualizar a distribuição dos descontos.

5. **Exportação dos resultados**: Os dados são exportados para um arquivo CSV, que pode ser facilmente importado para o Excel para análises adicionais.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python: BeautifulSoup, requests, pandas, matplotlib

## Como usar

1. Clone o repositório ou faça o download dos arquivos.

2. Instale as bibliotecas Python necessárias:
   ```
   pip install beautifulsoup4 requests pandas matplotlib
   ```

3. Execute o script `scraping_mercadolivre.py`.

4. Os resultados serão salvos em um arquivo CSV chamado `produtos_oferta_mercadolivre.csv`.

5. Abra o arquivo CSV no Excel para visualizar os dados e o boxplot gerado.

## Notas importantes

- Este projeto é apenas para fins educacionais e de aprendizado.
- Certifique-se de respeitar os termos de serviço do Mercado Livre ao fazer scraping de seus dados.
- O código pode precisar ser ajustado conforme as mudanças na estrutura do site do Mercado Livre.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
