
from Modules.defaultValues import Colors, Texts

class Menu:
  def __init__(self, texts):
    self.options = {
      'ids': ['1', '2', '3', '4', '0'],
      'names': texts['options']
    }
    self.title = texts['title']

  def showOptions(self):
    print(Texts.SEPARATOR1)
    print(self.title)
    print(Texts.SEPARATOR1)
    for i in range(len(self.options['ids'])):
      print(f'{self.options['ids'][i]} - {self.options['names'][i]}')

    return
  
  def showOptionByID(self, menuID):
    for i in range(len(self.options['ids'])):
      if (self.options['ids'][i] == menuID):
        print(Texts.SEPARATOR2)
        print(f'{Colors.TITLE2}{self.options['ids'][i]} - {self.options['names'][i]}{Colors.END}')
        print(Texts.SEPARATOR2)
  
  def returnOptionNameByID(self, menuID):
    for i in range(len(self.options['ids'])):
      if (self.options['ids'][i] == menuID):
        return self.options['names'][i]
  