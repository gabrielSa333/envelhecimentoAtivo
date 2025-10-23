# Como rodar o projeto

## Clonar o projeto
Comece clonando o projeto onde desejar.

## Arquivos necessários
1. [Acesse o site do IBGE](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html?=&t=downloads)
2. Você precisa instalar dois arquivos, o `PNS_2019_20220525.zip` e o `Dicionario_e_input_20220530.zip`. Estes arquivos estão na pasta `2019`, dentro de `Microdados`, em `Dados` e `Documentacao`.
3. Depois de instalados, extraia ambos. Dentro das pastas extraídas, localize os arquivos `dicionario_PNS_microdados_2019.xls` dentro do ZIP de dicionário e o arquivo `PNS_2019.txt`.
4. Após localiza-los, o mais fácil é mover estes arquivos para dentro da pasta `src` do projeto.
    - Você pode alterar o código para apontar para o path dos seus arquivos, mas terá muito mais trabalho.

## Rodar o projeto
O ideal é fazer isso com uma venv. As dependências estão dentro do requirements.txt.
- Depois de criar uma venv e instalar as dependências, basta rodar o script etl.py `python etl.py`. Esse script faz o parse do dicionário para CSV e divide os dados em dataframes particionados. Depois de fazer isso, basta seguir o `examplos.ipynb` que mostra como lidar com os dados.
