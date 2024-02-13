

from sqlalchemy import create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    
    customer = relationship("Customer", back_populates='reviews')
    restaurant = relationship("Restaurant", back_populates='reviews')
     
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Customer: {self.name}'
