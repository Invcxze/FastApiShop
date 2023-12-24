from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base

product_category = Table('product_category', Base.metadata,
                         Column('product_id', Integer,
                                ForeignKey('products.id')),
                         Column('category_id', Integer,
                                ForeignKey('categories.id'))
                         )

# Таблица для связи многие-ко-многим между продуктами и производителями
product_manufacturer = Table('product_manufacturer', Base.metadata,
                             Column('product_id', Integer,
                                    ForeignKey('products.id')),
                             Column('manufacturer_id', Integer,
                                    ForeignKey('manufacturers.id'))
                             )


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    # Другие поля, если необходимо


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    logo = Column(String)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    category = Column(String)
    manufacturer = Column(String)
    characteristics = Column(
        String)  # Может быть JSON-полем или отдельными колонками
    price = Column(Integer)
    availability = Column(Integer)
    photos = relationship("ProductPhoto", back_populates="product")


class ProductPhoto(Base):
    __tablename__ = 'product_photos'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="photos")


# class CartItem(Base):
#     __tablename__ = 'cart_items'
#
#     id = Column(Integer, primary_key=True, index=True)
#     product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))
#     quantity = Column(Integer)
#     # user_id = Column(Integer, ForeignKey('users.id'))
#

# class Notification(Base):
#     __tablename__ = 'notifications'
#
#     id = Column(Integer, primary_key=True, index=True)
#     product_id = Column(Integer, ForeignKey('products.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     is_notified = Column(Boolean, default=False)
