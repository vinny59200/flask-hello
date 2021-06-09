import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
	
@app.route('/question/<idQuestion>')
def user(idQuestion):
	 return jsonify(
        question="EN 1990, 4 PERSONNES SUR 10 VIVAIENT SOUS LE SEUIL DE PAUVRETÉ EXTRÊME. COMBIEN DE PERSONNES VIVENT ACTUELLEMENT SOUS CE SEUIL? A)1 sur 10 | B)3 sur 10 | C)5 sur 10",
        answer="A",
        id="2"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)