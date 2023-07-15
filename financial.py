import json
from flask import Flask, render_template
from collections import Counter
from datetime import datetime, timedelta

app = Flask(__name__)

# Carregar dados

@app.route('/consulta/<int:transaction_id>',methods=['GET'])
def consulta_json(transaction_id):
    with open(r'C:\Users\mecoa\Documents\GitHub\cloudwalk_test\dataset.json') as json_file:
        data = json.load(json_file)
        user_id = [transaction['user_id'] for transaction in data]
        user_id_count = Counter(user_id)

        #Procurar a transação pelo id
        for transaction in data:
                if transaction['transaction_id'] == transaction_id:
                    transaction_amount = transaction['transaction_amount']
                    user_id = transaction['user_id']
                    transaction_date_str = transaction['transaction_date']
                    transaction_date = datetime.strptime(transaction_date_str, '%Y-%m-%dT%H:%M:%S.%f')

                    # Verificar se o user_id fez transações recentes
                    if anti_fraude(user_id, transaction_date, data):
                        status = f"Status da Transação: {user_id}. Negada, transação dentro do intervalo de 12 minutos!"
                        return render_template('status.html', status=status)

                    # Condição para transação limite

                    if transaction_amount < 500.0:
                        if user_id_count[user_id] > 2:
                             status = f"Status da Transação: {user_id}. Negada, você excedeu o limite de transações!"
                             return render_template('status.html', status=status)
                        else:
                             status = f"Status da Transação: {user_id}, Transação Aprovada!"
                             return render_template('status.html', status=status)
                    else:   
                        status = f"Status da Transação: {user_id}. Negado, você excedeu o limite de crédito!"
                        return render_template('status.html', status=status)      
                    
        status = "Transação não encontrada."
        return render_template('status.html', status=status)

def anti_fraude(user_id, current_transaction_date, data, minutes=12):
    with open(r'C:\Users\mecoa\Documents\GitHub\cloudwalk_test\dataset.json') as json_file:
        data = json.load(json_file)
    recent_time_limit = current_transaction_date - timedelta(minutes=minutes)
    #current_time = datetime.now()
    recent_transactions = [transaction for transaction in data if transaction['user_id'] == user_id and
                           datetime.strptime(transaction['transaction_date'], '%Y-%m-%dT%H:%M:%S.%f') > recent_time_limit]
    return len(recent_transactions) > 1

# Endpoint para casos de estorno

@app.route('/estorno/<int:transaction_id>',methods=['GET'])
def estorno_json(transaction_id):
    with open(r'C:\Users\mecoa\Documents\GitHub\cloudwalk_test\dataset.json') as json_file:
        data = json.load(json_file)

        for estorno in data:
            if estorno['transaction_id'] == transaction_id:
               has_cbk = estorno['has_cbk'] 

               if has_cbk == 'TRUE':
                  status = f"Estorno: {transaction_id}. Não é possível realizar o estorno."
                  return render_template('status.html', status=status)
               else:
                   status = f"Estorno: {transaction_id}. Possível, entre em contato!"
                   return render_template('status.html', status=status)
               
        return "Transação não encontrada."
        

app.run(port=5000,host='localhost',debug=True)


