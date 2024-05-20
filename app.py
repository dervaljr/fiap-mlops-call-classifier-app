import streamlit as st
import requests
import json

def get_prediction(data):

    endpoint = st.secrets['API-ENDPOINT']
    headers = {'x-api-key': st.secrets['API-KEY'], 'Content-Type': 'application/json'}

    response = requests.post(endpoint, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
       result = (response.json())
       st.markdown('foi aberto um chamado na categoria:')
       st.markdown(result['prediction'])

    else:
        st.markdown("Error")

"""
Trabalho MLOPS

Grupo: 
    Derval Oliveira (349407), Elaine Silva (350458), João Marcos Silva (346688), Sérgio Resnauer (350814)

Bem-vindo ao canal de atendimento da QuantumFinance!!!

Relate abaixo seu problema ou dúvida que iremos classificá-lo da melhor forma 
entre os principais assuntos:\n 
    - Serviços de conta bancária\n
    - Cartão de crédito / Cartão pré-pago\n
    - Hipotecas / Empréstimos\n
    - Roubo / Relatório de disputa\n
    - Outros

Iremos direcionar para a área especialista no assunto que irá entrar em contato o mais breve possível.
    
"""

texto = st.text_area('Digite aqui seu problema/dúvida:')

payload = {
  "data": {
    "text": texto
  }
}

if st.button('enviar'):
    with st.spinner('processando...'):
        get_prediction(payload)