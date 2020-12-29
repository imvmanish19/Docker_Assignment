from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def students_db() -> List[Dict]:
            config = {
                    'user': 'root',
                    'password': 'root',
                    'host': 'db',
                    'port': '3306',
                    'database': 'students'
                    }
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM student')
            results = [{name: usn} for (name, usn) in cursor]
            cursor.close()
            connection.close()
            return results
@app.route('/')
def index() -> str:
    return "Hello World ! I am back with db running .!\n"+json.dumps({'Students': students_db()})
if __name__ == '__main__':
    app.run(host='0.0.0.0')
