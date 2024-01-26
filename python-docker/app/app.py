from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        conn = psycopg2.connect(host="postgresql_container",port="5432",database="postgres",user="postgres",password="postgres")
        return 'Hello, Dockereeeee!'
    except:
        return 'No connect!'