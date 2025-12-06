import shortuuid
from src import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.String(22), primary_key=True, default=lambda: shortuuid.uuid())
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Category {self.name}>"
