from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

@app.route('/')
def debug():
    pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000)
    app.run(host = '0.0.0.0', port = port)