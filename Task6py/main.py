from flask import Flask
import sqlite3
import logging
import logging.config
import redis

r = redis.Redis(host ='localhost',port = 6379 ,db = 0)
response = r.ping()
print('Response:',response)

conn = sqlite3.connect('NewDb.db')
cursor = conn.cursor()

table_creation_query = """
    CREATE TABLE NEW (
        Email VARCHAR(255) NOT NULL,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(25),
        Score INT
    );
"""
cursor.execute("DROP TABLE IF EXISTS NEW")
cursor.execute(table_creation_query)
cursor.execute("INSERT INTO NEW VALUES ('Remelia@gmail.com', 'Remi', 'Scarlet','100')")
conn.commit()
conn.close()



app = Flask(__name__)
                    
logging.config.fileConfig('temp.conf')

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('NewDb.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM NEW''')
    results = cursor.fetchall()
    conn.close()
    return (results)

@app.route('/Log')
def Logger():
    logger.debug('This is a debug')
    logger.info('Tihs is info')
    logger.warning('war')
    logger.error('Error')
    return 'Hello'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)