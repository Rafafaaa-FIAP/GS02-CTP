
# Importação do módulo dos valores padrões
from Modules.defaultValues import Colors
from datetime import timedelta, date

# Importação da biblioteca requests utilizada para pegar os dados da API
import requests

# Endpoint da API
ENDPOINT = f'https://gs-ano1-sem2-default-rtdb.firebaseio.com/leituras.json?orderBy="dt_leitura"&startAt="{date.today() + timedelta(days=-7)}"'

# Criação da classe Firebase
class Firebase:
  # Função de inicialização da classe
  def __init__(self, texts):
    self.errorText = texts['errorFirebase']

  # Função de pegar os dados da API, formatar da maneira necessária e retornar esses dados formatados
  def getLeituras(self):
    leiturasRet = []
    try:
      response = requests.get(ENDPOINT)
      leituras = response.json()
      for key in leituras.keys():
        obj = leituras[key]
        obj['id'] = key
        leiturasRet.append(obj)
    except:
      print(self.errorText)

    return leiturasRet