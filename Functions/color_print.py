# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str,*effects: str) -> None:
    '''
    prints text in color using ANSI code defined in begining of module
    :param text: text to be printed
    :param effects: color we want to introduce
    '''
    effects_string="".join(effects)
    print(effects_string)
    print("{0}{1}{2}".format(effects_string,text,RESET))


color_print("what is this",BLUE)
color_print("what is this",BLUE,BOLD)
print('done')