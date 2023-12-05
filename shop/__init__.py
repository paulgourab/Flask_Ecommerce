from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# configure the extention

#create the app
app = Flask(__name__)
#configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"
app.config['SECRET_KEY']='ATT2023'
#initialize the app with the extension
db.init_app(app)
bcrypt = Bcrypt(app)


from shop.admin import routes


