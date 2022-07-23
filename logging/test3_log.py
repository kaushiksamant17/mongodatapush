import logging
logging.basicConfig(filename="test3.log",level=logging.DEBUG,format='%(asctime)s %(name)s %(message)s')
logging.info("this is my log with timestamp")

"""format keyword works in a better way to organize the log 
input in a better way that each of the meassage can be arranged
in the way that the person want to see.
in the above example in format we have mention the code
to use the systme time that is asctime , then use the 
username , and then display the messages"""