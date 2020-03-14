import logging

#Enabling logging

log_filename = 'logs_multilogin.log'
log_filemode = 'w'
log_level = logging.DEBUG
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
log_datefmt='%m-%d-%Y %H:%M:%S'

logging.basicConfig(filename=log_filename, filemode=log_filemode, level=log_level, format=log_format, datefmt=log_datefmt)
logger = logging.getLogger('telegram_logs')

logger.info("This info goes to logs")
logger.warning("This one as well")