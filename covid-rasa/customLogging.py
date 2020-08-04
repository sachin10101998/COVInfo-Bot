import logging
import urls
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(levelname)8s | %(filename)10s:%(funcName)15s:%(lineno)3s |  - %(message)s')


if urls.uri=="https://renee.piri.ai":
   	file_handler = logging.FileHandler(urls.LOG_FILE)      #for prod
else:
   	file_handler = logging.FileHandler(urls.LOG_FILE)      #for local

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(logging.Formatter('%(filename)10s:%(funcName)10s:%(lineno)3s |  - %(message)s'))

logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
