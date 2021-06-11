import os
from flask import Flask
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
from flask import jsonify

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql11.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql11418445'
app.config['MYSQL_PASSWORD'] = 'a5vzh6NtHK'
app.config['MYSQL_DB'] = 'sql11418445'

mysql = MySQL(app)

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

    db = MySQLdb.connect("sql11.freemysqlhosting.net","sql11418445","a5vzh6NtHK","sql11418445" )

    cursor = db.cursor()

    query_string = "SELECT * FROM question WHERE id = %s"
    cursor.execute(query_string, (id,))

    data = cursor.fetchall()

    db.close()

    return str(data[0])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)