import logging
logging.basicConfig(filename="test6.log",level = logging.INFO,format ="%(asctime)s %(levelname)s %(name)s %(message)s")

try:
    logging.info("we are try to open file")
    r = open("xyz.txt","r")
except Exception as e:
    logging.error(e)
    logging.critical("new file can't be created in read mode")
finally:
    logging.debug("at any cost , this part should get executed")
    w = open("abc1.txt","w")
    w.writelines("i am writing the line to check kesto1 \n"
                 "khkffk"
                 "ytryui")
    logging.info("writing operation done")
    w.close()
    logging.info("file operation closed")
