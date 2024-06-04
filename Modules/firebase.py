
from Modules.defaultValues import Colors
from datetime import timedelta, date
import requests

ENDPOINT = f'https://gs-ano1-sem2-default-rtdb.firebaseio.com/leituras.json?orderBy="dt_leitura"&startAt="{date.today() + timedelta(days=-7)}"'

leiturasTeste = {
"-Nz5fBZ-NePjWpTBCCRo": {
"dt_leitura": "2024-05-29T23:26:04.938Z",
"temperatura": -35.4,
"turbidez": 60
},
"-Nz5fFl48i_nAzaDcjt8": {
"dt_leitura": "2024-05-29T23:26:22.158Z",
"temperatura": -35.4,
"turbidez": 60
},
"-Nz5f3COePEUi-RIXgtc": {
"dt_leitura": "2024-05-29T23:25:30.722Z",
"temperatura": 47.4,
"turbidez": 60
},
"-Nz5f7F-Tko30T5aOoUW": {
"dt_leitura": "2024-05-29T23:25:47.274Z",
"temperatura": 47.4,
"turbidez": 60
},
"-Nz5fSpxunrtSorirg6O": {
"dt_leitura": "2024-05-29T23:27:15.718Z",
"temperatura": -12,
"turbidez": 60
},
"-Nz5faUsfx52d4wTMCOG": {
"dt_leitura": "2024-05-29T23:27:51.170Z",
"temperatura": -12,
"turbidez": 60
},
"-Nz5WgbxMCZxN_ygoRY4": {
"dt_leitura": "2024-05-29T22:44:34.811Z",
"temperatura": "32.60",
"turbidez": "25"
},
"-NzFA7XzM2vdBvaOLOy2": {
"dt_leitura": "2024-05-31T19:43:11.910Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5f-ArhS_in0oe1hYy": {
"dt_leitura": "2024-05-29T23:25:14.241Z",
"temperatura": 47.4,
"turbidez": 91
},
"-Nz5ee6BAplCsVd_ie11": {
"dt_leitura": "2024-05-29T23:23:43.830Z",
"temperatura": 32.6,
"turbidez": 25
},
"-NzF9wf-m2DKL2-JxObr": {
"dt_leitura": "2024-05-31T19:42:23.271Z",
"temperatura": 32.6,
"turbidez": 25
},
"-NzF97xgqPCSwrVPNKs2": {
"dt_leitura": "2024-05-31T19:38:51.474Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5fOetCTkh4JAETkUb": {
"dt_leitura": "2024-05-29T23:26:58.627Z",
"temperatura": -12,
"turbidez": 60
},
"-NzF8rHM9TgKn9NoJMM3": {
"dt_leitura": "2024-05-31T19:37:39.068Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5fjMDGiJYYz5ZCC6G": {
"dt_leitura": "2024-05-29T23:28:27.480Z",
"temperatura": 12.4,
"turbidez": 60
},
"-Nz5fepUrZsWkopQq0Ms": {
"dt_leitura": "2024-05-29T23:28:08.936Z",
"temperatura": -12,
"turbidez": 60
},
"-NzF9oy6lcOtOTaJ6mGW": {
"dt_leitura": "2024-05-31T19:41:51.726Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5g0J8WIi4B7XwuYlx": {
"dt_leitura": "2024-05-29T23:29:41.011Z",
"temperatura": 12.4,
"turbidez": 91
},
"-Nz5fo0t30TN8vWzwm1z": {
"dt_leitura": "2024-05-29T23:28:46.594Z",
"temperatura": 12.4,
"turbidez": 91
},
"-NzFA3_1ZEIeKfUo9xKS": {
"dt_leitura": "2024-05-31T19:42:55.657Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5eihO9m4h4llHPb3Y": {
"dt_leitura": "2024-05-29T23:24:02.659Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5ew4cdvhqPpTW3k0q": {
"dt_leitura": "2024-05-29T23:24:57.458Z",
"temperatura": 47.4,
"turbidez": 0
},
"-NzF9l1HOh1kZ3v6rTfp": {
"dt_leitura": "2024-05-31T19:41:35.608Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5erh8UwyAZCCcktdd": {
"dt_leitura": "2024-05-29T23:24:39.506Z",
"temperatura": 47.4,
"turbidez": 0
},
"-Nz5enCMGd5_u7YawIr2": {
"dt_leitura": "2024-05-29T23:24:21.089Z",
"temperatura": 47.4,
"turbidez": 25
},
"-Nz5fXP8R6gGN5_DBejS": {
"dt_leitura": "2024-05-29T23:27:34.419Z",
"temperatura": -12,
"turbidez": 60
},
"-NzFABVPCrskW3U5tX3x": {
"dt_leitura": "2024-05-31T19:43:28.129Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5fK0iGtu0cndhf-zt": {
"dt_leitura": "2024-05-29T23:26:39.607Z",
"temperatura": -12,
"turbidez": 60
},
"-NzF9sm7uEMphRsPFMMm": {
"dt_leitura": "2024-05-31T19:42:07.343Z",
"temperatura": 32.6,
"turbidez": 25
},
"-NzFA-bCXbmgJDYoCpUN": {
"dt_leitura": "2024-05-31T19:42:39.412Z",
"temperatura": 32.6,
"turbidez": 25
},
"-Nz5fwxOhf0RGiSy9uF1": {
"dt_leitura": "2024-05-29T23:29:23.171Z",
"temperatura": 12.4,
"turbidez": 91
},
"-Nz5g4vweOtP90k4YzrL": {
"dt_leitura": "2024-05-29T23:29:59.942Z",
"temperatura": 12.4,
"turbidez": 91
},
"-Nz5fs_BmchHERydAh6-": {
"dt_leitura": "2024-05-29T23:29:05.238Z",
"temperatura": 12.4,
"turbidez": 91
},
}

class Firebase:
  def __init__(self, texts):
    self.errorText = texts['errorFirebase']

  def getLeituras(self):
    leiturasRet = []
    try:
      # response = requests.get(ENDPOINT)
      leituras = leiturasTeste # response.json()
      for key in leituras.keys():
        obj = leituras[key]
        obj['id'] = key
        leiturasRet.append(obj)
    except:
      print(self.errorText)

    return leiturasRet