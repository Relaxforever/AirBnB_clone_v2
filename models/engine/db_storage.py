#!/usr/bin/python3
"""shebang"""

from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """conect to databases"""
    __engine = None
    __session = None

    def __init__(self):
        """Linked to databases dev or db"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host_se = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host_se, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Show all the data"""
        list_t = ['State', 'City']
        dict_table = {}
        if cls is None:
            for class_t in list_t:
                for data in self.__session.query(eval(class_t)).all():
                    key = type(cls).__name__ + '.' + data.id
                    dict_table[key] = data
        else:
            for data in self.__session.query(eval(cls)).all():
                key = type(cls).__name__ + '.' + data.id
                dict_table[key] = data
        return dict_table

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        self.__session = scoped_session(self.__session)
