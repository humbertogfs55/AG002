## 
Ola, meu nome é humberto e esse é meu trabalho pratico para a avaliação global de 2024.

Neste projeto Criei um modelo de arvore de decisão, treinado com um dataset de 3 especies diferentes de pinguins. dado certas informações de um determinado pinguin o modelo é capaz de prever a especie desse pinguin. 

Primeiramente vou mostrar o modelo, e depois vamos passar pelo codigo linha a linha com uma curta explicação do seu funcionamento.  

Esse codigo foi escrito e organizado com base no documento base para o projeto para facilitar o desenvolvimento. 

### (1) 
Primeiramente criamos dicionarios para mapear as strings do dataset para ints.
passamos o mapeamento para o data frame utilizando a função replace.

### (2)
criação de uma array com a ordem desejada das colunas
utilizamos a função reindex para reordenar o dataset. 

### (3) 
Agora utilizamos pela primeira vez o sklearn.
X é nosso data frame de features e contem todas as colunas exeto a species, essas são as variaveis que o modelo utiliza para tentar prever nosso alvo

y é o dataframe alvo, ele contem apenas a coluna species.

a função train test split recebe x e y, e alguns parametros a mais, 
test size separa o dataset em 20% para datos de teste, direcionando para x test e y test. 
ele infere o valor de treinamento para os 80% restantes. 

o parametro random state funciona como uma seed, garantindo que sempre separemos os mesmos dados entre teste e treino. é util para fim de testes. 

### (4)
instanciando a classe decisiontreeclassifier, criamos o nosso modelo em si
e chamando a função  fit e passando os parametros de treinamento ele é treinado. 

### (5)
a função predict recebendo os dados de teste gera um dataframe Y(ou seja uma coluna de 0-2) contendo as especies esperadas com base nos dados de teste x

### (6)
Com os resultados da previsão anterior podemos avaliar a qualidade do treinamento do modelo com as funçoes accuracy e report. 

acuracy nos da um valor de 0 a 1 representando a rasão geral de precisao do modelo, ou seja se 100% das instancias forem previstas com sucesso temos uma acurracy de 1.0

o classification report nos da alguns dados mais precisos. 

primeiro passando pelo 0 1 2 temos os dados finos de cada especie de pinguin.
 
precision pode ser entendido como quantos itens selecionados são relevantes.
recall pode ser entendido quantos itens relevantes foram selecionados
f1-score é a media harmonica entre precision e recall 
support é a quantidade de ocorrencias da especie dentro do dataset. 

0 adelie
1 chinstrap
2 gentoo

