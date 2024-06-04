
from Modules.defaultValues import Colors
from datetime import timedelta, date
import requests

ENDPOINT = f'https://gs-ano1-sem2-default-rtdb.firebaseio.com/leituras.json?orderBy="dt_leitura"&startAt="{date.today() + timedelta(days=-7)}"'

class Firebase:
  def __init__(self, texts):
    self.errorText = texts['errorFirebase']

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