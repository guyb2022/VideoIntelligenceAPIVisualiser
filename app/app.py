import os
from flask import Flask, request, render_template, Response
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import HTTPException, NotFound
import google.auth

execution_path = os.getcwd()

app = Flask(__name__)
CORS(app)

logging.getLogger().setLevel(logging.INFO)
service_account_path = 'app/credentials/client-secret.json'

@app.route("/", methods= ['GET','POST'])
@cross_origin()
def homepage(): # Redirecting to home page
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))



