import os
import sys
import logging
#creating logging string to understand logging format
logging_str="[%(asctime)s: %(levelname)s: %(module)s:%(message)s]"
#naming log dir
log_dir="logs"
#creating log storing filepath
log_filePath=os.path.join(log_dir,'running_log')
os.makedirs(log_dir, exist_ok=True)
#loging pattern configuration
logging.basicConfig(level=logging.INFO,
format=logging_str,
handlers=[
    logging.FileHandler(log_filePath),
    logging.StreamHandler(sys.stdout)
])



logger=logging.getLogger("mlProjectLogger")