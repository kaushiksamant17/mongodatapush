import logging
logging.basicConfig(filename= "test2.log",level=logging.INFO)
logging.info("this is info logging")
logging.warning("this is a warning")
l=[1,2,4,5,3,2,2,2]
for i in l:
    if i == 2:
        logging.error(f"the number is equal to {i}")

'''here we are just trying to logging different 
level of logs'''