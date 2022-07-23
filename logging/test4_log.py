import logging
logging.basicConfig(filename="test4.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")

def debide(a,b):
    logging.info(f"the number entered by user is {a} and {b}")
    try:
        logging.info("we are in function")
        div = a/b
        logging.info("we have completed division")
        logging.info("the value of division is %s",div)
    except Exception as e:
        logging.error(e)



debide(4,0)
debide(8,2)

'''Normally in the arguement list of basicCOnfig we provide the value
for level=logging.INFO , this means anything high here the value of 
error level as info those things will get captured in the logs 
if we put level = logging.Error then in that case anything equal
to level of Error or higher will get printed all other things 
will not get printed.
as we know the heirarchy. 
10 : debug
20: info
30:warning
40:error
50:critical'''