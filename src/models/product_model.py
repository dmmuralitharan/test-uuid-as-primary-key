import uuid
from src import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Product {self.name}>"
