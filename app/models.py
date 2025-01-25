from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .db import db

class User(db.Model):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    corbado_user_id: str = Column(String(255), unique=True, nullable=False)
    city: str = Column(String(255), nullable=True, default=None)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User(corbado_user_id='{self.corbado_user_id}', city='{self.city}')>"

    # Optional: Define a __str__ method for string representation
    def __str__(self):
        return f"{self.corbado_user_id} - {self.city}"