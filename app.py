from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['new-todo']
        desc = request.form['new-desc']
        new_todo = Todo(title=title, desc=desc)
        db.session.add(new_todo)
        db.session.commit()

    allTodo = Todo.query.all()
    css_url = url_for('static', filename='style.css')
    return render_template('index.html', css_url=css_url, allTodo=allTodo)

if __name__ == "__main__":
    app.run(debug = True)
