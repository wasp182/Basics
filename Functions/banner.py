def banner(text: str = " ",screen: int = 80) -> None:
    '''
    Prints string of text in specified length with ** as beginning and ending
    :param text: `str` text to be printed.
                Asterix (*) will result in line of astrix to be printed within "**" on
                either side
    :param screen: `int` length of area where text is to be printed
    :raises ValueError: raises a value error if text is longer than specifed area
    '''
    #screen=80 (no space) is the preferred mode of giving default values
    if len(text)>=screen-4:
        print('text too long to fit in banner')
        raise ValueError("string too long")
    if text=="*":
        print("*" * screen)
    else:
        print("**{}**".format(text.center(screen-4)))


banner("rahul")
banner(screen=80)