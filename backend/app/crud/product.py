from sqlmodel import Session, select
from app.models.product import Product
from datetime import datetime


def create_product(session: Session, data, seller_id: int):
    product = Product(
        name=data.name,
        description=data.description,
        price=data.price,
        quantity=data.quantity,
        seller_id=seller_id
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def get_all_products(session: Session):
    return session.exec(select(Product)).all()


def get_product_by_id(session: Session, product_id: int):
    return session.get(Product, product_id)


def update_product(session: Session, product: Product, data):
    product.name = data.name
    product.description = data.description
    product.price = data.price
    product.quantity = data.quantity
    product.updated_at = datetime.utcnow()

    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def delete_product(session: Session, product: Product):
    session.delete(product)
    session.commit()
    return True
