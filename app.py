from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://username:password@server/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    css_url=url_for('static', filename='style.css')
    return render_template('index.html', css_url=css_url)

if __name__ == "__main__":
    app.run(debug = True)

