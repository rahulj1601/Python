"""

**************
*            *
*            *
*            *
**************

"""

##def boxPrint(symbol, width, height):
##
##    if len(symbol) != 1:
##        raise Exception("Symbol needs to be a string of length 1.") #returns an error message when some unwanted input is provided
##    # you also get the traceback information to see where the error message originates from
##
##    if (width < 2) or (height < 2):
##        raise Exception("Width and height must be greater or equal to 2")
##    
##    print(symbol * width)
##
##    for i in range(height-2):
##        print(symbol + (' ' * (width-2)) + symbol)
##
##    print(symbol * width)
##
##boxPrint('**', 15, 5)

################################################################################################################################################

##
##import traceback
##
##try:
##    raise Exception('This is the error message.')
##
##except:
##    errorFile = open('error_log.txt', 'a')
##    errorFile.write(traceback.format_exc()) #allows you to access the error message --> traceback.format_exc()
##    errorFile.close()
##    print('Traceback information was written to error_log.txt')
##

################################################################################################################################################


assert False, 'This is the error message.' #assertion statement

market_2nd = {'ns':'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)
    # shows that when the condition is False there is a bug in the program and the error is displayed
    # condition --> 'red' in intersection.values()
    # error message is the second part of the assert statement
            

switchLights(market_2nd)
