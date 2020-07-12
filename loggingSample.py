import logging

#default syntax for logging
logging.basicConfig(filename=(r'C:\Users\erich\Desktop\Python\debug.txt'),format='%(asctime)s - %(levelname)s - %(message)s')

#the code below disables print function for debug until it is critical
logging.disable(logging.CRITICAL)

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)'%(n))
    total=1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is %s, total is %s'%(i,total))
        
    logging.debug('Return value is %s' %(total))
    return total


print(factorial(5))
logging.debug('End of program')
