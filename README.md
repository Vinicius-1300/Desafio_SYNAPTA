# Desafio_SYNAPTA
Repositório destinado a resolução do desafio SYNAPTA  |  Laboratório de Dados e Inteligência Artificial
Dataset: Sao Paulo Housing Prices

A documentação a seguir, visa explicar a analise do preços de aluguéis do município de São Paulo, retirado da plataforma Kaglle, sendo feito um código em linguagem Python, utilizando as bibliotecas (módulos) pandas (responsável pela análise dos dados) e plotly (responsável por gerar os gráfico) para obtenção desse objetivo. Para a construção e execução do código foi utilizado a IDE Visual Studio Code.

O dataset possui ao todo 11657 linhas (rows) e 8 colunas (columns), ou seja um grande número de dados coletados. As colunas são as seguintes: 
 - address (Endereço): consiste nos dados de localidade, que seriam os logradouros.
 - district (Bairro): onde exatamente estão esses logradouros, ou ruas de uma explicação mais simples
 - área (Área): em metros quadrados, que consiste no tamanho do imóvel
 - bedrooms (Quartos): quantidade de quartos que o imóvel possui
 - garage (Garagem): se possui garagem, e quantas são
 - type (Tipo): define se é apartamento, kit-net, casa ou casa em condomínio

Para facilitar o entendimento e análise, as colunas foram traduzidas já que código foi escrito para ter mensagens de saída em português - BR.

No inicio do código, foi utilizado a função describe() que é oriunda da biblioteca pandas. Sua função, é gerar um 'resumo' estatístico do dataframe pois traz informação especificas 
em relação ao dados como exemplo: a média de cada uma das colunas, o valor mínimo e máximo também da cada uma das colunas.

Inteligência artificial generativa foi utilizado n código, mas para tirar dúvidas ao aparecerem erros no terminl do VS Code, para correção de sintaxe, busca de soluação para problemas que não tiveram soluções com mente humana, para pedir ajuda para verificar se a lógica do código em alguns trechos estavam corretas e também para verificação se a sintaxe estava correta.

ANÁLISE(S) DO DATASET 
Valor médio e mediano:

De inicio, foi tirada o preço médio do aluguel que teve como resultado  R$3250,81 de valor. O resultado foi gerado com base apenas na coluna 'Aluguel'. Como também, foi tirada o valor mediano que seu valor foi R$ 2415,00. O valor médio e valor mediano, tem grandes diferenças pois a média soma todos os valores e divide pelo total e já mediana apenas consiste em pegar o valor que aparece no meio de todos os valores.

Localidades com maior e menor aluguel:
 
A principio, o resultado não pode aparecer por completo por conta da vasta quantidades de dados tanto em relação as localidades, quanto pelos valores do aluguel. O reultado, foi o total de 5348 itens que foram analisados do dataset. Uma observação, não é possível gerar duas tabelas separadas onde uma tem os valores com os locais com maior aluguel e outra com menor aluguel por conta dos dados da coluna Endereço não se repetirem e para contornar esse problema foi colocado em ordem decrescente em uma única tabela.

Comparação do aluguel com características do imóvel:

Foi usado duas características, para verificar a influência que tem sobre o  valor do aluguel. As características escolhidas foi a área e o endereço, ambas colunas do dataframe ,por conta da grande número de dados que contém foi usado uma amostra para não forçar o processamento e para facilitar a análise visualmente. Ambas, foi gerado um gráfico para mostrar os resultados e para facilitar o entendimento de eventuais pessoas que irão olhar e testar. Os gráficos foram gerados através da biblioteca plotly. 

CONLUSÕES:

Para começar, será dito o quais conclusões foi feita analisando o preço médio dos alugueis que é a seguinte: o preço dos alugueis no município de São Paulo e bastante alto, principalmente para pessoas que vindas de estados com padrão de preços bem mais baixo. Isso se deve, ser a capital do estado de São Paulo, por também ser um metrópole, ser uma das maiores cidades do Brasil e América Latina, como também ser altamente industrializada. Esses fatores, faz com que os preços dos aluguéis encareçam, além disso o bairro e rua a qual está o imóvel influência já que existe localidades que são considerados de classe baixa, já outras de classe alta. A quantidade de CEPs que o município possui é vasta, aproximadamente São Paulo tem 1.522,68 km² de extensão e o próprio dataset mostrou isso por ter ao total 11657 linhas de dados na coluna Endereço. 

Outra conclusão encontrada, está na análise do gráfico referente a comparação do valor do aluguel com o área, que está em metros quadrados, mostrou-se que é um dos fatores que influência no preço final do aluguel, como exemplo no gráfico há dois dados que serão uados para comparação que um imóvel que possui um área de 45 metros quadrados tem seu valor de aluguel R$ 500,00. Enquanto um imóvel que tem 54 metros quadrados sobe para R$1100,00 de aluguel, ou seja, mesmo que a diferença seja de apenas 9 metros, foi mais do dobro de diferença de preço. O gráfico consiste nos eixos x e y, que são respctivamente aos valores do aluguel e área, sendo definidos em um gráfico de dispersão simples.

Como dito anteriormente, a área do imóvel influência bastante no valor do aluguel mas não é único fator que compõem. Outro fator que foi usado para análise foi o endereço, também mencionado anteriormente, também foi construído um gráfico que mostra a relação do endereço com o  valor do aluguel. O resultado visto, foi de que um visualização de um amostra, por conta do alto número de dados, onde constata que determinadas ruas possuem preços de alugueis maiores do que outras. Para exemplificar de forma hipotética, duas ruas podem possuir um imóvel come mesma área, quantidades de quartos, mesmo tipo e quantidades de garagem, mas por estarem localizados em endereços diferentes vai ter diferença no valor final, mesmo tendo as mesmas características. E como dito anteriormente, existe locais em São Paulo que são de determinadas classes sociais e isso define qual vai ser o valor do aluguel. No gráfico, o eixo y está os endereços que constam no dataset, já o eixo  x estão os valores do aluguel naquela localidade correspondida.

O terceiro e último gráfico, mostra a relação, tendo como titulo Bairro x Tipo, entre o tipo de imóvel e a quantidade que há em determinado bairro. Nessa relação, mostrou-se que o tipo de imóvel que tem maior quantidade é apartamento, seguido respectivamente casa, studio e kitnet e  por último casa em condomínio. Para esse gráfico em especifico, foi apenas utilizado o as ordenadas (eixo y) pois foi uma solução encontrada para apenas mostrar os bairros e quais os tipo tem maior ou menor quantidade, mas existe uma orientação de quais tipo de imóveis aparecem no gráfico.    

ORIENTAÇÃOES SOBRE O CÓDIGO:

Essa parte se destina para algumas informações que são necessárias para que o código seja executado com êxito e que seu objetivo seja alcançado

Primeiramente, como dito antes, foi usada os módulos pandas e plotly qeu ambos são da linguagem python. Porém, não são nativas da linguagem então precisam ser instaladas na naquina que executará o código.
Acesse o terminal, e digite o seguinte comando: py -m pip install (nome do módulo) e faça isso tanto para a biblioteca pandas quanto para plotly. No caso do plotly, ao importar digite plotly.express. 
Segue o link da documentação das bibliotecas:

Docs do pandas: https://pandas.pydata.org/
Docs do plotly: https://plotly.com/python/plotly-express/

Ambas os múdulos se encontram no arquivo requiremnets.txt e com versão utilizada de cada módulo.

O dataset não estará disponivel no repositório, então precisará ser baixado pela plataforma Kaglle. Abaixo estão os passos para obtenção do dataset quanto para poder ser acessado pelo código:

Passo 1: acesse a plataforma Kaglle e se cadastre caso não tenha conta
Passo 2: pesquise o nome do dataset que é Sao Paulo Housing Prices
Passo 3: busque o icone de baixar e clique para fazer dawload
Passo 4: após baixar, leve o arquivo para mesma pasta onde está o código por conta que o módulo pandas só funciona se orquivo estiver na mesmas localização que o aqruivo executável
Passo 5: para os qruivo ser lido, precisa-se utilizar a função pandas.readcsv(). Lembrando, que o nome do arquivo tem que estar entre espas, ou seja, como uma string e o arquivo está no formato csv.

Se for utilizar o caminho completo do windows para acessar o arquivo, utilize a seguinte sintaxe pandas.readcsv(r"nome do arquivo.csv"). 

E por último, para acessar os dependências usdas utilize o seguinte comando no terminal da IDE: py -m pip install -r requirements.txt