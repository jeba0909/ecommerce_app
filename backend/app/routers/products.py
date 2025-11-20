from fastapi import APIRouter, Depends, HTTPException

from sqlmodel import Session

from app.utils.deps import get_session, get_current_user
from app.models.user import User, UserRole
from app.schemas.product import ProductCreate, ProductUpdate, ProductRead
from app.crud.product import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)

router = APIRouter(prefix="/products", tags=["Products"])


# -----------------------------
# GET ALL PRODUCTS
# -----------------------------
@router.get("/", response_model=list[ProductRead])
def list_products(
    session: Session = Depends(get_session)
):
    return get_all_products(session)


# -----------------------------
# CREATE PRODUCT (Admin + Seller only)
# -----------------------------
@router.post("/", response_model=ProductRead)
def add_product(
    payload: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in [UserRole.admin, UserRole.seller]:
        raise HTTPException(status_code=403, detail="Not authorized")

    return create_product(session, payload, current_user.id)


# -----------------------------
# UPDATE PRODUCT
# -----------------------------
@router.put("/{product_id}", response_model=ProductRead)
def edit_product(
    product_id: int,
    payload: ProductUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    product = get_product_by_id(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Only the seller who created or admin can update
    if current_user.role != UserRole.admin and product.seller_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    return update_product(session, product, payload)


# -----------------------------
# DELETE PRODUCT
# -----------------------------
@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    product = get_product_by_id(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if current_user.role != UserRole.admin and product.seller_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    delete_product(session, product)
    return {"message": "Product deleted"}
