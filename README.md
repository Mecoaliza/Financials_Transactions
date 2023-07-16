# RISK TEST

# 1. Introdução

Este projeto Flask [financial.py](https://github.com/Mecoaliza/Financials_Transactions/blob/main/financial.py) apresenta endpoints para consulta de informações de transações e estornos. 
Os dados são obtidos tanto de um banco de dados quanto de um arquivo JSON que contém os registros de transações. 
Além disso, foi implementado um mecanismo de detecção de fraudes com regras específicas para aprovação ou negação das transações.

Durante o desenvolvimento, foram aplicados métodos simples para identificar possíveis padrões de compras fraudulentas e estabelecer regras fictícias para as transações. 
Utilizando o Flask, foram criados endpoints da API, e o Python foi utilizado para aplicar as regras de negócio. Houve integração com o banco de dados, 
e uma página HTML básica foi criada para exibir o status das transações.

É válido ressaltar que, embora esse projeto tenha utilizado métodos mais simples, existem abordagens mais avançadas, como o uso de técnicas de Machine Learning, que podem ser aplicadas para uma detecção de fraudes mais sofisticada.


# 2. Endpoints:

[financial.py](https://github.com/Mecoaliza/Financials_Transactions/blob/main/financial.py)

- ###  "/consulta/<int:transaction_id>":
- Este endpoint recebe um ID de transação como parâmetro na URL. 
Ele consulta as informações da transação a partir do banco de dados e do arquivo JSON. Em seguida, são aplicadas regras de anti fraude e verificadas as seguintes condições:

- Se o usuário realizou transações recentes dentro de um intervalo de 12 minutos, a transação é negada.
Se o valor da transação for menor que 500.0 e o usuário tiver realizado mais de duas transações, a transação é negada.
Caso contrário, a transação é aprovada.

     ![image](https://github.com/Mecoaliza/Financials_Transactions/assets/113151407/5754deb6-0fd9-4bb3-a469-ddef4c6f4cef)



- ### "/estorno/<int:transaction_id>":
- Este endpoint recebe um ID de transação como parâmetro na URL. Ele consulta as informações da transação a partir do banco de dados SQLServer
- Se a transação existir e tiver um campo has_cbk com valor "TRUE", não há a possibilidade de estorno. Caso contrário, o estorno é considerado possível e o usuário é solicitado a entrar em contato.

  ![image](https://github.com/Mecoaliza/Financials_Transactions/assets/113151407/3fab38ec-01c3-4cfb-af15-58800bcb3af9)  


# 3. Anti Fraude:

- O mecanismo de anti fraude verifica se o usuário da transação realizou transações recentes dentro de um intervalo de 12 minutos. 
Isso é feito consultando o arquivo JSON que contém as transações. Se for encontrada mais de uma transação dentro do intervalo, 
a função de anti fraude retorna True, indicando que a transação atual deve ser negada. Caso contrário, retorna False.

- ### Regras de Aprovação ou Negação:

- Transação Negada (anti fraude): Se o usuário tiver realizado transações recentes dentro de um intervalo de 12 minutos.
- Transação Negada (limite de transações): Se o valor da transação for menor que 500.0 e o usuário tiver realizado mais de duas transações.
- Transação Negada (limite de crédito): Se o valor da transação for igual ou superior a 500.0.
- Transação Aprovada: Caso contrário, a transação é aprovada.

Essas regras são aplicadas no endpoint de consulta *"/consulta/<int:transaction_id>"* para determinar o status da transação.

- ### Outros padrões para se analisar:
- **Localização geográfica**: Verificar se as transações estão sendo feitas de diferentes localidades ou se há concentração em uma única região geográfica. Isso pode indicar atividades fraudulentas.
- **Dispositivo utilizado**: Analisar o dispositivo (por exemplo, computador, smartphone) e o tipo de conexão (rede móvel, Wi-Fi) utilizados nas transações.
   Comportamentos incomuns, como muitos dispositivos diferentes sendo usados por um mesmo usuário, podem indicar atividades fraudulentas.
- **Padrões de compra**: Observar o histórico de compras do usuário, incluindo itens, valores, categorias de produtos e horários.
  Identificar comportamentos incomuns, como compras excessivamente grandes ou incomuns para o padrão do cliente, pode indicar atividades fraudulentas.


  # 4. Execução do programa:

  ![image](https://github.com/Mecoaliza/Financials_Transactions/assets/113151407/a7f54f06-64d7-4b0a-a910-8eda9eb4129d)

  ![image](https://github.com/Mecoaliza/Financials_Transactions/assets/113151407/43c58880-5d70-484b-9d4b-18f7f9dd841a)






