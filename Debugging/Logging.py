import logging
logging.basicConfig(filename = 'myProgrammingLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - ?%(message)s')
# Add a filename to write the log messages to an external file, get rid of this if you don't want it
# required at the top of each program using logging

logging.disable(logging.CRITICAL) # remove the logging data that isn't critical
## 5 levels of logging --> (highest) critical, error, warning, info, debug (lowest)

logging.debug('Start of program') # Using logging to see how certain variables change throughout the program

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i = %s, Total = %s' % (i, total)) #change debug to another more important level if needed

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
