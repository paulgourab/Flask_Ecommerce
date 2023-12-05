from shop import app
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from shop import db 

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    profile: Mapped[str] = mapped_column(String, unique=False, nullable=False, default='profile.jpg')

    def __repr__(self) -> str:
        return '<User %r>' % self.username




with app.app_context():
    db.create_all()
