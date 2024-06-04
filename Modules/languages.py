
from Modules.defaultValues import Colors, Texts

def returnBeginEndWithStyle(text):
  return f'{Colors.LIGHT_CYAN}{Colors.NEGATIVE}{text}{Colors.END}'

def returnTitleWithStyle(text):
  return f'{Colors.TITLE1}{text}{Colors.END}'

def returnInputWithStyle(text):
  return f'{Colors.INPUT}{text}{Colors.END}'

def returnErrorWithStyle(text):
  return f'{Colors.ERROR}{text}{Colors.END}'

class Languages:
  def __init__(self, selected = ''):
    self.all = {
      'pt_br': {
        'id': '1',
        'name': 'Português',
        'title': returnTitleWithStyle('IDIOMA'),
        'begin': returnBeginEndWithStyle('Bem-vindo ao nosso sistema de Monitoramento dos Mares!'),
        'end': returnBeginEndWithStyle('Obrigado por utilizar nosso sistema!'),
        'selectMenu': returnInputWithStyle('Escolha uma opção:'),
        'selectLanguage': returnInputWithStyle('Escolha um idioma:'),
        'errorOption': returnErrorWithStyle('Opção inválida!'),
        'errorFirebase': returnErrorWithStyle('Erro ao buscar dados!'),
        'about': f'Nosso sistema utiliza os dados armazenados por um circuito Arduino para criar gráficos para análise e monitoramento da qualidade dos mares.\nVeja também nosso site: {Texts.LINK_SITE}',
        'menu': {
          'title': returnTitleWithStyle('MENU'),
          'options': ['Sobre', 'Média Diária', 'Média Mensal', 'Mudar Idioma', 'Sair']
        },
        'tempText': 'Temperatura',
        'turbText': 'Turbidez',
      },
      'en': {
        'id': '2',
        'name': 'English',
        'title': returnTitleWithStyle('LANGUAGE'),
        'welcome': returnBeginEndWithStyle('Welcome to our Sea Monitoring system!'),
        'end': returnBeginEndWithStyle('Thank you for using our system!'),
        'selectMenu': returnInputWithStyle('Choose an option:'),
        'selectLanguage': returnInputWithStyle('Choose a language:'),
        'errorOption': returnErrorWithStyle('Invalid option!'),
        'errorFirebase': returnErrorWithStyle('Error fetching data!'),
        'about': f'Our system uses data stored by an Arduino circuit to create graphs for analyzing and monitoring the quality of the seas.\nSee also our website: {Texts.LINK_SITE}',
        'menu': {
          'title': returnTitleWithStyle('MENU'),
          'options': ['About', 'Daily Average', 'Monthly Average', 'Change Language', 'Exit']
        },
        'tempText': 'Temperature',
        'turbText': 'Turbidity',
      },
      'es': {
        'id': '3',
        'name': 'Español',
        'title': returnTitleWithStyle('IDIOMA'),
        'begin': returnBeginEndWithStyle('Bienvenido a nuestro sistema de Monitoreo del Mar!'),
        'end': returnBeginEndWithStyle('Gracias por utilizar nuestro sistema!'),
        'selectMenu': returnInputWithStyle('Elige una opcion:'),
        'selectLanguage': returnInputWithStyle('Elige un idioma:'),
        'errorOption': returnErrorWithStyle('Opción inválida!'),
        'errorFirebase': returnErrorWithStyle('Error al obtener datos!'),
        'about': f'Nuestro sistema utiliza datos almacenados por un circuito Arduino para crear gráficos para analizar y monitorear la calidad de los mares.\nConsulte también nuestro sitio web: {Texts.LINK_SITE}',
        'menu': {
          'title': returnTitleWithStyle('MENÚ'),
          'options': ['Acerca De', 'Promedio Diario', 'Media Mensual', 'Cambiar Idioma', 'Salir']
        },
        'tempText': 'Temperatura',
        'turbText': 'Turbiedad',
      }
    }

    listID = []
    for key in self.all.keys():
      listID.append(self.all[key]['id'])
    self.listID = listID

    if (selected == ''):
      self.selected = self.all['pt_br']
    else:
      self.selected = selected

  def showAllLanguages(self):
    for key in self.all.keys():
      print(f'{self.all[key]['id']} - {self.all[key]['name']}')

    return

  def returnLanguageByID(self, languageID):
    for key in self.all.keys():
      if (self.all[key]['id'] == languageID):
        return self.all[key]
  
