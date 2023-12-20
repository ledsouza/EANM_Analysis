# Análise dos hemisférios direito e esquerdo do simulador Hoffman 3D

Cálculo da razão entre o hemisfério direito e esquerdo das estruturas do cérebro simulada pelo Hoffman 3D

| :books: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Análise dos hemisférios direito e esquerdo do simulador Hoffman 3D**
| :label: Tecnologias | python, pandas, glob, os

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://vitrinedev.s3.amazonaws.com/Hoffman_analysis.png#vitrinedev)

## Detalhes do projeto

Análise quantitativa desenvolvida para um projeto de harmonização de estudos neurológicos para PET/CT.

A Associação Européia de Medicina Nuclear (EANM) estabeleceu o EANM Forschungs GmbH (EARL) em 2010 para padronizar a quantificação em imagens de medicina nuclear. O programa de acreditação do EARL oferece controle de qualidade independente para scanners de PET/CT, harmonizando a reconstrução e interpretação de estudos. Isso reduz a variabilidade nos resultados de Valor de Captação Padronizado (SUV) e assegura a calibração precisa dos equipamentos. Dentre os critérios de quantificação, está a razão entre o hemisfério direito e esquerdo dos volumes de interesse da substância cinzenta.

Esse código em Python lida com arquivos CSV em um diretório específico e cria um dicionário onde as chaves são os nomes dos arquivos (sem extensão) e os valores são os caminhos completos dos respectivos arquivos. Em seguida, é passado para a variável _key_name_ o nome do protocolo em questão que será feito o processamento dos dados. 

O processamento dos dados é realizado utilizando a biblioteca pandas:

1. Separa as colunas 'Side' e 'Region' da coluna 'Data ID' em um DataFrame chamado df.
2. Remove a coluna 'Data ID'.
3. Filtra as linhas onde a coluna 'Side' não é igual a 'Brainstem', 'Corpus', 'Regional WM recovery coefficients using full mask' e 'Third'.
4. Divide o DataFrame df em dois sub-DataFrames, df_1 e df_2.
5. Agrupa e soma os valores em df_1 e df_2 com base nas colunas 'Region' e 'Side'.
6. Pivot transforma os dados agrupados em um formato de tabela pivô.
7. Calcula a razão ('Ratio') entre as colunas 'Left' e 'Right' para cada DataFrame pivô (pivoted_1 e pivoted_2).
8. Concatena os dois DataFrames pivôs em um novo DataFrame chamado concatenated_df.
