from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_final'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/ROG/PycharmProjects/PP_Vue_Midterm/database.db'
db = SQLAlchemy(app)

import routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
