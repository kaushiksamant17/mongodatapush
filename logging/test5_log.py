import logging
logging.basicConfig(filename = "test5.log",level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")

try:
    logging.info("i am trying to read a file")
    with open("abc.txt",'r'):
        logging.info("the new file has been created as it is in write mode")
except Exception as e:
    logging.error(e)
    logging.critical("the mode of operation is read and no such file eixist")