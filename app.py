from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    complete=db.Column(db.Boolean)
@app.route('/')
def index():
    #sjow all todos
    todo_list=ToDo.query.all()
    print(todo_list)
    return render_template('base.html',todo_list=todo_list)
@app.route('/add',methods=['POST'])
def add():
    title=request.form.get('title')
    new_todo=ToDo(title=title,complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


# Only create tables if the script is run directly, not when imported as a module
if __name__ == '__main__':
    # Import your models here

    # Create tables
    with app.app_context():
        db.create_all()

    # Run the development server
    app.run(debug=True)
