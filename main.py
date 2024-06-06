
# Importações dos módulos
from datetime import datetime
from Modules.defaultValues import Colors
from Modules.languages import Languages
from Modules.menu import Menu
from Modules.firebase import Firebase

# Importação da biblioteca que gera os gráficos
import matplotlib.pyplot as plt
import numpy as np

# Setup dos módulos
lang = Languages()
menu = Menu(lang.selected['menu'])
firebase = Firebase(lang.selected)
readings = []

# Função de inicializar os sistema (selecionar opção do Menu)
def initializeSystem():
  print(lang.selected['begin'])
  global readings
  while (True):
    menuID = selectOption(lang.selected['selectMenu'], menu.options['ids'], menu.showOptions)
    menu.showOptionByID(menuID)
    menuOptionName = menu.returnOptionNameByID(menuID)
    if (menuID == '0'):
      break
    elif (menuID == '1'):
      print(lang.selected['about'])
    elif (menuID == '2'):
      if (len(readings) == 0):
        readings = firebase.getLeituras()
      dailyAverage(menuOptionName)
    elif (menuID == '3'):
      if (len(readings) == 0):
        readings = firebase.getLeituras()
      monthlyAverage(menuOptionName)
    elif (menuID == '4'):
      changeLanguage()
  print(lang.selected['end'])

# Função para obrigar o usuário a escolher uma opção dentre as existentes
def selectOption(text, possibleOptions, funcShowOptions):
  funcShowOptions()
  text += ' '
  value = input(text)
  while (value not in possibleOptions):
    funcShowOptions()
    print(lang.selected['errorOption'])
    value = input(text)
  return value

# Função que gera os gráficos de médias diárias
def dailyAverage(figureTitle):
  global readings
  listData = {}
  for obj in readings:
    dt_leitura = datetime.strptime(obj['dt_leitura'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%d/%m/%Y")
    if (dt_leitura not in listData.keys()):
      listData[dt_leitura] = {'temp': [], 'turb': []}
    listData[dt_leitura]['temp'].append(float(obj['temperatura']))
    listData[dt_leitura]['turb'].append(float(obj['turbidez']))
  
  graphicsData = {
    'date': [],
    'temp': [],
    'turb': []
  }

  for key in listData.keys():
    medTemp = 0
    for temp in listData[key]['temp']:
      medTemp += temp
    medTemp /= len(listData[key]['temp'])
    medTurb = 0
    for turb in listData[key]['turb']:
      medTurb += turb
    medTurb /= len(listData[key]['turb'])
    graphicsData['date'].append(key)
    graphicsData['temp'].append(round(medTemp, 2))
    graphicsData['turb'].append(round(medTurb, 2))

  fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=True)

  dates = graphicsData['date']
  data_means = {
      lang.selected['tempText']: {
        'color': Colors.TEMPERATURE,
        'data': graphicsData['temp']
      },
      lang.selected['turbText']: {
        'color': Colors.TURBIDITY,
        'data': graphicsData['turb']
      },
  }

  x = np.arange(len(dates))
  width = 0.25
  multiplier = 0

  for attribute, measurement in data_means.items():
    offset = width * multiplier
    rects = axs[0].bar(x + offset, measurement['data'], width, label=attribute, color=measurement['color'])
    axs[0].bar_label(rects, padding=3)
    multiplier += 1

  axs[0].set_xticks(x + width, dates)
  axs[0].legend(loc='upper center', ncols=2)
  axs[0].set_ylim(0, 100)

  axs[1].plot(graphicsData['date'], graphicsData['temp'], 'o-', color=Colors.TEMPERATURE)
  axs[1].plot(graphicsData['date'], graphicsData['turb'], 'o-', color=Colors.TURBIDITY)
  for i in range(len(graphicsData['date'])):
    axs[1].annotate(text=graphicsData['temp'][i], xy=(i, graphicsData['temp'][i]))
    axs[1].annotate(text=graphicsData['turb'][i], xy=(i, graphicsData['turb'][i]))

  axs[1].legend(data_means.keys(), loc='upper center', ncols=2)
  axs[1].set_ylim(0, 100)

  fig.suptitle(figureTitle, fontsize=16)

  plt.show()

# Função que gera os gráficos de médias mensais
def monthlyAverage(figureTitle):
  global readings
  objData = {
    'temp': [],
    'turb': []
  }
  for obj in readings:
    objData['temp'].append(float(obj['temperatura']))
    objData['turb'].append(float(obj['turbidez']))

  medTemp = 0
  for temp in objData['temp']:
    medTemp += temp
  medTemp /= len(objData['temp'])
  medTemp = round(medTemp, 2)
  medTurb = 0
  for turb in objData['turb']:
    medTurb += turb
  medTurb /= len(objData['turb'])
  medTurb = round(medTurb, 2)

  fig, ax = plt.subplots(figsize=(2, 3), subplot_kw=dict(aspect="equal"))

  data = [medTemp, medTurb]

  wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, colors=(Colors.TEMPERATURE, Colors.TURBIDITY))

  bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
  kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

  for i, p in enumerate(wedges):
      ang = (p.theta2 - p.theta1)/2. + p.theta1
      y = np.sin(np.deg2rad(ang))
      x = np.cos(np.deg2rad(ang))
      horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
      connectionstyle = f"angle,angleA=0,angleB={ang}"
      kw["arrowprops"].update({"connectionstyle": connectionstyle})
      ax.annotate(data[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                  horizontalalignment=horizontalalignment, **kw)

  ax.set_title(figureTitle, fontsize=16)

  plt.show()

# Função que altera o idioma do sistema
def changeLanguage():
  global lang
  newLanguage = lang.returnLanguageByID(selectOption(lang.selected['selectLanguage'], lang.listID, lang.showAllLanguages))
  lang = Languages(newLanguage)
  global menu
  menu = Menu(lang.selected['menu'])
  global firebase
  firebase = Firebase(lang.selected)
  return

# Chamando a função de inicializar o sistema
initializeSystem()