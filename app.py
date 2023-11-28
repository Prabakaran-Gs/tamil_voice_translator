from flask import Flask , render_template , url_for ,request
from transulate import trans

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/play' , methods=['GET', 'POST'])
def play():
    if request.method == 'POST' :
        statement = request.form.get('statement')
        trans(statement)
    return render_template("play.html")
                              

if __name__ == '__main__':
    app.run(debug=True)