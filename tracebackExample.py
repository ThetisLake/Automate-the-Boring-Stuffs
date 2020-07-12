import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open(r'C:\Users\erich\Desktop\Python\error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')

    
