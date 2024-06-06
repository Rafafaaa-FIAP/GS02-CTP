
# Importação do módulo dos valores padrões
from Modules.defaultValues import Colors, Texts

# Criação da classe Menu
class Menu:
  # Função de inicialização da classe
  def __init__(self, texts):
    self.options = {
      'ids': ['1', '2', '3', '4', '0'],
      'names': texts['options']
    }
    self.title = texts['title']

  # Função que exibe todas as opções
  def showOptions(self):
    print(Texts.SEPARATOR1)
    print(self.title)
    print(Texts.SEPARATOR1)
    for i in range(len(self.options['ids'])):
      print(f'{self.options['ids'][i]} - {self.options['names'][i]}')

    return
  
  # Função que exibe uma opção específica
  def showOptionByID(self, menuID):
    for i in range(len(self.options['ids'])):
      if (self.options['ids'][i] == menuID):
        print(Texts.SEPARATOR2)
        print(f'{Colors.TITLE2}{self.options['ids'][i]} - {self.options['names'][i]}{Colors.END}')
        print(Texts.SEPARATOR2)
  
  # Função que retorna uma opção específica
  def returnOptionNameByID(self, menuID):
    for i in range(len(self.options['ids'])):
      if (self.options['ids'][i] == menuID):
        return self.options['names'][i]
  