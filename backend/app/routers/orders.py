from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.models.order import Order
from app.models.product import Product
from app.utils.deps import get_db, get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


# ---------------------------
# CREATE ORDER (Buyer only)
# ---------------------------
@router.post("/")
def create_order(
    product_id: int,
    quantity: int,
    session: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    # Check if product exists
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    # Create order
    order = Order(
        product_id=product_id,
        user_id=user.id,
        quantity=quantity
    )

    session.add(order)
    session.commit()
    session.refresh(order)

    return {"message": "Order created", "order": order}


# ---------------------------
# GET ALL ORDERS (Admin only)
# ---------------------------
@router.get("/")
def get_all_orders(
    session: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins only"
        )

    orders = session.exec(select(Order)).all()
    return orders


# ---------------------------
# GET MY ORDERS (Buyer)
# ---------------------------
@router.get("/me")
def get_my_orders(
    session: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    orders = session.exec(select(Order).where(Order.user_id == user.id)).all()
    return orders
