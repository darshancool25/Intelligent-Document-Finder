from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "<p>This is Home Page!</p>"

@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':
        result = request.form['myfile']
    else:
        result = request.args.get['myfile']
    return result