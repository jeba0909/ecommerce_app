from sqlmodel import Session, select
from app.models.user import User
from app.models.product import Product


def create_order(session: Session, buyer_id: int, product: Product, quantity: int):
    total_price = product.price * quantity

    order = Order(
        buyer_id=buyer_id,
        product_id=product.id,
        quantity=quantity,
        total_price=total_price
    )
    session.add(order)

    # Decrease product stock
    product.quantity -= quantity
    session.add(product)

    session.commit()
    session.refresh(order)

    return order


def get_orders_by_user(session: Session, user_id: int):
    return session.exec(select(Order).where(Order.buyer_id == user_id)).all()


def get_all_orders(session: Session):
    return session.exec(select(Order)).all()
