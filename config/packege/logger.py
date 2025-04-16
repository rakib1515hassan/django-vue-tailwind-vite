import os
import dotenv
import environ

env = environ.Env()
env.read_env()
django_setting = env('DJANGO_SETTINGS', default='local')

import logging.config
from config.env import BASE_DIR, env
from django.conf import settings



# Create the logs directory if it doesn't exist
log_dir = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '{asctime}:{levelname}:: {message}',
            # 'format': '{asctime}:{levelname} -{name} {module}.py :: {message}',
            # 'format': '{levelname} {asctime} {module} {message}',
            # 'format': '{levelname} {asctime} (File: {filename}, Line: {lineno}):: {message} ',
            # 'format': '{levelname} {asctime} {module} (File: {filename}, Line: {lineno}):: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'general_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'default',
        },
        'info_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'info.log'),
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'default',
        },
        'error_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'error.log'),
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'default',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'general_file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'info_logger': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'error_logger': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {  # Root logger for all apps
            'handlers': ['console', 'general_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}




# logger.debug("Debug information")
# logger.info("Informational message")
# logger.warning("A warning message")
# logger.error("An error occurred")
# logger.critical("Critical issue encountered")
