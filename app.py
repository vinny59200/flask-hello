import os
from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL
from flask import jsonify

app = Flask(__name__)



mysql = MySQL()
 
# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'sql11418445'    # default user of MySQL to be replaced with appropriate username
app.config['MYSQL_DATABASE_PASSWORD'] = 'a5vzh6NtHK' # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_DB'] = 'sql11418445'  # Database name to be replaced with appropriate database name
app.config['MYSQL_DATABASE_HOST'] = 'sql11.freemysqlhosting.net' # default database host of MySQL to be replaced with appropriate database host
#initialise mySQL
mysql.init_app(app)
#create connection to access data
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
    #create a cursor
    cursor = conn.cursor() 
    #execute select statement to fetch data to be displayed in combo/dropdown
    query_string = "SELECT * FROM question WHERE id = %s"
    cursor.execute(query_string, (id,))
    #fetch all rows ans store as a set of tuples 
    joblist = cursor.fetchall() 
    #render template and send the set of tuples to the HTML file for displaying
    return str(joblist )
	


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)