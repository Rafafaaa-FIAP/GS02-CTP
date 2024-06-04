
class Colors:
  ''' ANSI color codes '''
  BLACK = '\033[0;30m'
  RED = '\033[0;31m'
  GREEN = '\033[0;32m'
  BROWN = '\033[0;33m'
  BLUE = '\033[0;34m'
  PURPLE = '\033[0;35m'
  CYAN = '\033[0;36m'
  LIGHT_GRAY = '\033[0;37m'
  DARK_GRAY = '\033[1;30m'
  LIGHT_RED = '\033[1;31m'
  LIGHT_GREEN = '\033[1;32m'
  YELLOW = '\033[1;33m'
  LIGHT_BLUE = '\033[1;34m'
  LIGHT_PURPLE = '\033[1;35m'
  LIGHT_CYAN = '\033[1;36m'
  LIGHT_WHITE = '\033[1;37m'
  BOLD = '\033[1m'
  FAINT = '\033[2m'
  ITALIC = '\033[3m'
  UNDERLINE = '\033[4m'
  BLINK = '\033[5m'
  NEGATIVE = '\033[7m'
  CROSSED = '\033[9m'
  END = '\033[0m'
  TITLE1 = LIGHT_BLUE
  TITLE2 = LIGHT_PURPLE
  INPUT = LIGHT_GREEN
  ERROR = LIGHT_RED
  TEMPERATURE = '#36A2EB'
  TURBIDITY = '#FF6384'

  def showColors():
    print(f'{Colors.BLACK} BLACK {Colors.RED} RED {Colors.GREEN} GREEN {Colors.BROWN} BROWN {Colors.BLUE} BLUE {Colors.PURPLE} PURPLE {Colors.CYAN} CYAN {Colors.LIGHT_GRAY} LIGHT_GRAY {Colors.DARK_GRAY} DARK_GRAY {Colors.LIGHT_RED} LIGHT_RED {Colors.LIGHT_GREEN} LIGHT_GREEN {Colors.YELLOW} YELLOW {Colors.LIGHT_BLUE} LIGHT_BLUE {Colors.LIGHT_PURPLE} LIGHT_PURPLE {Colors.LIGHT_CYAN} LIGHT_CYAN {Colors.LIGHT_WHITE} LIGHT_WHITE {Colors.BOLD} BOLD {Colors.FAINT} FAINT {Colors.ITALIC} ITALIC {Colors.UNDERLINE} UNDERLINE {Colors.BLINK} BLINK {Colors.NEGATIVE} NEGATIVE {Colors.CROSSED} CROSSED {Colors.END} END ')

class Texts:
  SEPARATOR1 = f'{Colors.TITLE1}--------------------------------------------------{Colors.END}'
  SEPARATOR2 = f'{Colors.TITLE2}-------------------------{Colors.END}'
  LINK_SITE = f'{Colors.BLUE}{Colors.UNDERLINE}https://rafafaaa-fiap.github.io/GS02-FRO{Colors.END}'
