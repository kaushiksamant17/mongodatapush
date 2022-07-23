import logging
logging.basicConfig(filename="test7.log",level = logging.INFO ,format ="%(asctime)s %(levelname)s %(name)s %(message)s")

try:
    logging.info("here initiating the file open operation")
    with open("jkl1.txt",'r'):
        pass
except Exception as e:
    logging.debug("no such file exist and logging details is from DEBUG")
    logging.error("no such file exist and logging details is from Error")
    logging.critical(e)
finally:
    a = open("jkl1.txt",'w')
    l = [1,2,3,4,5]
    for i in l:
        a.write("\n")
        a.write(f"the current value is {i} in iteration")
    logging.warning("file operation is completed")
    a.close()

