from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from classes.model import Model


class Table(Base):

    def __init__(self, model: Model):
        __tablename__ = model.name

        for column in model.columns:
            if column == model.primary_key:
                setattr(self, column, Column(Integer, primary_key=True))
            elif column in model.unique:
                setattr(self, column, Column(String, unique=True))
            elif column in model.foreign_key:
                setattr(
                    self, column, Column(Integer, ForeignKey(model.foreign_key[column]))
                )
                setattr(self, column + "_obj", relationship(model.foreign_key[column]))
            else:
                setattr(self, column, Column(String))
