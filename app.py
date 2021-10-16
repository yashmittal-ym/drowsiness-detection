from flask import Flask, Response, render_template, request
from dd import fun
app = Flask(__name__)

link = ''

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("contact.html")
 
@app.route('/results', methods=['GET', 'POST'])
def runIt():
    global link
    if request.method == 'POST':
        link = request.form['link']
    return Response(fun(link),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
	app.run(debug=True, port=8000,threaded=True)