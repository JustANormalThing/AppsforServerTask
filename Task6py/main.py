from flask import Flask
import logging
import logging.config


app = Flask(__name__)
                    
logging.config.fileConfig('temp.conf')

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/Log')
def Logger():
    logger.debug('This is a debug')
    logger.info('Tihs is info')
    logger.warning('war')
    logger.error('Error')
    return 'Hello'
    

if __name__ == '__main__':
    app.run()