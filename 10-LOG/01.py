import logging
LOG_FORMAT = "%(asctime)s----%(levelname)s----%(message)s"


logging.basicConfig(filename="text01.log",level=logging.DEBUG,format=LOG_FORMAT)

logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")


# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")