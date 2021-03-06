import logging
import logging.config
from colorlog import ColoredFormatter

REVIEWS_URL = 'http://itunes.apple.com/us/rss/customerreviews/page={0}/id={1}/sortby=mostrecent/{2}'

MONGO_DB = 'app'
MONGO_CONNECTION_STRING = 'mongodb://x3/%s' % MONGO_DB

REDIS_HOSTNAME = 'x0'
REDIS_PORT = 6379

CELERY_PIDFILE = '/var/run/celery.pid'
CELERY_LOGFILE = '/var/log/celery'
FLOWER_PIDFILE = '/var/run/celery-flower.pid'
FLOWER_LOGFILE = '/var/log/celery-flower'

INIT_HOSTS = ['x0', 'bshank12']
X_HOSTS = ['x{0}'.format(i) for i in xrange(0,6)]
MONGOS_HOSTS = ['x{0}'.format(i) for i in xrange(3,6)]
MONGOD_CONFIG_HOSTS = ['x{0}'.format(i) for i in xrange(0,3)]

BEAT_HOST = 'x0'
FLOWER_HOST = 'x0'
WORKER_HOSTS = ['x{0}'.format(i) for i in xrange(1,6)]

def configure_logging():
	FORMAT = '%(log_color)s %(levelname)-8s%(reset)s %(bold_blue)s%(message)s'
	formatter = ColoredFormatter(
	    FORMAT,
	    datefmt = None,
	    reset = True,
	    log_colors = {
	        'DEBUG': 'cyan',
	        'INFO': 'green',
	        'WARNING': 'yellow',
	        'ERROR': 'red',
	        'CRITICAL': 'red'
	    }
	)

	logging.config.dictConfig({
	    'version': 1,
	    'formatters': {
	        'colored': {
	            '()': 'colorlog.ColoredFormatter',
	            'format': FORMAT
	        }
	    },
	    'handlers': {
	        'console': {
	            'class': 'logging.StreamHandler',
	            'level': 'INFO',
	            'formatter': 'colored',
	            'stream': 'ext://sys.stdout'
	        }
	    },
	    'root': {
	        'level': 'INFO',
	        'handlers': ['console']
	    }
	})
	logging.getLogger('requests').setLevel(logging.WARNING)
