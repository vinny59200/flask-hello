import os
from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL
from flask import jsonify
from random import randint
import logging
import json

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

mysql = MySQL()

# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'sql11418445'  # default user of MySQL to be replaced with appropriate username
app.config[
    'MYSQL_DATABASE_PASSWORD'] = 'a5vzh6NtHK'  # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_DB'] = 'sql11418445'  # Database name to be replaced with appropriate database name
app.config[
    'MYSQL_DATABASE_HOST'] = 'sql11.freemysqlhosting.net'  # default database host of MySQL to be replaced with appropriate database host
# initialise mySQL
mysql.init_app(app)
# create connection to access data
conn = mysql.connect()


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/question/<idQuestion>')
def user(idQuestion):
    return jsonify(
        question="EN 1990, 4 PERSONNES SUR 10 VIVAIENT SOUS LE SEUIL DE PAUVRETE EXTREME. COMBIEN DE PERSONNES VIVENT ACTUELLEMENT SOUS CE SEUIL? A)1 sur 10 | B)3 sur 10 | C)5 sur 10",
        answer="A",
        id="2"
    )


@app.route('/select/<id>')
def select(id):
    # create a cursor
    cursor = conn.cursor()
    # execute select statement to fetch data to be displayed in combo/dropdown
    query_string = "SELECT * FROM question WHERE id = %s"
    cursor.execute(query_string, (id,))
    # fetch all rows ans store as a set of tuples
    joblist = cursor.fetchone()
    # render template and send the set of tuples to the HTML file for displaying
    return str(joblist)


@app.route('/send/', methods=['POST'])
def send():
    data = request.json  # a multidict containing POST data
    id = data['id']
    app.logger.info(id)
    questionFromFront = data['question']
    answerFromFront = data['answer']
    print(answerFromFront)

    cursor = conn.cursor()
    print("Connected to database")
    query = "SELECT * FROM question WHERE id = %s"
    cursor.execute(query, (id,))
    record = cursor.fetchone()
    idFromDB = record[0]
    app.logger.info(idFromDB)
    # questionFromDB = record['question']
    answerFromDB = record[2]
    karma = record[3]
    print(answerFromDB)
    cursor.close()

    if answerFromFront == answerFromDB:
        print("karma +1")
        mycursor = conn.cursor()

        sql = "UPDATE question SET karma = %s WHERE id = %s"

        mycursor.execute(sql, (karma + 1, idFromDB,))

        conn.commit()
    else:
        print("karma -1")
        mycursor = conn.cursor()

        sql = "UPDATE question SET karma = %s WHERE id = %s"

        mycursor.execute(sql, (karma - 1, idFromDB,))

        conn.commit()

    # create a cursor
    cursor = conn.cursor()
    # execute select statement to fetch data to be displayed in combo/dropdown
    query_string = "SELECT * FROM question WHERE id = %s"
    value = randint(2, 171)
    cursor.execute(query_string, (value,))
    # fetch all rows ans store as a set of tuples
    # render template and send the set of tuples to the HTML file for displaying
    row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    rv = cursor.fetchone()
    json_data = []
    json_data.append(dict(zip(row_headers, rv)))
    return json.dumps(json_data[0])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
