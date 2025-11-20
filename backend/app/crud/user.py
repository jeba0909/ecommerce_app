from sqlmodel import Session, select
from app.models.user import User, UserRole
from app.core.security import get_password_hash
from app.models.product import Product
from app.models.order import Order


def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()


def create_user(session: Session, full_name: str, email: str, password: str, role: UserRole = UserRole.buyer):
    hashed_password = get_password_hash(password)
    user = User(
        full_name=full_name,
        email=email,
        hashed_password=hashed_password,
        role=role
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_id(session: Session, user_id: int):
    return session.exec(select(User).where(User.id == user_id)).first()


def update_user_role(session: Session, user_id: int, new_role: UserRole):
    user = get_user_by_id(session, user_id)
    if not user:
        return None
    user.role = new_role
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
