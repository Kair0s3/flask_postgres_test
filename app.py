from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import urllib.parse

app = Flask(__name__)

# Please note to type your creds as follows into dump.txt - USER:PASS
with open('dump.txt') as dump:
    creds = dump.read().strip()
    split = creds.split(':')
    # URL-encode incase, the user/pass contains special characters (esp. @ and :)
    db_user = urllib.parse.quote_plus(split[0])
    db_pass = urllib.parse.quote_plus(split[1])

server = "localhost:5432"
db_name = "test" # Currently using test table

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{server}/{db_name}'

db = SQLAlchemy(app) # Creates the SQLAlchemy Object

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    resp = insertNewUser(request.form['username'], request.form['password'])
    return resp

@app.route('/listAll')
def listAll():
    if request.method == "GET":
        res = getAllUsers()
        return render_template('listAll.html', records=res)

# Database Operation Methods/functions
def insertNewUser(username, password):
    query = """insert into users (username, password) values (%s, %s);""" # Parameterized Queries
    with db.engine.connect() as conn:
        res = conn.execute(query, (username, password))
    # For Insert functions - probably using try catch, if error caught, insertion failed, since no resp due to insertion operation
    return "Created New User!"

def getAllUsers():
    query = """select * from users;"""
    with db.engine.connect() as conn:
        res = conn.execute(query)
    return res

if __name__ == '__main__':
    app.run(debug=True)

# Custom Queries using SQLAlchemy (1min onwards) - https://www.youtube.com/watch?v=FEtJgtmogSY
# @ inside password field - https://stackoverflow.com/questions/58661569/password-with-cant-connect-the-database
# https://stackoverflow.com/questions/5491140/incrementing-on-errors
