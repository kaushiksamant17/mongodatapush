import logging
logging.basicConfig(filename ="test1.log",level=logging.INFO)

logging.info("this is my first code for logging")
l =[1,2,3,4,4,5,6,7,3,3]

for i in l:
    if i == 3:
        logging.info(i)

'''Here the logging works in a way to include all the values
of the print statement that we use to get the output after
few line of code we use logging to store the data in the differen
file that can be used by the programmers to store the info
of working code. NOrmally it has different level ranging
from 10 to 50
where 10 is lowest and 50 is highest
10 : Debug, 20: Info , 30: Warning , 40: Error , 50: Critical'''